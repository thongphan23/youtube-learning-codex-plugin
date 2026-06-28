# YouTube Learning Codex Plugin

YouTube Learning is a Codex plugin for learning from YouTube without reducing a talk to a surface summary.

It ports two Antigravity workflows into Codex:

- `/youtube-learn`: decode a YouTube video into speaker context, worldview, belief structure, limits, and reusable learning atoms.
- `/youtube-discover`: turn an article or thesis into a curated set of credible YouTube videos that support, challenge, or deepen the idea.

The plugin is router-first, following the same design pattern used by Product Design and Build Web Apps: a small index skill routes work into focused phase skills, references hold reusable contracts, and scripts handle repeatable checks.

## Install Locally

Clone the repo into your local plugin folder:

```bash
mkdir -p ~/plugins
git clone https://github.com/thongphan23/youtube-learning-codex-plugin.git ~/plugins/youtube-learning
```

Add it to your personal marketplace at `~/.agents/plugins/marketplace.json`:

```json
{
  "name": "youtube-learning",
  "source": {
    "source": "local",
    "path": "./plugins/youtube-learning"
  },
  "policy": {
    "installation": "AVAILABLE",
    "authentication": "ON_INSTALL"
  },
  "category": "Education"
}
```

Enable it in `~/.codex/config.toml`:

```toml
[plugins."youtube-learning@personal"]
enabled = true
```

Refresh the local marketplace cache:

```bash
codex plugin marketplace add ~
```

Start a new Codex thread and mention `@youtube-learning`.

## Usage

Decode a video:

```text
@youtube-learning decode this video: https://www.youtube.com/watch?v=...
```

Find supporting videos for an article:

```text
@youtube-learning find credible YouTube videos for this article:

<paste article>
```

Save learning into Brain2:

```text
@youtube-learning turn this talk into Brain2 worldview atoms
```

## Agent Contract

Agents should start at `skills/index/SKILL.md`.

Use `learn-video` when the user gives a YouTube link, transcript, podcast interview, talk, lecture, or asks to decode a speaker worldview.

Use `discover-videos` when the user gives an article, draft, thesis, lesson, or content idea and asks for videos to support or challenge it.

Do not fabricate transcripts, speaker biography, view counts, channel identity, or personal viewing claims. Use source evidence, label uncertainty, and ask for user-provided transcript when tools cannot retrieve it.

## Privacy

This plugin is local-first. It does not ship a hosted service or store data outside the user machine by itself. Agents may use whatever search, browser, transcript, or vault tools the current Codex environment exposes.

## Terms

This is an unofficial learning workflow for YouTube URLs and related public metadata. It is not affiliated with, endorsed by, or sponsored by YouTube.
