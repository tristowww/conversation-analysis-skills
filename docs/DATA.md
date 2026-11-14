# Public data and attribution

Source: [Anthropic Interviewer](https://huggingface.co/datasets/Anthropic/AnthropicInterviewer), associated with [Introducing Anthropic Interviewer: What 1,250 professionals told us about working with AI](https://www.anthropic.com/research/anthropic-interviewer), December 4, 2025.

Attribution: Kunal Handa, Michael Stern, Saffron Huang, Jerry Hong, Esin Durmus, Miles McCain, Grace Yun, AJ Alt, Thomas Millar, Alex Tamkin, Jane Leibrock, Stuart Ritchie, and Deep Ganguli (2025).

The publisher describes 1,000 general-workforce interviews, 125 creative-professional interviews, and 125 scientist interviews, released with participant consent. This convenience research sample does not establish workforce prevalence or demographic representativeness.

## Version and license

The download code pins revision `c9e1ec1e6b093712b9c42235c7303ece647490e9` and verifies the three source-file SHA-256 hashes. The committed aggregate audit records the URLs, hashes, and file sizes.

The dataset card's license section specifies **CC-BY for data and MIT for code**. Its generic metadata header says MIT. This project follows the specific data statement; the card does not specify a CC-BY version, so none is assigned here. The source dataset's license does not automatically license this project's independently authored code or instructions.

Changes in this project: decode CSV records, recognize explicit speaker labels, preserve transcript text and hashes, add turn IDs and character offsets, and count corpus-level structural properties. The preparation code assigns no qualitative labels. The separately authored worked analyses apply 11 skills to three complete interviews and publish selected verbatim excerpts with new AI-assisted interpretations. A declared numerical screen also counts participant-message words and computes within-cohort quartiles and review flags, without dropping cases. These judgments and flags do not belong to Anthropic and imply no publisher endorsement.

## Local handling

Raw CSVs and full exact-text prepared packages stay in ignored `.local-data/` paths. Local working records stay in `.local-runs/`. The public release includes aggregate preparation and length diagnostics, a three-interview sample manifest, and 37 selected source excerpts in `examples/anthropic-evidence.json`. Public source-record IDs, turn locators, offsets, and transcript hashes make these excerpts reproducible. The examples omit participant names, contact details, and the full interviews. Length output identifies only the three already selected source records; no identities or transcript text are published for corpus-wide flags. Public availability is not a reason to infer identities or profile individual participants.

The [original worked analysis](../examples/ANTHROPIC_WORKED_EXAMPLE.md) and [four additional examples](../examples/ADVANCED_ANTHROPIC_EXAMPLES.md) use real source interviews. The three source rows were fixed before substantive reading: the first record of each pinned CSV. Their full 69 turns were read, and quotations were checked against the source, including speaker and character offsets. Selection is deterministic and convenient, not representative; one record per cohort does not support cohort comparisons. Interpretations were authored with AI assistance on November 13–14, 2026, without independent human ratings or a measured skill-versus-baseline experiment. Numerical screening of all interviews does not extend that qualitative reading scope.

Files prefixed `synthetic-` and `SYNTHETIC_CHECKS.md` remain wholly invented code-test examples. They are independent of the real interviews and any employee dataset.

## Parser limits

The source format uses line-start `Assistant:`, `AI:`, and `User:` labels. An identical label embedded inside a quoted response can be ambiguous. Structural checks identify empty messages and consecutive roles, but do not resolve every potential ambiguity or verify interview quality. Preserve both speakers and inspect the full source before interpreting a case.
