"""Toaster error message entry for the make.fun bounty
"u-eager-stork-81-9647-the-funniest-toaster-error-436406cd".

Writes one line (93 chars) to /output/entry.txt: a deadpan error
message from a kitchen toaster whose bread has declined to brown
and filed for a transfer to the freezer. Fresh angle: the bread as
a disgruntled employee filing an HR transfer, not a burnt-toast
or 404 pun; the punch lands on the last two words.
"""

import os

ENTRY = "E14: Bread declined to brown and has requested a transfer to the freezer. No further comment."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
