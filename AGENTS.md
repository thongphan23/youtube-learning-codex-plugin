# Agent Instructions For YouTube Learning

Start with `skills/index/SKILL.md`.

This plugin is for research and learning from YouTube, not uploading or publishing videos. If the task is upload, title, description, thumbnail, chapters, privacy, OAuth, or YouTube Studio, use the separate `youtube-publisher` plugin instead.

Default routing:

- YouTube URL, transcript, interview, talk, lecture, podcast, speaker profile, worldview, belief archaeology: `skills/learn-video/SKILL.md`.
- Article, draft, thesis, Facebook post, essay, lesson, source recommendations, "find videos": `skills/discover-videos/SKILL.md`.

Core rules:

- Evidence first. Do not invent transcript, biography, channel identity, view count, quotes, or Brain2 matches.
- Default output belongs in the chat. Files are supporting evidence or reusable artifacts, not a substitute for the full answer.
- Vietnamese-first. Translate or explain English technical terms in Vietnamese the first time they appear; avoid unexplained English such as worldview, insight, framework, leverage, agent, alignment, incentive, governance, autonomy, or deployment.
- Speaker sections must prove authority, not list a resume. Explain titles, institutions, achievements, and roles in plain Vietnamese: what they mean, how hard or important they are, why they matter for the video topic, and what they do not prove.
- Every direct English quote in Vietnamese output must be followed by a close Vietnamese translation.
- For Thong Phan personal-brand or Brain2 atomization work, Brain2 is the durable knowledge source; if Brain2 tools are unavailable, say so and continue with an explicit fallback.
- Do not claim the writer has watched a video unless the user or local evidence says so.
- Distinguish "speaker said", "agent inferred", and "application suggestion".
