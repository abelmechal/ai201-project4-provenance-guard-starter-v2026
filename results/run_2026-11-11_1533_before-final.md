# Run log — before-final

- Produced by: `run_eval.py::main`
- Service: `app.py::submit` · scoring: `scoring.py::combine_signals`
- 3 trials per criterion · 2026-11-11 15:33

Fill in Target from `criteria.md`, and Run and Verdict from the output
underneath. Whether a trial passed depends on the criterion you wrote.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. my own writing |  |   |   |   |  |
| 2. label coverage |  |   |   |   |  |
| 3. appeal setup |  |   |   |   |  |
| 4. bad input and recovery |  |   |   |   |  |
| 5. score separation |  |   |   |   |  |

---

## What actually came back

Real output. Paste the relevant parts into your README — the rubric
asks for the actual JSON, not a description of it.

### my own writing

**Trial 1**

```json
[
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4653,
    "model_score": 0.4779,
    "style_score": 0.4527,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Setting up a dual-monitor workstation requires more attention to ergon"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.3848,
    "model_score": 0.2876,
    "style_score": 0.4819,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "A quiet Sunday afternoon provides the ideal atmosphere to reorganize a"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4177,
    "model_score": 0.4463,
    "style_score": 0.3891,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Arrival stands out as one of the most compelling science fiction films"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.5625,
    "model_score": 0.617,
    "style_score": 0.5081,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Taking a brisk walk through the neighborhood during the transition bet"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4859,
    "model_score": 0.4719,
    "style_score": 0.5,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Making a reliable pour-over coffee comes down to thermal control and s"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4214,
    "model_score": 0.3645,
    "style_score": 0.4782,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "The debate between physical books and e-readers often reduces to a fal"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.3932,
    "model_score": 0.3378,
    "style_score": 0.4486,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Early morning light rail commutes carry a distinctive, rhythmic ambian"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.3699,
    "model_score": 0.3239,
    "style_score": 0.4159,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Visiting a neighborhood diner early on a weekday morning is a lesson i"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4456,
    "model_score": 0.4459,
    "style_score": 0.4452,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Learning to care for a collection of houseplants is essentially an exe"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.3889,
    "model_score": 0.2794,
    "style_score": 0.4984,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Keeping a dedicated, written notebook for active projects remains far "
  }
]
```

**Trial 2**

```json
[
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4653,
    "model_score": 0.4779,
    "style_score": 0.4527,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Setting up a dual-monitor workstation requires more attention to ergon"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.3848,
    "model_score": 0.2876,
    "style_score": 0.4819,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "A quiet Sunday afternoon provides the ideal atmosphere to reorganize a"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4177,
    "model_score": 0.4463,
    "style_score": 0.3891,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Arrival stands out as one of the most compelling science fiction films"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.5625,
    "model_score": 0.617,
    "style_score": 0.5081,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Taking a brisk walk through the neighborhood during the transition bet"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4859,
    "model_score": 0.4719,
    "style_score": 0.5,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Making a reliable pour-over coffee comes down to thermal control and s"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4214,
    "model_score": 0.3645,
    "style_score": 0.4782,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "The debate between physical books and e-readers often reduces to a fal"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.3932,
    "model_score": 0.3378,
    "style_score": 0.4486,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Early morning light rail commutes carry a distinctive, rhythmic ambian"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.3699,
    "model_score": 0.3239,
    "style_score": 0.4159,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Visiting a neighborhood diner early on a weekday morning is a lesson i"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4456,
    "model_score": 0.4459,
    "style_score": 0.4452,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Learning to care for a collection of houseplants is essentially an exe"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.3889,
    "model_score": 0.2794,
    "style_score": 0.4984,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Keeping a dedicated, written notebook for active projects remains far "
  }
]
```

**Trial 3**

