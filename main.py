"""Six-word story entry for make.fun's "Six Words, One Story".

The program writes one complete story in exactly six words to
$OUTPUT_DIR/entry.txt (default /output). The story is 42 characters long,
inside the competition's 1-60 character gate.
"""

import os

# Six words, one story: a son comes home after a long absence and the
# woman who answers the door does not know him. The turn lands on the
# last word; everything before it is setup, everything after it is
# left for the reader to fill in.
TEXT = "He knocked. His mother answered. Stranger."


def main():
    # The gate counts Unicode code points and refuses whitespace-only text,
    # so check the contract here instead of trusting it silently.
    if not TEXT.strip() or not 1 <= len(TEXT) <= 60:
        raise SystemExit("entry text must be 1-60 code points, not whitespace-only")
    if len(TEXT.split()) != 6:
        raise SystemExit("entry text must be exactly six words")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
