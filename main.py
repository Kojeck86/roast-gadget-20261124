"""Entry for make.fun bounty u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.

Writes one single-line roast of a gadget used every day to
/output/entry.txt. Standard library only; deterministic: the same line
every run.

The roast: the robot vacuum that has mapped the whole house in perfect
detail and still eats the same charging cable every single morning —
a smart machine outsmarted by a cable it already knows is there.
"""

import os

LINE = (
    "My robot vacuum has mapped my entire house in perfect detail "
    "and still eats the same charging cable every single morning."
)


def main():
    # Gate: 1-200 characters, one line, no trailing newline.
    if not 1 <= len(LINE) <= 200:
        raise ValueError("entry line must be 1-200 characters, got %d" % len(LINE))
    if "\n" in LINE:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
