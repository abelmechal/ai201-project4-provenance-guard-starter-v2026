# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. False-Positive Target

Across each of the three evaluation trials, of 10 pieces of writing I created myself, at most 0 may be labeled high-confidence AI.

**Why this target:**

A false accusation matters because falsely labeling authentic student work as AI-generated carries severe academic integrity penalties, damages trust between students and educators, and creates anxiety for innocent authors. A zero-tolerance false-positive rate (0 out of 10) sets a strict standard for this evaluation.



---

## 2. Label-Coverage Target

Across each of the three evaluation trials, of 6 deliberately selected test inputs, all three labels—`human`, `unsure`, and `ai`—must appear at least once.

**Test input breakdown:**

- **2 clearly human-authored texts:** Unedited personal reflections, drafts, or published writing known to predate modern LLMs.
- **2 ambiguous or hybrid texts:** Human-drafted text lightly edited by AI, or highly formal, formulaic human writing designed to test the model's uncertainty threshold.
- **2 pure AI-generated texts:** Raw, unedited responses generated directly by an LLM from standard prompts.

**Why this target:**

A functional provenance guard must demonstrate active decision boundaries across the full spectrum of writing. Requiring all three labels prevents the system from collapsing into an overconfident binary classifier that forces artificial certainty onto nuanced, hybrid text, while ensuring it still decisively recognizes unambiguous human and AI writing.



---

## 3. Appeal-Path Target

Across each of the three evaluation trials, I will test 2 valid appeals submitted against flagged items: one following a high-confidence `ai` label and one following an `unsure` label. Each appeal must return an immediate successful confirmation, report `under_review` status, and create a `/log` entry containing the content ID, timestamp, and appeal rationale.

**Why this target:**

Because automated AI detectors are probabilistic and prone to false positives, authors require a clear way to challenge a decision. Recording the appeal as `under_review` gives a reviewer an auditable, verifiable record and prevents the challenge from being silently dropped or ignored.



---

## 4. Bad-Input Target

Across each of the three evaluation trials, I will test 3 malformed requests representing the primary input-validation boundaries. Missing or empty `text` and missing `creator_id` must return HTTP `400` with a descriptive JSON error message; text exceeding the character limit must return HTTP `413` with a descriptive JSON error message. Every rejected request must create an audit-log entry recording the timestamp and rejection reason, and the service must remain responsive to a subsequent valid request.

**Why this target:**

A production service must withstand malformed or malicious inputs without crashing. Uncaught exceptions or unbounded payloads can exhaust server memory, trigger denial-of-service conditions, and take the system offline for legitimate users. Handling bad inputs gracefully at the boundary ensures high availability, provides actionable feedback so developers can correct malformed requests, and preserves an audit record of rejected activity.



---

## 5. Score-Separation Target

Across each of the three evaluation trials, I will evaluate 5 clearly human-authored texts and 5 clearly AI-generated texts (10 total samples) to measure score separation. The average confidence score of the AI group must exceed the average confidence score of the human group by at least 0.50. The lowest-scoring AI text must also score higher than the highest-scoring human text, creating zero rank overlap on these unambiguous inputs.

**Why this target:**

A meaningful classification engine must exhibit wide discriminative separation on polar, unambiguous test cases. If a detector groups both human and AI samples within a narrow score band, such as 0.40 to 0.60, it demonstrates weak signal capture and high vulnerability to random noise. Enforcing an average spread of at least 0.50 tests whether the underlying heuristics produce a decisive, polarized score distribution rather than returning nearly the same score for every input.



---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
-->

# Capstone Acceptance Criteria

## 1. Bounded detector timeout

**Criterion:** When detector scoring runs longer than the configured 15.0-second limit, the API must stop waiting—while letting the background detector task finish—and return an HTTP 503 Service Unavailable JSON response containing an `error` field whose value is `detector_timeout` (alongside its descriptive `message` field) within 15.5 seconds of the request across 3 of 3 trials.

**Target:** Maximum caller wait time of 15.5 seconds for the 15.0-second timeout setting, HTTP 503, and JSON error value `detector_timeout`, allowing additional fields such as `message`, in 3 of 3 trials.

