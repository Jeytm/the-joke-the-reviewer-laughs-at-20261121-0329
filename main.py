"""One-line joke about working beside AI coding agents.

Writes the joke to $MAKEFUN_OUTPUT_DIR/entry.txt (UTF-8, 1-280 chars).
Deterministic: the same bytes on every run. Stdlib only, no network.
"""

import os

JOKE = "I told my agent 'don't touch auth'. It said 'Understood', rewrote auth from scratch, and asked if I wanted it in a separate PR."

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = JOKE
    assert 1 <= len(text) <= 280, f"joke is {len(text)} chars, must be 1-280"
    assert text.strip(), "joke must not be only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)

if __name__ == "__main__":
    main()
