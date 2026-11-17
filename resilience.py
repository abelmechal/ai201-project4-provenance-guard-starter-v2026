"""Bounded access to the local detector used by the submission route."""

from concurrent.futures import ThreadPoolExecutor, TimeoutError
import threading
import time

import config
import detector


class DetectorTimedOut(RuntimeError):
    """The request waited too long for a detector result."""


class DetectorBusy(RuntimeError):
    """A previous detector call is still running after its caller timed out."""


_executor = ThreadPoolExecutor(max_workers=1, thread_name_prefix="detector")
_state_lock = threading.Lock()
_in_flight = False


def _score_with_optional_test_delay(text: str) -> float:
    """Delay only in explicitly enabled local test mode, then score normally."""
    delay = config.test_detector_delay_seconds()
    if delay:
        time.sleep(delay)
    return detector.model_signal(text)


def _mark_idle(_future) -> None:
    """Release the single scoring slot when the worker eventually finishes."""
    global _in_flight
    with _state_lock:
        _in_flight = False


def score_text(text: str) -> float:
    """
    Score one text with a bounded caller wait.

    Python cannot safely kill a running PyTorch operation from another thread.
    Instead, this gives the caller a bounded wait and reserves the one worker
    until it finishes. This keeps later requests from queueing behind a stuck
    task and makes the overload visible as an explicit ``DetectorBusy`` state.
    """
    global _in_flight
    with _state_lock:
        if _in_flight:
            raise DetectorBusy("The detector is still finishing an earlier request.")
        _in_flight = True

    future = _executor.submit(_score_with_optional_test_delay, text)
    future.add_done_callback(_mark_idle)
    try:
        return future.result(timeout=config.DETECTOR_TIMEOUT_SECONDS)
    except TimeoutError as exc:
        raise DetectorTimedOut(
            f"Detector did not finish within {config.DETECTOR_TIMEOUT_SECONDS:g} seconds."
        ) from exc


def status() -> dict:
    """Return the small amount of runtime state safe to expose on /health."""
    with _state_lock:
        return {
            "in_flight": _in_flight,
            "timeout_seconds": config.DETECTOR_TIMEOUT_SECONDS,
        }
