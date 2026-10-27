# a-sesha.github.io

The content of my site. The engine (code, theme, built-in pieces) lives in
[blog-template](https://github.com/a-sesha/blog-template) and is used from `../blog-template` or `./engine`.

```bash
python build.py                    # build into public/ (drafts shown with a badge)
python build.py --publish --check  # what gets uploaded: no drafts, every link checked
```

- `content/drafts/`: work in progress (and its media). Built locally with a draft badge, never published, and ignored by git, so it
  stays out of this public repository; move a finished post to `content/posts/`.
- `site.json`: name, description and, once decided, the site address (`url`; it switches on the feed and sitemap).
- `content/posts/NAME.html` (+ an optional `NAME/` folder with that post's own media, scripts and styles), `content/pages/`,
  `content/images/`, `content/snippets/` (my own reusable pieces).
- To change how the site looks, put a file of the same name under `theme/` (for example `theme/style.css`); it replaces the engine's.
- `.github/workflows/pages.yml` publishes to GitHub Pages; see the notes at the top of that file before enabling it.
