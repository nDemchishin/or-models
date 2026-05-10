#!/usr/bin/env python3
"""Fetch OpenRouter models and render index.html from template.html."""
import json, urllib.request, datetime, pathlib, sys

ROOT = pathlib.Path(__file__).parent
API = "https://openrouter.ai/api/v1/models"

def fetch():
    with urllib.request.urlopen(API, timeout=30) as r:
        return json.load(r)["data"]

def shape(m):
    pricing = m.get("pricing", {})
    arch = m.get("architecture", {})
    pid = m["id"]
    in_p = float(pricing.get("prompt", 0)) * 1_000_000
    out_p = float(pricing.get("completion", 0)) * 1_000_000
    return {
        "id": pid,
        "provider": pid.split("/")[0],
        "name": pid.split("/", 1)[1] if "/" in pid else pid,
        "in": in_p,
        "out": out_p,
        "ctx": m.get("context_length", 0),
        "truly_free": pid.endswith(":free"),
        "preview_warning": (in_p == 0 and out_p == 0 and not pid.endswith(":free")),
        "in_mod": arch.get("input_modalities", []),
        "out_mod": arch.get("output_modalities", []),
        "desc": (m.get("description") or "")[:280],
    }

def main():
    models = [shape(m) for m in fetch()]
    msk = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3)))
    updated = msk.strftime("%Y-%m-%d %H:%M МСК")
    template = (ROOT / "template.html").read_text(encoding="utf-8")
    out = (template
        .replace("__DATA__", json.dumps(models, ensure_ascii=False))
        .replace("__UPDATED__", updated)
        .replace("__COUNT__", str(len(models))))
    (ROOT / "index.html").write_text(out, encoding="utf-8")
    print(f"OK — {len(models)} models, snapshot {updated}, {len(out):,} bytes")

if __name__ == "__main__":
    sys.exit(main())
