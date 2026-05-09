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

## How to refresh the data

```bash
curl -s https://openrouter.ai/api/v1/models > models.json
# regenerate index.html with the new snapshot
```

Snapshot inside `index.html` was captured 2026-05-09.

## License

MIT
