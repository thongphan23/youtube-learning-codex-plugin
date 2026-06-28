---
name: learn-video
description: "Decode a YouTube video, transcript, talk, lecture, podcast, or interview into speaker context, worldviews, limits, applications, and optional Brain2 atoms."
---

# Learn Video

Use this skill when the user gives a YouTube URL, transcript, podcast interview, talk, lecture, or asks to learn from a speaker.

## Required References

Before running a serious decode, read:

- `../../references/source-policy.md`
- `../../references/speaker-research-contract.md`
- `../../references/chat-output-contract.md`
- `../../references/vietnamese-style-contract.md`
- `../../references/output-contracts.md`
- `../../references/socratic-worldview-contract.md`
- `../../references/brain2-vault-contract.md` when Brain2 storage or comparison is requested.
- `../../references/quality-rubric.md` before final handoff.

## Phase 1: Source Capture

Collect the best available evidence:

1. Metadata: URL, title, channel, upload date, description, and oEmbed author identity when possible.
2. Transcript: prefer user-provided transcript; otherwise try available transcript tools, browser transcript panel, `yt-dlp` captions, or official podcast/transcript pages.
3. Speaker context: search reliable web sources when the speaker is not already known from provided context.

If transcript capture fails, stop and ask for transcript or a summary. Do not continue as if the full talk was read.

Useful helper:

```bash
python3 /Users/rio/plugins/youtube-learning/scripts/youtube_learning.py oembed "https://www.youtube.com/watch?v=..."
```

## Output Mode

Default to full chat delivery. The user should be able to judge the length, depth, clarity, and usefulness directly from the chat response.

Use files only as supporting artifacts when:

- the transcript is long;
- the user asks to save durable notes;
- a reusable Brain2 import draft is needed;
- the run needs audit evidence.

Even when files are created, the final chat response must include the full substantive analysis: speaker portrait, core ideas, Socratic worldview sections, synthesis, application, source boundary, and QA verdict. Do not answer with only file links or a short summary unless the user explicitly asks for a short summary.

## Phase 2: Speaker Authority Map

Write a speaker section that helps the learner decide whether to listen, how much to trust, and where to stay careful. This is not a resume dump.

Cover:

- Human introduction: who this person is in plain Vietnamese, not only title, employer, or discipline.
- At least 5 concrete achievements, credentials, books, papers, institutional roles, public contributions, or high-signal career facts.
- For every role, institution, title, or achievement that appears, explain:
  - what it means in everyday language;
  - whether it is difficult, rare, prestigious, or merely descriptive;
  - why it matters for this video's topic;
  - what it does not prove.
- What makes the speaker unusual among strong peers.
- Why this person is worth listening to for this topic, written as 2-4 concrete reasons.
- The trust boundary: where their authority is direct, where it is adjacent, and where the learner should treat it as opinion.
- Likely bias or lens created by their career, institution, incentives, or community.
- Context of the appearance: who they spoke with, where, and why that context matters.

Do not guess biographical facts. Mark unknowns. If fewer than 5 achievements can be verified, say exactly how many were found and what sources were checked. Do not leave unexplained phrases like "associate professor", "principal investigator", "fellow", "think tank", "research lab", "venture partner", or institution names without explaining why they matter.

## Phase 3: Belief Archaeology

Choose at most 3 worldviews. For each worldview, use this exact structure. The goal is not to name an idea; the goal is to make the user feel the value, boundary, and application of the idea.

### Worldview #[N]: [short name]

**Socratic entry question**

Ask the one question that makes the worldview necessary.

**Surface evidence**

> "[English quote]"
> -> "[Vietnamese close translation]"

Explain what the speaker said, decided, or noticed in context.

**What it really is**

Define it in plain Vietnamese in 1-2 sentences.

**What it is not**

State the most tempting wrong interpretation.

**Often confused with**

Name the adjacent idea people mix it up with, then separate them.

**Hidden belief**

Write one Vietnamese sentence that is simple enough to remember after one reading. Avoid abstract philosophy language.

**Why this belief must be true in their head**

Explain what assumption underneath the quote makes the claim coherent. State what mainstream belief it rejects.

**Visible signs**

List 3-5 concrete behaviors, decisions, phrases, or tradeoffs that reveal this worldview in real life.

**Types**

If useful, split the worldview into 2-4 practical types. If no useful types exist, say "No useful subtype; treat it as one lens."

**True when**

Give 2 concrete examples that a high-school student can understand.

**False when**

Give 1-2 cases where applying this worldview would create bad results.

**Application for Thong Phan or the user**

Give one specific action in one domain: influence, persuasion, content, learning, product, or life. Include the benefit, the risk it reduces, and the smallest next action.

**Core insight**

Compress the worldview into one reusable sentence the user could use in a talk, lesson, note, or product rule.

## Phase 4: Synthesis

Provide:

- A table of the 3 core beliefs and their clearest behavior.
- Contrast with mainstream thinking.
- Internal tension: what contradiction exists inside the worldview and how the speaker handles it.
- "So what for the learner": the 3 highest-leverage changes in how the user should think, decide, or build.

## Phase 4.5: Chat Answer Assembly

Assemble the final chat answer in Vietnamese-first language:

1. Source boundary: what was read, what was verified, and what remains uncertain.
2. Speaker authority map with 5+ concrete achievements and a plain-Vietnamese explanation of why each one matters.
3. The 3 most valuable ideas, each with the full Socratic structure.
4. Practical use for the learner, not only abstract meaning.
5. Synthesis table.
6. Reflection questions.
7. Optional file/artifact links at the end, never as a replacement for the analysis.

## Phase 5: Brain2 Check

When Brain2 is relevant and tools are available, search Brain2 for:

- Reinforcing ideas.
- Contradicting ideas.
- Extensions.
- Personal stories or prior decisions that make the worldview usable.

Classify each match as reinforce, contradiction, extension, or new.

## Phase 6: Reflection Questions

End with 3 questions:

1. What in this worldview feels uncomfortable?
2. If this worldview were fully adopted, what would change first?
3. Where is this worldview wrong or incomplete?

Ask which worldview the user wants to save to the Worldview Library.

## Phase 7: Atomization

If saving is requested:

- Draft or update Speaker Profile automatically.
- Ask before saving Worldview Library atoms unless the user explicitly asked to save all.
- Follow `../../references/brain2-vault-contract.md`.

## QA Checklist

- At most 3 worldviews.
- Speaker authority map has at least 5 sourced achievements or clearly states why fewer were found.
- Speaker roles, titles, institutions, and achievements are translated into plain meaning, topic relevance, trust value, and trust limits.
- Each worldview has Socratic entry question, surface evidence, what it is, what it is not, common confusion, hidden belief, visible signs, types, true cases, false cases, application, and core insight.
- Hidden belief is plain Vietnamese, not academic jargon.
- Application states benefit, reduced risk, and smallest next action.
- English quotes have Vietnamese close translation.
- Speaker facts are sourced or marked unknown.
- Transcript gaps are disclosed.
- Brain2 availability and result boundary are stated.
- Final chat response contains the full analysis, not just links to files.
- Vietnamese-first language: English terms are avoided, translated, or explained immediately.
