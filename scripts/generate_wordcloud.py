#!/usr/bin/env python3
"""Generate the community word cloud image from data/words.json."""

from __future__ import annotations

import json
import random
from pathlib import Path

from wordcloud import WordCloud

ROOT = Path(__file__).resolve().parents[1]
WORDS_PATH = ROOT / "data" / "words.json"
OUTPUT_PATH = ROOT / "assets" / "wordcloud.png"

# Cyberpunk-ish palette: hot coral → electric cyan
COLORS = [
    "#ff6b6b",
    "#ff8e8e",
    "#f472b6",
    "#e879f9",
    "#a78bfa",
    "#60a5fa",
    "#38bdf8",
    "#22d3ee",
    "#2dd4bf",
    "#34d399",
]


def color_func(
    word: str | None = None,
    font_size: int | None = None,
    position: tuple[int, int] | None = None,
    orientation: int | None = None,
    font_path: str | None = None,
    random_state: random.Random | None = None,
) -> str:
    rng = random_state or random.Random()
    return rng.choice(COLORS)


def main() -> None:
    payload = json.loads(WORDS_PATH.read_text(encoding="utf-8"))
    words: list[str] = payload.get("words", [])
    if not words:
        raise SystemExit("No words in data/words.json")

    text = " ".join(words)
    seed = random.randint(0, 2**32 - 1)

    wc = WordCloud(
        width=1200,
        height=520,
        background_color="#0d1117",
        max_words=200,
        prefer_horizontal=0.7,
        min_font_size=10,
        max_font_size=120,
        collocations=False,
        color_func=color_func,
        random_state=seed,
    )
    wc.generate(text)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    wc.to_file(str(OUTPUT_PATH))
    print(f"Wrote {OUTPUT_PATH} ({len(words)} words, seed={seed})")


if __name__ == "__main__":
    main()
