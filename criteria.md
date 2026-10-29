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
     ───────────────────────────────────────────────────────────────────────── -->
