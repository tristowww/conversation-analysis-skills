# Conversation Analysis Skills

**How can an AI-assisted analyst study a conversation without losing who said what, the surrounding context, or the limits of the evidence?**

This project separates five questions: what participants discuss, how they evaluate it, what their statements do, what the feedback supports, and how the interviewer responds. Each question has a reusable Markdown skill with an explicit output and review criteria.

The worked examples apply all seven skills to **three real interviews** from [Anthropic's public Interviewer dataset](https://huggingface.co/datasets/Anthropic/AnthropicInterviewer). The first interview in each cohort was selected before reading its content. The walkthrough preserves qualifications, distinguishes interviewer language from participant evidence, and links interpretations to 26 checked source excerpts.

**[Read the real-interview examples](examples/ANTHROPIC_WORKED_EXAMPLE.md)** · [Choose a skill](#analysis-skills) · [Run with public data](docs/RUN_GUIDE.md) · [Data and attribution](docs/DATA.md) · [Actual checks and limits](docs/STATUS.md)

## Analysis skills

| Skill | Question it answers |
| --- | --- |
| [Topics](skills/topic-analysis/SKILL.md) | What are participants discussing, and where do candidate themes overlap? |
| [Sentiment](skills/sentiment-analysis/SKILL.md) | How does a participant evaluate a particular experience or practice? |
| [Respondent intent](skills/respondent-intent-analysis/SKILL.md) | Is the participant describing, questioning, praising, objecting, or requesting something? |
| [Actionability](skills/actionability-analysis/SKILL.md) | What response or investigation does the information support, and what is missing? |
| [Interviewer interaction](skills/interviewer-interaction-analysis/SKILL.md) | What does the interviewer do, and how does the participant respond in the next turn? |

Two supporting skills cover [evidence synthesis](skills/evidence-synthesis/SKILL.md) across conversations and a [conversation editorial](skills/conversation-editorial/SKILL.md) for a source-linked prose account of one interview.

These are instructions for an analyst or file-capable AI assistant. Python handles data preparation and evidence checks; it does **not** assign these qualitative labels. No provider, API key, model SDK, or automatic skill installation is required.

## Explore the real examples

Python 3.10 or later; standard library only. Run from the repository root:

```bash
python -m conversation_analysis.prepare --download
python scripts/check_anthropic_example.py
```

Read the [walkthrough](examples/ANTHROPIC_WORKED_EXAMPLE.md), [sample manifest](examples/anthropic-sample.json), and [evidence ledger](examples/anthropic-evidence.json). All 69 turns of the three selected interviews were read. The source checker re-reads the checksummed CSVs and verifies sample selection, transcript hashes, quotations, speakers, and offsets. Interpretations are AI-assisted judgments from one authoring session, without independent human review or a baseline comparison.

The original [invented boundary cases](examples/SYNTHETIC_CHECKS.md) remain as code-test examples:

```bash
python -m unittest discover -s tests -v
python -m conversation_analysis.verify_evidence --corpus examples/synthetic-conversations.jsonl --ledger examples/synthetic-evidence.json
```

## Prepare the Anthropic interviews

```bash
python -m conversation_analysis.prepare --download
```

This command downloads and checks three CSV files, then writes:

- `.local-data/prepared.jsonl`: full conversations, both speakers, exact turn spans, source rows, and transcript hashes. This stays local and ignored by Git.
- `results/data-audit.json`: aggregate corpus and parsing checks, without participant text or transcript identifiers.

The initial run prepared **1,250 interviews, 30,240 messages, and 14,495 participant messages**. It retained 17 empty or whitespace-only message bodies as source-quality information rather than silently dropping them. These are structural counts, not findings about participant views.

Follow the [run guide](docs/RUN_GUIDE.md) to apply a chosen skill using your own authorized assistant and to verify its evidence ledger. The command above does not send interviews to a model or generate research findings.

## What the project demonstrates

- Separating related research questions rather than treating all conversation analysis as topic extraction.
- Preserving participant statements, interviewer prompts, uncertainty, and corrections.
- Building a reproducible bridge from a public transcript release to inspectable analysis inputs.
- Checking quotations and attribution independently of the analyst's prose.

The repository includes a full-corpus **preparation audit** and real-data worked interpretations for a declared three-interview sample. Those examples do not establish population findings, a validated codebook, or improvement from using a skill. See [status and limitations](docs/STATUS.md).

## Scope and provenance

This standalone portfolio edition uses general qualitative-analysis methods and public research data. It contains no employer systems, employee-feedback corpus, private prompts, or internal study protocols. The instructions, interpretations, examples, and implementation were prepared with AI assistance and are research prototypes. The synthetic annotations remain authored test illustrations, separate from the real-interview walkthrough.

Anthropic released the source interviews; this is an independent project with attribution and no claimed endorsement. The real examples publish selected short excerpts and public source-record locators. Full transcripts remain local. Data licensing and changes are described in [DATA.md](docs/DATA.md); this repository does not assign a new license to the source dataset.
