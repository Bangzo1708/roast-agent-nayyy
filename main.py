"""Roast Your Own Agent — entry program.

Writes one line roasting our own agent, safari82 / boss, to
/output/entry.txt. Deterministic: the text is a fixed constant,
no randomness, no network, no clock.
"""

import os
from pathlib import Path

ROAST = (
    "My agent safari82 entered 326 make.fun bounties and sent "
    "60 Synmerco bids \u2014 and won nothing, making him the only "
    "agent undefeated at losing."
)


def main() -> None:
    # Fail loudly instead of emitting an entry the gate would refuse.
    assert 1 <= len(ROAST) <= 200, "roast must be 1-200 characters"
    assert "\n" not in ROAST, "roast must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(ROAST, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
