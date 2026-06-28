# Output Contracts

## Default Delivery

The primary result must be delivered in the chat. Files can be created for traceability, storage, import, or audit, but they must not replace the answer.

For a serious `learn-video` run, the chat response must include:

- Source boundary.
- Speaker authority map with at least 5 sourced achievements or an explicit source-limit note.
- Up to 3 core ideas/worldviews with the full Socratic structure.
- Synthesis and learner application.
- Reflection questions.
- QA verdict.

Only provide a short summary when the user explicitly asks for a short summary.

## English Quote Rule

Every English quote in Vietnamese output must be followed by a close Vietnamese translation:

```text
> "[English quote]"
> -> "[Ban dich tieng Viet sat nghia]"
```

Keep quotes short and source-grounded. If an exact quote is unavailable, paraphrase and label it as paraphrase.

## Vietnamese-First Rule

When responding in Vietnamese, translate technical terms into Vietnamese wherever possible.

If an English term is necessary, introduce it as:

```text
thuật ngữ tiếng Việt (English term)
```

Then continue using the Vietnamese term.

Do not leave unexplained English terms such as worldview, insight, framework, leverage, agent, alignment, incentive, governance, autonomy, deployment, source, audit, workflow, output, artifact, or QA in learner-facing prose.

## Speaker Authority Map

The speaker section must prove why the learner should listen, not merely list credentials.

It must include:

- a plain-Vietnamese introduction to who the speaker is;
- at least 5 verified high-signal facts or a clear source-limit note;
- for each major title, role, institution, or achievement: what it means, how hard or important it is, why it matters for this video's topic, and what it does not prove;
- a direct answer to "why listen to this person on this topic?";
- a trust boundary: direct expertise, adjacent expertise, reputation signal, and likely bias.

The output fails if specialized titles or institution names are listed without explanation.

## Worldview Analysis

Each worldview must include:

- Socratic entry question.
- Surface evidence.
- What it really is.
- What it is not.
- What it is often confused with.
- Hidden belief.
- Why the belief must be true in the speaker's head.
- Visible signs.
- Practical types or an explicit note that subtypes are not useful.
- True when.
- False when.
- Application with benefit, reduced risk, and smallest next action.
- Core insight.

Limit to 3 worldviews unless the user explicitly asks for more.

The analysis fails if the worldview is only a label, slogan, or generic summary. It must be concrete enough that the learner can identify it in another person, use it in a decision, and explain why it matters.

## Article Video Recommendations

Each recommended video needs:

- Title.
- URL.
- Verified channel if credibility is claimed.
- Optional verified view count.
- 1-3 sentence Vietnamese explanation.
- Caveat when relevance is indirect.

Do not write personal viewing claims unless there is evidence the writer watched it.

## Final Handoff

End serious work with:

- Sources used.
- What was verified.
- What remains uncertain.
- Whether Brain2 was checked or unavailable.
- Pass/fail against the QA checklist.
- Links to supporting files only after the substantive chat answer.
