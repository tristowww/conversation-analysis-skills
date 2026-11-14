# Public data and attribution

Source: [Anthropic Interviewer](https://huggingface.co/datasets/Anthropic/AnthropicInterviewer), associated with [Introducing Anthropic Interviewer: What 1,250 professionals told us about working with AI](https://www.anthropic.com/research/anthropic-interviewer), December 4, 2025.

Attribution: Kunal Handa, Michael Stern, Saffron Huang, Jerry Hong, Esin Durmus, Miles McCain, Grace Yun, AJ Alt, Thomas Millar, Alex Tamkin, Jane Leibrock, Stuart Ritchie, and Deep Ganguli (2025).

The publisher describes 1,000 general-workforce interviews, 125 creative-professional interviews, and 125 scientist interviews, released with participant consent. This convenience research sample does not establish workforce prevalence or demographic representativeness.

## Version and license

The download code pins revision `c9e1ec1e6b093712b9c42235c7303ece647490e9` and verifies the three source-file SHA-256 hashes. The committed aggregate audit records the URLs, hashes, and file sizes.

The dataset card's license section specifies **CC-BY for data and MIT for code**. Its generic metadata header says MIT. This project follows the specific data statement; the card does not specify a CC-BY version, so none is assigned here. The source dataset's license does not automatically license this project's independently authored code or instructions.

Changes in this project: decode CSV records, recognize explicit speaker labels, preserve transcript text and hashes, add turn IDs and character offsets, and count corpus-level structural properties. No transcript content is rewritten or assigned a sentiment, topic, or intent by the preparation code. No publisher endorsement is implied.

## Local handling

Raw CSVs, exact-text prepared packages, participant identifiers, and any public-data analysis ledgers stay in ignored `.local-data/` or `.local-runs/` paths. Only the aggregate preparation audit is committed. Public availability is not a reason to infer identities or profile individual participants.

The committed conversations and evidence quotes under `examples/` are wholly invented for this project. They are not modified, anonymized, or sampled participant records. Their example annotations are authored illustrations, not human reference ratings or an observed model run.

## Parser limits

The source format uses line-start `Assistant:`, `AI:`, and `User:` labels. An identical label embedded inside a quoted response can be ambiguous. Structural checks identify empty messages and consecutive roles, but do not resolve every potential ambiguity or verify interview quality. Preserve both speakers and inspect the full source before interpreting a case.
