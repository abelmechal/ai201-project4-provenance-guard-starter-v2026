# Attack run — after

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
| EV01 | evasion | signal two: typos raise word variety | 201 | `0debecbb-891a-456d-bb08-23e81b0c1593` | unsure | 0.351 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 201 | `5c88e7f8-3f1e-4113-91f7-e3150f363cf0` | unsure | 0.399 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 201 | `72fe61d8-d6a8-47d3-8725-533c5c3dad09` | unsure | 0.521 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 201 | `7df54ece-2145-488e-a850-074c64f4a0be` | unsure | 0.568 |  |
| EV05 | evasion | both signals: heavy human editing pass | 201 | `b87345e6-0e7d-4e00-a359-3cbed6da1a2d` | human | 0.281 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 201 | `08c3ec09-6eed-4582-b370-3142926c3dfb` | unsure | 0.405 |  |
| EV07 | evasion | signal two: padding with punctuation | 201 | `71c1e0bc-eed9-470e-b43a-e58e005d05e7` | unsure | 0.596 |  |
| EV08 | evasion | signal one: text below the token window | 201 | `4e364329-fa5d-49d7-bb86-18dead337729` | human | 0.338 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 201 | `c044c1f6-66f9-426b-9909-c2ffae836e51` | unsure | 0.532 |  |
| EV10 | evasion | signal two: repeated stanza structure | 201 | `d9267be0-b7be-42d1-b4c5-4b080a74b4a5` | ai | 0.807 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 201 | `f04858ed-4a6f-4d07-9a7f-8a6b0c24e1d2` | unsure | 0.524 |  |
| FP02 | false_positive | human writing in a formal register | 201 | `9203c952-fb8a-4b04-bddd-a24781812fde` | unsure | 0.652 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 201 | `69425b84-7255-4396-98be-1566e2f1d839` | unsure | 0.659 |  |
| FP04 | false_positive | a student essay written to a rubric | 201 | `2df5500c-da17-4125-9fa6-bf3ad8fb1fc9` | unsure | 0.641 |  |
| FP05 | false_positive | technical documentation written by a person | 201 | `7c8b81ae-3a26-40f5-a2d9-e4005706b57a` | unsure | 0.692 |  |
| FP06 | false_positive | a person imitating a formal template | 201 | `eb0ad0c2-0143-4f4b-b223-708ad067d4e0` | unsure | 0.634 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 201 | `d165bb6a-9941-4442-aefc-69a579625b28` | unsure | 0.621 |  |
| FP08 | false_positive | very short genuine human submission | 201 | `c3bac796-5ccc-4c8e-8750-23a755bc5d0b` | human | 0.331 |  |
| PI01 | prompt_injection | instruction to ignore the check | 201 | `8d369a7b-08d2-4bcc-bba2-4c8365f249b2` | human | 0.346 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 201 | `cf957829-4b9e-445c-8047-5115b4e9e596` | human | 0.207 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 201 | `b7534d97-6e33-48c8-8760-1a59c051898a` | unsure | 0.509 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 201 | `d91518c4-a4b2-4c44-bf88-df1abc09e375` | unsure | 0.447 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 201 | `989ebbe8-68c4-4164-9283-d9e1034e9bbe` | unsure | 0.445 |  |
| PI06 | prompt_injection | instruction plus real human text | 201 | `c5e1e982-b5c7-4fa7-b81c-a4ec7e945b7e` | unsure | 0.499 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 201 | `b67a1913-1ebd-4f52-a2d4-7e252638f812` | human | 0.300 |  |
| MF04 | malformed | text is only punctuation | 201 | `1fca937e-1d12-45c5-9d55-c8816af196c4` | unsure | 0.431 |  |
| MF05 | malformed | text is a very long single word | 201 | `dae1b36e-70d9-418b-8ee7-42d823de2265` | ai | 0.799 |  |
| MF06 | malformed | text is emoji only | 201 | `b280e3a5-a301-4be1-9e56-457f156fe1bf` | ai | 0.999 |  |
| MF07 | malformed | text is right-to-left script | 201 | `9cad8345-d560-4fe4-83c9-34c1c6f2a308` | ai | 0.953 |  |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 201 | `5722a0aa-b833-428e-8d0e-afe096440a76` | unsure | 0.420 |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 201 | `f1506a61-c194-4451-a0ab-b192675600b6` | human | 0.325 |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 201 | `4e077f7b-610a-45af-a3a2-399792e576a6` | human | 0.314 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 201 | `cba479e1-a3ab-41b6-81cd-5a0da9342851` | human | 0.314 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 201 | `2e2aca65-d91a-4d4f-9679-9fea108fb01c` | human | 0.314 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 201 | `c5931942-7904-4bb0-b3af-17127b6a19d8` | human | 0.314 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 201 | `5f4e19ad-58b3-451b-a257-76233f14c0b1` | human | 0.314 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 201 | `dd57a7d4-475b-45e4-b757-4d933cbbaee2` | human | 0.314 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 201 | `2294ce3b-bcb4-486e-bc30-493643081d0e` | human | 0.314 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 201 | `5fdc545d-7c98-4e58-8b31-ede09288d403` | human | 0.314 |  |
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
  "content_id": "0debecbb-891a-456d-bb08-23e81b0c1593",
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
  "content_id": "5c88e7f8-3f1e-4113-91f7-e3150f363cf0",
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
  "content_id": "72fe61d8-d6a8-47d3-8725-533c5c3dad09",
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
  "content_id": "7df54ece-2145-488e-a850-074c64f4a0be",
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
  "content_id": "b87345e6-0e7d-4e00-a359-3cbed6da1a2d",
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
  "content_id": "08c3ec09-6eed-4582-b370-3142926c3dfb",
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
  "content_id": "71c1e0bc-eed9-470e-b43a-e58e005d05e7",
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
  "content_id": "4e364329-fa5d-49d7-bb86-18dead337729",
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
  "content_id": "c044c1f6-66f9-426b-9909-c2ffae836e51",
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
  "content_id": "d9267be0-b7be-42d1-b4c5-4b080a74b4a5",
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
  "content_id": "f04858ed-4a6f-4d07-9a7f-8a6b0c24e1d2",
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
  "content_id": "9203c952-fb8a-4b04-bddd-a24781812fde",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.6521,
  "model_score": 0.7387,
  "style_score": 0.5654,
  "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
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
  "content_id": "69425b84-7255-4396-98be-1566e2f1d839",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.6595,
  "model_score": 0.8051,
  "style_score": 0.5139,
  "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
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
  "content_id": "2df5500c-da17-4125-9fa6-bf3ad8fb1fc9",
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
  "content_id": "7c8b81ae-3a26-40f5-a2d9-e4005706b57a",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.6923,
  "model_score": 0.8005,
  "style_score": 0.5841,
  "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
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
  "content_id": "eb0ad0c2-0143-4f4b-b223-708ad067d4e0",
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
  "content_id": "d165bb6a-9941-4442-aefc-69a579625b28",
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
  "content_id": "c3bac796-5ccc-4c8e-8750-23a755bc5d0b",
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
  "content_id": "8d369a7b-08d2-4bcc-bba2-4c8365f249b2",
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
  "content_id": "cf957829-4b9e-445c-8047-5115b4e9e596",
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
  "content_id": "b7534d97-6e33-48c8-8760-1a59c051898a",
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
  "content_id": "d91518c4-a4b2-4c44-bf88-df1abc09e375",
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
  "content_id": "989ebbe8-68c4-4164-9283-d9e1034e9bbe",
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
  "content_id": "c5e1e982-b5c7-4fa7-b81c-a4ec7e945b7e",
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
  "content_id": "b67a1913-1ebd-4f52-a2d4-7e252638f812",
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
  "content_id": "1fca937e-1d12-45c5-9d55-c8816af196c4",
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
  "content_id": "dae1b36e-70d9-418b-8ee7-42d823de2265",
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
  "content_id": "b280e3a5-a301-4be1-9e56-457f156fe1bf",
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
  "content_id": "9cad8345-d560-4fe4-83c9-34c1c6f2a308",
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
  "content_id": "5722a0aa-b833-428e-8d0e-afe096440a76",
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
  "content_id": "f1506a61-c194-4451-a0ab-b192675600b6",
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
  "content_id": "4e077f7b-610a-45af-a3a2-399792e576a6",
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
  "content_id": "cba479e1-a3ab-41b6-81cd-5a0da9342851",
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
  "content_id": "2e2aca65-d91a-4d4f-9679-9fea108fb01c",
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
  "content_id": "c5931942-7904-4bb0-b3af-17127b6a19d8",
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
  "content_id": "5f4e19ad-58b3-451b-a257-76233f14c0b1",
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
  "content_id": "dd57a7d4-475b-45e4-b757-4d933cbbaee2",
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
  "content_id": "2294ce3b-bcb4-486e-bc30-493643081d0e",
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
  "content_id": "5fdc545d-7c98-4e58-8b31-ede09288d403",
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