```json
[
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4653,
    "model_score": 0.4779,
    "style_score": 0.4527,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Setting up a dual-monitor workstation requires more attention to ergon"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.3848,
    "model_score": 0.2876,
    "style_score": 0.4819,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "A quiet Sunday afternoon provides the ideal atmosphere to reorganize a"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4177,
    "model_score": 0.4463,
    "style_score": 0.3891,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Arrival stands out as one of the most compelling science fiction films"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.5625,
    "model_score": 0.617,
    "style_score": 0.5081,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Taking a brisk walk through the neighborhood during the transition bet"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4859,
    "model_score": 0.4719,
    "style_score": 0.5,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Making a reliable pour-over coffee comes down to thermal control and s"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4214,
    "model_score": 0.3645,
    "style_score": 0.4782,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "The debate between physical books and e-readers often reduces to a fal"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.3932,
    "model_score": 0.3378,
    "style_score": 0.4486,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Early morning light rail commutes carry a distinctive, rhythmic ambian"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.3699,
    "model_score": 0.3239,
    "style_score": 0.4159,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Visiting a neighborhood diner early on a weekday morning is a lesson i"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4456,
    "model_score": 0.4459,
    "style_score": 0.4452,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Learning to care for a collection of houseplants is essentially an exe"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.3889,
    "model_score": 0.2794,
    "style_score": 0.4984,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Keeping a dedicated, written notebook for active projects remains far "
  }
]
```

### label coverage

**Trial 1**

```json
[
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.5625,
    "model_score": 0.617,
    "style_score": 0.5081,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Taking a brisk walk through the neighborhood during the transition bet"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.3699,
    "model_score": 0.3239,
    "style_score": 0.4159,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Visiting a neighborhood diner early on a weekday morning is a lesson i"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4401,
    "model_score": 0.4269,
    "style_score": 0.4533,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Setting up a dual-monitor workstation requires more attention to ergon"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4355,
    "model_score": 0.4383,
    "style_score": 0.4326,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Making a reliable pour-over coffee comes down to thermal control and s"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4225,
    "model_score": 0.302,
    "style_score": 0.543,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Artificial intelligence can support modern organizations by automating"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4164,
    "model_score": 0.4159,
    "style_score": 0.417,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Effective project planning follows a predictable sequence. First, defi"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.5625,
    "model_score": 0.617,
    "style_score": 0.5081,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Taking a brisk walk through the neighborhood during the transition bet"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.3699,
    "model_score": 0.3239,
    "style_score": 0.4159,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Visiting a neighborhood diner early on a weekday morning is a lesson i"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4401,
    "model_score": 0.4269,
    "style_score": 0.4533,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Setting up a dual-monitor workstation requires more attention to ergon"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4355,
    "model_score": 0.4383,
    "style_score": 0.4326,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Making a reliable pour-over coffee comes down to thermal control and s"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4225,
    "model_score": 0.302,
    "style_score": 0.543,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Artificial intelligence can support modern organizations by automating"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4164,
    "model_score": 0.4159,
    "style_score": 0.417,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Effective project planning follows a predictable sequence. First, defi"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.5625,
    "model_score": 0.617,
    "style_score": 0.5081,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Taking a brisk walk through the neighborhood during the transition bet"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.3699,
    "model_score": 0.3239,
    "style_score": 0.4159,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Visiting a neighborhood diner early on a weekday morning is a lesson i"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4401,
    "model_score": 0.4269,
    "style_score": 0.4533,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Setting up a dual-monitor workstation requires more attention to ergon"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4355,
    "model_score": 0.4383,
    "style_score": 0.4326,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Making a reliable pour-over coffee comes down to thermal control and s"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4225,
    "model_score": 0.302,
    "style_score": 0.543,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Artificial intelligence can support modern organizations by automating"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4164,
    "model_score": 0.4159,
    "style_score": 0.417,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Effective project planning follows a predictable sequence. First, defi"
  }
]
```

### appeal setup

**Trial 1**

