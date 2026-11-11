# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-11 15:18
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 201 | `6bae1361-9e0c-4731-93d0-5dd4af3eeb52` | unsure | 0.351 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 201 | `af1875bc-419f-4205-a1fa-38f5e068dea6` | unsure | 0.399 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 201 | `e99ad991-6eb0-43e2-92fe-58df2bd831f5` | unsure | 0.521 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 201 | `2eb91fbe-d501-4418-9d2a-0244d65fe9be` | unsure | 0.568 |  |
| EV05 | evasion | both signals: heavy human editing pass | 201 | `65d059a1-0ebb-473b-b60e-e01576baca50` | human | 0.281 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 201 | `36622147-606d-4551-8f1c-a82fd673332f` | unsure | 0.405 |  |
| EV07 | evasion | signal two: padding with punctuation | 201 | `8efd9398-1ccd-494b-96b0-cd7170ef98e3` | unsure | 0.596 |  |
| EV08 | evasion | signal one: text below the token window | 201 | `463eaa4c-7c19-41c8-a4f4-67f51b3c5be1` | human | 0.338 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 201 | `f2bf1d80-e61f-44b5-a287-c9719c6fe6e2` | unsure | 0.532 |  |
| EV10 | evasion | signal two: repeated stanza structure | 201 | `33acb72e-08da-4812-a256-2cbac7e13f0b` | ai | 0.807 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 201 | `e277676b-5923-4d2b-b682-3ab18b0bc77a` | unsure | 0.524 |  |
| FP02 | false_positive | human writing in a formal register | 201 | `595f0815-0a17-4641-9ea1-0fecdf2ed6e2` | ai | 0.652 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 201 | `a02b92d7-3606-443d-b2d9-a678824a0c28` | ai | 0.659 |  |
| FP04 | false_positive | a student essay written to a rubric | 201 | `7201a3c9-5664-43c8-8b5e-80f0e27502af` | unsure | 0.641 |  |
| FP05 | false_positive | technical documentation written by a person | 201 | `93b283e5-4371-418c-97d5-e017e6efa609` | ai | 0.692 |  |
| FP06 | false_positive | a person imitating a formal template | 201 | `0bcab55c-4134-4711-8cef-669d814138b2` | unsure | 0.634 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 201 | `5fc1f685-45fc-43cc-b2be-db55a9477fc1` | unsure | 0.621 |  |
| FP08 | false_positive | very short genuine human submission | 201 | `f275584e-106f-4db1-8dea-5debfc22464f` | human | 0.331 |  |
| PI01 | prompt_injection | instruction to ignore the check | 201 | `2393881b-cd1e-45c9-9dce-d742d546de4e` | human | 0.346 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 201 | `82ab6286-0020-4619-8723-3c269da2d47a` | human | 0.207 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 201 | `1f5b6954-93d5-4221-a9a5-153deaff2e92` | unsure | 0.509 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 201 | `6d73d005-9622-4af5-9662-9ea9ba3b6773` | unsure | 0.447 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 201 | `307b055b-da95-4690-a639-90d9f9d1caaa` | unsure | 0.445 |  |
| PI06 | prompt_injection | instruction plus real human text | 201 | `7a158095-d2b8-45b8-8ac9-f20f32a455dc` | unsure | 0.499 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 201 | `c638a431-d6b2-47b4-afb4-a0dd9244b305` | human | 0.300 |  |
| MF04 | malformed | text is only punctuation | 201 | `85a53678-ca22-4da7-99db-727282eac7dc` | unsure | 0.431 |  |
| MF05 | malformed | text is a very long single word | 201 | `3e7dd2e2-75f8-47a3-9cee-9d3ae6540bab` | ai | 0.799 |  |
| MF06 | malformed | text is emoji only | 201 | `742cba85-279d-413b-8937-3ac0c6557eb7` | ai | 0.999 |  |
| MF07 | malformed | text is right-to-left script | 201 | `cb3e45c7-823c-4aac-812a-f0fe01efb91c` | ai | 0.953 |  |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 201 | `73dfa6ee-41ae-4873-ae90-4170a07aa02a` | unsure | 0.420 |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 201 | `da99a31c-9227-404a-ab4f-71fb477dccab` | human | 0.325 |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 201 | `2d6e6db5-55f1-4336-b000-126e9eed4f53` | human | 0.314 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 201 | `64d9391d-8288-4ee2-b90d-d054023baea0` | human | 0.314 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 201 | `118ee7cc-092a-4969-9c70-dce1d30583b6` | human | 0.314 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 201 | `d11a6bec-37aa-4c19-bb02-92740cdeabba` | human | 0.314 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 201 | `3dc14e17-d8aa-4efc-8f13-a1d6a6e390d0` | human | 0.314 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 201 | `f17e5e5e-9725-4924-bf46-fc6eec4e5048` | human | 0.314 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 201 | `729b60b6-37c8-4ed1-99ef-cebb53566c04` | human | 0.314 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 201 | `83d2b611-9e45-4daf-94df-179b4bd07853` | human | 0.314 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 201,
  "content_id": "6bae1361-9e0c-4731-93d0-5dd4af3eeb52",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.3507,
  "model_score": 0.1635,
  "style_score": 0.5379,
  "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 201,
  "content_id": "af1875bc-419f-4205-a1fa-38f5e068dea6",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.3992,
  "model_score": 0.5943,
  "style_score": 0.2041,
  "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 201,
  "content_id": "e99ad991-6eb0-43e2-92fe-58df2bd831f5",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.521,
  "model_score": 0.6662,
  "style_score": 0.3758,
  "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 201,
  "content_id": "2eb91fbe-d501-4418-9d2a-0244d65fe9be",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5682,
  "model_score": 0.6114,
  "style_score": 0.525,
  "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 201,
  "content_id": "65d059a1-0ebb-473b-b60e-e01576baca50",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.2813,
  "model_score": 0.3212,
  "style_score": 0.2415,
  "label": "This writing looks more likely to have been written by a person. This is not a final judgment.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 201,
  "content_id": "36622147-606d-4551-8f1c-a82fd673332f",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4045,
  "model_score": 0.5727,
  "style_score": 0.2363,
  "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 201,
  "content_id": "8efd9398-1ccd-494b-96b0-cd7170ef98e3",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5963,
  "model_score": 0.5862,
  "style_score": 0.6064,
  "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 201,
  "content_id": "463eaa4c-7c19-41c8-a4f4-67f51b3c5be1",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.3377,
  "model_score": 0.2452,
  "style_score": 0.4303,
  "label": "This writing looks more likely to have been written by a person. This is not a final judgment.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 201,
  "content_id": "f2bf1d80-e61f-44b5-a287-c9719c6fe6e2",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5317,
  "model_score": 0.7042,
  "style_score": 0.3592,
  "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 201,
  "content_id": "33acb72e-08da-4812-a256-2cbac7e13f0b",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8074,
  "model_score": 0.9792,
  "style_score": 0.6355,
  "label": "This writing shows patterns often associated with AI-generated text. This is not proof of authorship; you may appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 201,
  "content_id": "e277676b-5923-4d2b-b682-3ab18b0bc77a",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5238,
  "model_score": 0.6175,
  "style_score": 0.4301,
  "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 201,
  "content_id": "595f0815-0a17-4641-9ea1-0fecdf2ed6e2",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.6521,
  "model_score": 0.7387,
  "style_score": 0.5654,
  "label": "This writing shows patterns often associated with AI-generated text. This is not proof of authorship; you may appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 201,
  "content_id": "a02b92d7-3606-443d-b2d9-a678824a0c28",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.6595,
  "model_score": 0.8051,
  "style_score": 0.5139,
  "label": "This writing shows patterns often associated with AI-generated text. This is not proof of authorship; you may appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 201,
  "content_id": "7201a3c9-5664-43c8-8b5e-80f0e27502af",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.6413,
  "model_score": 0.8329,
  "style_score": 0.4498,
  "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 201,
  "content_id": "93b283e5-4371-418c-97d5-e017e6efa609",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.6923,
  "model_score": 0.8005,
  "style_score": 0.5841,
  "label": "This writing shows patterns often associated with AI-generated text. This is not proof of authorship; you may appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 201,
  "content_id": "0bcab55c-4134-4711-8cef-669d814138b2",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.6338,
  "model_score": 0.8814,
  "style_score": 0.3861,
  "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 201,
  "content_id": "5fc1f685-45fc-43cc-b2be-db55a9477fc1",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.621,
  "model_score": 0.8816,
  "style_score": 0.3604,
  "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 201,
  "content_id": "f275584e-106f-4db1-8dea-5debfc22464f",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.3312,
  "model_score": 0.3223,
  "style_score": 0.3402,
  "label": "This writing looks more likely to have been written by a person. This is not a final judgment.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 201,
  "content_id": "2393881b-cd1e-45c9-9dce-d742d546de4e",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.3458,
  "model_score": 0.4625,
  "style_score": 0.2291,
  "label": "This writing looks more likely to have been written by a person. This is not a final judgment.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 201,
  "content_id": "82ab6286-0020-4619-8723-3c269da2d47a",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.2066,
  "model_score": 0.2044,
  "style_score": 0.2088,
  "label": "This writing looks more likely to have been written by a person. This is not a final judgment.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 201,
  "content_id": "1f5b6954-93d5-4221-a9a5-153deaff2e92",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5086,
  "model_score": 0.5943,
  "style_score": 0.4228,
  "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 201,
  "content_id": "6d73d005-9622-4af5-9662-9ea9ba3b6773",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4474,
  "model_score": 0.4998,
  "style_score": 0.395,
  "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 201,
  "content_id": "307b055b-da95-4690-a639-90d9f9d1caaa",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.445,
  "model_score": 0.6401,
  "style_score": 0.2498,
  "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 201,
  "content_id": "7a158095-d2b8-45b8-8ac9-f20f32a455dc",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.4987,
  "model_score": 0.5583,
  "style_score": 0.4391,
  "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 201,
  "content_id": "c638a431-d6b2-47b4-afb4-a0dd9244b305",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.3,
  "model_score": 0.0,
  "style_score": 0.6,
  "label": "This writing looks more likely to have been written by a person. This is not a final judgment.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 201,
  "content_id": "85a53678-ca22-4da7-99db-727282eac7dc",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.4306,
  "model_score": 0.0112,
  "style_score": 0.85,
  "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 201,
  "content_id": "3e7dd2e2-75f8-47a3-9cee-9d3ae6540bab",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.7988,
  "model_score": 0.9976,
  "style_score": 0.6,
  "label": "This writing shows patterns often associated with AI-generated text. This is not proof of authorship; you may appeal this result.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 201,
  "content_id": "742cba85-279d-413b-8937-3ac0c6557eb7",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.9985,
  "model_score": 0.9969,
  "style_score": 1.0,
  "label": "This writing shows patterns often associated with AI-generated text. This is not proof of authorship; you may appeal this result.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 201,
  "content_id": "cb3e45c7-823c-4aac-812a-f0fe01efb91c",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.9532,
  "model_score": 0.9064,
  "style_score": 1.0,
  "label": "This writing shows patterns often associated with AI-generated text. This is not proof of authorship; you may appeal this result.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 201,
  "content_id": "73dfa6ee-41ae-4873-ae90-4170a07aa02a",
  "creator_id": null,
  "guess": "unsure",
  "confidence": 0.4197,
  "model_score": 0.2395,
  "style_score": 0.6,
  "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 201,
  "content_id": "da99a31c-9227-404a-ab4f-71fb477dccab",
  "creator_id": {
    "id": "x"
  },
  "guess": "human",
  "confidence": 0.3246,
  "model_score": 0.0492,
  "style_score": 0.6,
  "label": "This writing looks more likely to have been written by a person. This is not a final judgment.",
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 201,
  "content_id": "2d6e6db5-55f1-4336-b000-126e9eed4f53",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3143,
  "model_score": 0.0287,
  "style_score": 0.6,
  "label": "This writing looks more likely to have been written by a person. This is not a final judgment.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 201,
  "content_id": "64d9391d-8288-4ee2-b90d-d054023baea0",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3143,
  "model_score": 0.0287,
  "style_score": 0.6,
  "label": "This writing looks more likely to have been written by a person. This is not a final judgment.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 201,
  "content_id": "118ee7cc-092a-4969-9c70-dce1d30583b6",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3143,
  "model_score": 0.0287,
  "style_score": 0.6,
  "label": "This writing looks more likely to have been written by a person. This is not a final judgment.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 201,
  "content_id": "d11a6bec-37aa-4c19-bb02-92740cdeabba",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3143,
  "model_score": 0.0287,
  "style_score": 0.6,
  "label": "This writing looks more likely to have been written by a person. This is not a final judgment.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 201,
  "content_id": "3dc14e17-d8aa-4efc-8f13-a1d6a6e390d0",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3143,
  "model_score": 0.0287,
  "style_score": 0.6,
  "label": "This writing looks more likely to have been written by a person. This is not a final judgment.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 201,
  "content_id": "f17e5e5e-9725-4924-bf46-fc6eec4e5048",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3143,
  "model_score": 0.0287,
  "style_score": 0.6,
  "label": "This writing looks more likely to have been written by a person. This is not a final judgment.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 201,
  "content_id": "729b60b6-37c8-4ed1-99ef-cebb53566c04",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3143,
  "model_score": 0.0287,
  "style_score": 0.6,
  "label": "This writing looks more likely to have been written by a person. This is not a final judgment.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 201,
  "content_id": "83d2b611-9e45-4daf-94df-179b4bd07853",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3143,
  "model_score": 0.0287,
  "style_score": 0.6,
  "label": "This writing looks more likely to have been written by a person. This is not a final judgment.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