**How I will test it:** I will configure a controlled test hook on the detector scoring step to sleep for 18.0 seconds, send a valid `POST /submit` request, and record its wall-clock duration, status, and error field. I will poll `GET /health` until `detector_runtime.in_flight` becomes false between runs and repeat this three times.

**Why this target:** Writers actively drafting or reviewing text cannot have their UI hang indefinitely on a stalled detector call; returning a predictable 503 at 15 seconds keeps the client responsive so they can continue editing.

## 2. Timeout audit record

**Criterion:** Every `POST /submit` request that hits the 15.0-second detector timeout must write an audit log entry containing `reason: "detector_timeout"`, `failure_stage: "detector"`, `duration_ms` at least 15000, `input_summary.text_length` matching the submitted character count, and `output_summary.http_status: 503` in 3 of 3 trials.

**Target:** All 5 of 5 exact audit fields and values are present across 3 of 3 timeout trials.

**How I will test it:** I will trigger an 18.0-second simulated detector delay with submissions of distinct, known character lengths, then inspect the matching audit entry after each run. I will verify the five required fields without storing raw text or hashes.

**Why this target:** Preserving writer privacy while capturing exact failure-stage and text-length metrics lets me diagnose whether timeouts correlate with long submissions or model slowdowns without logging sensitive draft content.

## 3. Busy-worker protection

**Criterion:** While a slow detector task is still finishing in the background after its original caller timed out at 15.0 seconds, a second `POST /submit` request must be rejected within 0.5 seconds with HTTP 503 and a JSON `error` field whose value is `detector_busy`, alongside its descriptive message, in 3 of 3 trials.

**Target:** Rejection in 0.5 seconds or less, HTTP 503, and JSON error value `detector_busy` across 3 of 3 trials. No `Retry-After` header is required.

**How I will test it:** I will submit a request with a 20.0-second simulated detector delay. At the 16.0-second mark, while `GET /health` reports `detector_runtime.in_flight` as true, I will send a second valid request and measure its response. I will wait for the health endpoint to report false and repeat for three total trials.

**Why this target:** Failing fast when the single detector worker is still occupied prevents request pile-ups and memory exhaustion on local hardware, protecting overall service stability.

## 4. Recovery after a slow job

**Criterion:** Within 1.0 second after `GET /health` reports `detector_runtime.in_flight` is false following a slow detector job, a subsequent valid `POST /submit` request must succeed with HTTP 201 Created and return `content_id`, `confidence`, `guess`, `label`, `model_score`, and `style_score` in 3 of 3 trials.

**Target:** HTTP 201 and all 6 of 6 response fields on the first request submitted within 1.0 second of `detector_runtime.in_flight` becoming false across 3 of 3 trials.

**How I will test it:** I will trigger a 17.0-second slow job that times out to its caller at 15.0 seconds, poll the health endpoint until `detector_runtime.in_flight` changes from true to false, then send a normal un-delayed submission within 1.0 second. I will repeat this timeout-to-recovery cycle three times.

**Why this target:** A single slow inference pass must not leave the worker permanently locked; automatic recovery ensures writers can resume checking provenance after a transient slowdown without a manual service restart.

## 5. Normal-path regression check

**Criterion:** When the detector is healthy and idle (`detector_runtime.in_flight` is false), an ordinary valid `POST /submit` request must return HTTP 201 Created within 8.0 seconds, with `content_id`, `confidence`, `guess`, `label`, `model_score`, and `style_score` in the response, and record `duration_ms` under 8000, `input_summary.text_length`, and `output_summary.http_status: 201` in the audit log, in 3 of 3 trials.

**Target:** HTTP 201, response time of 8.0 seconds or less on local CPU, all 6 of 6 response fields, and all 3 baseline audit fields across 3 of 3 trials.

**How I will test it:** With no artificial delays active and `GET /health` showing the detector idle, I will submit a standard approximately 200-word writing sample. I will verify the status, duration, six JSON fields, and audit fields, then repeat with three different valid writing samples.

**Why this target:** Adding timeout wrappers and busy-worker guards must not alter scoring outputs, HTTP status codes, or privacy-preserving audit logs on the standard happy path that writers rely on every day.

<!--
     ───────────────────────────────────────────────────────────────────────── -->