```json
[
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4225,
    "model_score": 0.302,
    "style_score": 0.543,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Artificial intelligence can support modern organizations by automating"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4401,
    "model_score": 0.4269,
    "style_score": 0.4533,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Setting up a dual-monitor workstation requires more attention to ergon"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4225,
    "model_score": 0.302,
    "style_score": 0.543,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Artificial intelligence can support modern organizations by automating"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4401,
    "model_score": 0.4269,
    "style_score": 0.4533,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Setting up a dual-monitor workstation requires more attention to ergon"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4225,
    "model_score": 0.302,
    "style_score": 0.543,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Artificial intelligence can support modern organizations by automating"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4401,
    "model_score": 0.4269,
    "style_score": 0.4533,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Setting up a dual-monitor workstation requires more attention to ergon"
  }
]
```

### bad input and recovery

**Trial 1**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_bad_missing\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "A request with no creator identifier."
  },
  {
    "status": 201,
    "guess": "human",
    "confidence": 0.3028,
    "model_score": 0.0056,
    "style_score": 0.6,
    "label": "This writing looks more likely to have been written by a person. This is not a final judgment.",
    "sent": "{\"text\": \"A request with the creator identifier omitted.\"}"
  },
  {
    "status": 413,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "word word word word word word word word word word word word word word "
  },
  {
    "status": 201,
    "guess": "human",
    "confidence": 0.3001,
    "model_score": 0.0003,
    "style_score": 0.6,
    "label": "This writing looks more likely to have been written by a person. This is not a final judgment.",
    "sent": "A short valid recovery submission after rejected input."
  }
]
```

**Trial 2**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_bad_missing\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "A request with no creator identifier."
  },
  {
    "status": 201,
    "guess": "human",
    "confidence": 0.3028,
    "model_score": 0.0056,
    "style_score": 0.6,
    "label": "This writing looks more likely to have been written by a person. This is not a final judgment.",
    "sent": "{\"text\": \"A request with the creator identifier omitted.\"}"
  },
  {
    "status": 413,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "word word word word word word word word word word word word word word "
  },
  {
    "status": 201,
    "guess": "human",
    "confidence": 0.3001,
    "model_score": 0.0003,
    "style_score": 0.6,
    "label": "This writing looks more likely to have been written by a person. This is not a final judgment.",
    "sent": "A short valid recovery submission after rejected input."
  }
]
```

