# Source Policy

## Transcript Priority

Use sources in this order:

1. User-provided transcript or notes.
2. Official transcript or podcast page.
3. YouTube transcript panel through browser tools.
4. `yt-dlp` captions or subtitles when available.
5. Search snippets only as a fallback for discovery, not for deep video analysis.

If there is no transcript or reliable summary, do not perform full worldview decoding. Ask for transcript or continue only with a clearly labeled metadata-level preview.

## Speaker Research

Use reliable sources for speaker profile:

- Official website.
- Publisher, university, company, podcast, or conference page.
- Credible interview pages.
- Wikipedia only as a pointer, not as sole evidence for unusual claims.

Do not invent nationality, credentials, achievements, or quotes.

## YouTube Channel Verification

When credibility depends on channel identity, verify with at least one of:

- YouTube oEmbed `author_name` and `author_url`.
- YouTube Data API.
- Official channel page inspected through browser.

Exa or search-result `author` fields are useful candidates, not final channel identity.

## View Counts

View counts are optional. Show them only when fetched from YouTube metadata, page structured data, or YouTube Data API. If unavailable, omit the field.

