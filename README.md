# OpenRouter prices dashboard

Static single-page dashboard listing all 367 models available via [OpenRouter](https://openrouter.ai/), with search, filters, and per-modality breakdowns (input vs output, image/audio/video/file).

**Live:** https://ndemchishin.github.io/or-models/

## Features

- Search by model ID or description
- Provider filter (50+ providers)
- Separate filters for input modalities (image / audio / video / file) and output modalities (image / audio)
- Distinguishes truly free models (`:free` suffix, rate-limited) from "preview" models (priced at $0 in the API but billed via upstream)
- Sortable by price, context length, output/input ratio
- Color-coded prices: cyan = free, green <$1/M, orange $1–10/M, red ≥$10/M
- Self-contained — single HTML file, no build, works offline

## How it's built

- `template.html` — page with `__DATA__`, `__UPDATED__`, `__COUNT__` placeholders
- `build.py` — fetches `https://openrouter.ai/api/v1/models`, renders `index.html`
- `.github/workflows/refresh.yml` — runs `build.py` every Monday 06:00 UTC and commits if data changed (also runnable manually via Actions tab)

Refresh locally:

```bash
python3 build.py
```

## License

MIT