**Trial 3**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_bad_missing\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "A request with no creator identifier."
  },
  {
    "status": 201,
    "guess": "human",
    "confidence": 0.3028,
    "model_score": 0.0056,
    "style_score": 0.6,
    "label": "This writing looks more likely to have been written by a person. This is not a final judgment.",
    "sent": "{\"text\": \"A request with the creator identifier omitted.\"}"
  },
  {
    "status": 413,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "word word word word word word word word word word word word word word "
  },
  {
    "status": 201,
    "guess": "human",
    "confidence": 0.3001,
    "model_score": 0.0003,
    "style_score": 0.6,
    "label": "This writing looks more likely to have been written by a person. This is not a final judgment.",
    "sent": "A short valid recovery submission after rejected input."
  }
]
```

### score separation

**Trial 1**

```json
[
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4653,
    "model_score": 0.4779,
    "style_score": 0.4527,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Setting up a dual-monitor workstation requires more attention to ergon"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.3848,
    "model_score": 0.2876,
    "style_score": 0.4819,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "A quiet Sunday afternoon provides the ideal atmosphere to reorganize a"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4177,
    "model_score": 0.4463,
    "style_score": 0.3891,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Arrival stands out as one of the most compelling science fiction films"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.5625,
    "model_score": 0.617,
    "style_score": 0.5081,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Taking a brisk walk through the neighborhood during the transition bet"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4859,
    "model_score": 0.4719,
    "style_score": 0.5,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Making a reliable pour-over coffee comes down to thermal control and s"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4225,
    "model_score": 0.302,
    "style_score": 0.543,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Artificial intelligence can support modern organizations by automating"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4164,
    "model_score": 0.4159,
    "style_score": 0.417,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Effective project planning follows a predictable sequence. First, defi"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.3932,
    "model_score": 0.4144,
    "style_score": 0.3721,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Climate resilience requires communities to combine practical preparati"
  },
  {
    "status": 201,
    "guess": "human",
    "confidence": 0.3295,
    "model_score": 0.3268,
    "style_score": 0.3321,
    "label": "This writing looks more likely to have been written by a person. This is not a final judgment.",
    "sent": "A strong learning routine balances focused practice, feedback, and res"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4505,
    "model_score": 0.4895,
    "style_score": 0.4115,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Good customer service depends on clarity, empathy, and follow-through."
  }
]
```

**Trial 2**

```json
[
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4653,
    "model_score": 0.4779,
    "style_score": 0.4527,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Setting up a dual-monitor workstation requires more attention to ergon"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.3848,
    "model_score": 0.2876,
    "style_score": 0.4819,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "A quiet Sunday afternoon provides the ideal atmosphere to reorganize a"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4177,
    "model_score": 0.4463,
    "style_score": 0.3891,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Arrival stands out as one of the most compelling science fiction films"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.5625,
    "model_score": 0.617,
    "style_score": 0.5081,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Taking a brisk walk through the neighborhood during the transition bet"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4859,
    "model_score": 0.4719,
    "style_score": 0.5,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Making a reliable pour-over coffee comes down to thermal control and s"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4225,
    "model_score": 0.302,
    "style_score": 0.543,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Artificial intelligence can support modern organizations by automating"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4164,
    "model_score": 0.4159,
    "style_score": 0.417,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Effective project planning follows a predictable sequence. First, defi"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.3932,
    "model_score": 0.4144,
    "style_score": 0.3721,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Climate resilience requires communities to combine practical preparati"
  },
  {
    "status": 201,
    "guess": "human",
    "confidence": 0.3295,
    "model_score": 0.3268,
    "style_score": 0.3321,
    "label": "This writing looks more likely to have been written by a person. This is not a final judgment.",
    "sent": "A strong learning routine balances focused practice, feedback, and res"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4505,
    "model_score": 0.4895,
    "style_score": 0.4115,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Good customer service depends on clarity, empathy, and follow-through."
  }
]
```

**Trial 3**

```json
[
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4653,
    "model_score": 0.4779,
    "style_score": 0.4527,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Setting up a dual-monitor workstation requires more attention to ergon"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.3848,
    "model_score": 0.2876,
    "style_score": 0.4819,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "A quiet Sunday afternoon provides the ideal atmosphere to reorganize a"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4177,
    "model_score": 0.4463,
    "style_score": 0.3891,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Arrival stands out as one of the most compelling science fiction films"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.5625,
    "model_score": 0.617,
    "style_score": 0.5081,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Taking a brisk walk through the neighborhood during the transition bet"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4859,
    "model_score": 0.4719,
    "style_score": 0.5,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Making a reliable pour-over coffee comes down to thermal control and s"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4225,
    "model_score": 0.302,
    "style_score": 0.543,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Artificial intelligence can support modern organizations by automating"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4164,
    "model_score": 0.4159,
    "style_score": 0.417,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Effective project planning follows a predictable sequence. First, defi"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.3932,
    "model_score": 0.4144,
    "style_score": 0.3721,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Climate resilience requires communities to combine practical preparati"
  },
  {
    "status": 201,
    "guess": "human",
    "confidence": 0.3295,
    "model_score": 0.3268,
    "style_score": 0.3321,
    "label": "This writing looks more likely to have been written by a person. This is not a final judgment.",
    "sent": "A strong learning routine balances focused practice, feedback, and res"
  },
  {
    "status": 201,
    "guess": "unsure",
    "confidence": 0.4505,
    "model_score": 0.4895,
    "style_score": 0.4115,
    "label": "We cannot confidently determine how this writing was created. No action is needed, and you may appeal this result.",
    "sent": "Good customer service depends on clarity, empathy, and follow-through."
  }
]
```
