# Status and limits

Initial portfolio edition and real-data worked examples prepared November 13, 2026.

Four additional skills and their real-data examples added November 14, 2026, using the same frozen sample.

| Component | What has been done | What it does not establish |
| --- | --- | --- |
| Eleven Markdown skills | Written as general research instructions with outputs and review limits | Validated codebooks, reliable labels, or transfer across research contexts |
| Real-interview worked examples | Read all 69 turns of the preselected first interview in each cohort; applied 11 skills across the November 13–14 authoring sessions; checked 37 quoted excerpts and their source provenance | Independent human validation, population estimates, cohort comparisons, or improvement over an unassisted baseline |
| Synthetic worked example | Authored to illustrate different judgments; its quoted evidence is checked against the invented source | A model execution, participant finding, or independent human rating |
| Public-data preparation | Downloaded the pinned Anthropic release, verified all three checksums, prepared all 1,250 interviews, and checked exact turn spans | Semantic analysis of the remaining 1,247 interviews |
| Length outlier screen | Counted words for all 14,495 participant-message slots; computed within-cohort inclusive quartiles and upper-fence flags; retained every case; no selected-case message crosses its cohort fence | Meaning or quality of flagged messages, semantic review of the other interviews, or a validated outlier classifier |
| Evidence verifier | Exercised on synthetic examples, failure cases, and real source excerpts; verifies optional exact quote offsets | Every claim has evidence, or each quote supports the interpretation |
| Automated tests | 18 local code tests passed; CI runs these, source evidence checks, and reproduction of the length diagnostic | Research usefulness, causal validity, privacy guarantees, or model accuracy |

The [data audit](../results/data-audit.json) is the actual aggregate preparation output. The [original walkthrough](../examples/ANTHROPIC_WORKED_EXAMPLE.md) and [four additional examples](../examples/ADVANCED_ANTHROPIC_EXAMPLES.md) contain sample-scoped qualitative interpretations with a [source ledger](../examples/anthropic-evidence.json) and [sample manifest](../examples/anthropic-sample.json). The [length output](../results/response-length-review.json) is a reproducible descriptive screen. No skill-versus-baseline comparisons, independent ratings, population findings, thematic saturation, or token/time savings are claimed.

Next validation step: obtain independent review of the worked interpretations, then choose and freeze a question, scope, task, and review criteria for a baseline-versus-skill comparison. The [run guide](RUN_GUIDE.md) describes that comparison as future work.
