# Status and limits

Initial portfolio edition and real-data worked examples prepared November 13, 2026.

| Component | What has been done | What it does not establish |
| --- | --- | --- |
| Seven Markdown skills | Written as general research instructions with outputs and review limits | Validated codebooks, reliable labels, or transfer across research contexts |
| Real-interview worked examples | Read all 69 turns of the preselected first interview in each cohort; applied all seven skills in one AI-assisted authoring session; checked 26 quoted excerpts and their source provenance | Independent human validation, population estimates, cohort comparisons, or improvement over an unassisted baseline |
| Synthetic worked example | Authored to illustrate different judgments; its quoted evidence is checked against the invented source | A model execution, participant finding, or independent human rating |
| Public-data preparation | Downloaded the pinned Anthropic release, verified all three checksums, prepared all 1,250 interviews, and checked exact turn spans | Semantic analysis of the remaining 1,247 interviews |
| Evidence verifier | Exercised on synthetic examples, failure cases, and real source excerpts; verifies optional exact quote offsets | Every claim has evidence, or each quote supports the interpretation |
| Automated tests | 14 local code tests passed; CI runs these and a separate public-source example check | Research usefulness, causal validity, privacy guarantees, or model accuracy |

The [data audit](../results/data-audit.json) is the actual aggregate preparation output. The [real worked analysis](../examples/ANTHROPIC_WORKED_EXAMPLE.md) contains sample-scoped qualitative interpretations with a [source ledger](../examples/anthropic-evidence.json) and [sample manifest](../examples/anthropic-sample.json). No skill-versus-baseline comparisons, independent ratings, population findings, or token/time savings are claimed.

Next validation step: obtain independent review of the worked interpretations, then choose and freeze a question, scope, task, and review criteria for a baseline-versus-skill comparison. The [run guide](RUN_GUIDE.md) describes that comparison as future work.
