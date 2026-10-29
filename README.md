# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

1. A writer sends `text` and `creator_id` to `POST /submit`.
2. The service rejects malformed, empty, or oversized input with a clear error and an audit entry.
3. The local GPT-2 detector scores how predictable the writing is.
4. The stylometry signal measures sentence-length variation, vocabulary variety, and punctuation density.
5. `scoring.py::combine_signals` turns the two signal scores into one confidence score from 0 to 1.
6. `scoring.py::score_to_label` maps that score to a reader-facing label.
7. The decision is appended to `logs/audit.jsonl`; a writer can use `POST /appeal` to record a challenge and place the item under review.

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:**

How predictable a local GPT-2 language model finds the submitted text. Low perplexity becomes a higher AI score.

**Why that might differ between human and AI writing:**

Generated prose can use more probable next words and patterns, which may make it easier for a language model to predict.

**What it can't see:**

Predictability is not authorship. Plain, concise human writing, including writing by second-language learners, can be incorrectly treated as AI-like; rare or ornate AI writing can go the other direction.

### Signal two — the style signal

**What it measures:**

The shape of the text: sentence-length spread, unique-word ratio, and punctuation density.

**Why that might differ between human and AI writing:**

Human writing can have a more uneven rhythm, vocabulary, and punctuation pattern. Regular sentence lengths and repeated vocabulary raise this signal's AI score.

**What it can't see:**

It cannot understand meaning or authorship. Typos, sentence splitting, quotation, or deliberate formatting can change the measurements without changing who wrote the text.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:**

Both signals produce scores where higher means more AI-like. The service takes their equal-weight average. When they disagree, the average moves toward the unsure range rather than treating either signal as conclusive.

**The numbers:**

Model-signal weight: 0.50. Style-signal weight: 0.50. Human threshold: 0.35 or below. Unsure range: above 0.35 and below 0.65. AI threshold: 0.65 or above.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**

For the sample personal reflection below, the model score was 0.5400 while the style score was 0.3233. Their average was 0.4316, so the service returned the unsure label rather than making a high-confidence authorship claim.



---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00–0.35 | This writing looks more likely to have been written by a person. This is not a final judgment. |
| unsure | >0.35–<0.65 | We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result. |
| high-confidence AI | 0.65–1.00 | This writing shows patterns often associated with AI-generated text. This is not proof of authorship; you may appeal this result. |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->

It says the system lacks confidence rather than implying that the writer did something wrong. It also points directly to the appeal path.

---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```powershell
$body = @{ text = 'I keep a notebook beside the kitchen window. This morning I wrote down the first frost on the grass, a recipe my aunt taught me, and a reminder to call my brother. The notes are small, but they help me notice what I would otherwise forget.'; creator_id = 'sample-writer' } | ConvertTo-Json -Compress
$body | curl.exe --silent -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" --data-binary "@-"
```

```json
{
  "confidence": 0.4316,
  "content_id": "199e6e47-f1ef-4df4-82d7-e371428257c2",
  "guess": "unsure",
  "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
  "model_score": 0.54,
  "style_score": 0.3233
}
```

**An appeal**

```powershell
$body = @{ content_id = '199e6e47-f1ef-4df4-82d7-e371428257c2'; reasoning = 'I wrote this personal observation myself and would like it reviewed.' } | ConvertTo-Json -Compress
$body | curl.exe --silent -X POST http://127.0.0.1:5000/appeal -H "Content-Type: application/json" --data-binary "@-"
```

```json
{
  "content_id": "199e6e47-f1ef-4df4-82d7-e371428257c2",
  "message": "Your appeal was recorded and is now under review.",
  "ok": true,
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": 0.4316,
      "content_id": "199e6e47-f1ef-4df4-82d7-e371428257c2",
      "creator_id": "sample-writer",
      "guess": "unsure",
      "model_score": 0.54,
      "style_score": 0.3233,
      "status": "decided"
    },
    {
      "content_id": "199e6e47-f1ef-4df4-82d7-e371428257c2",
      "event": "appeal",
      "reasoning": "I wrote this personal observation myself and would like it reviewed.",
      "status": "under_review"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:* I asked Codex to diagnose the starter project's setup failures and prepare a compatible local environment.
- *What came back:* It identified that the original virtual environment used Python 3.14, while the pinned packages required Python 3.13; it also identified a Windows path-length issue during PyTorch installation.
- *What I changed:* I used the Python 3.13 environment at a shorter path, installed the pinned dependencies, downloaded the local detector model, and verified the course check passed.

**Moment 2**

- *What I asked for:* I asked Codex to help implement and test the two-signal submission pipeline and appeal endpoint while I wrote my own acceptance criteria.
- *What came back:* It suggested a stylometry implementation, an equal-weight combining rule, input validation, reader-facing labels, and sample requests to test the endpoints.
- *What I changed:* I used the proposed implementation, tested the response and audit-log behavior, and kept the criteria targets and rationales as my own decisions.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
