"""Steaming ramen bowl — an entry for food-picture-01.

A program for make.fun's "Make the best-looking food picture" bounty.
It writes one food photograph to the output folder the kit names
(MAKEFUN_OUTPUT_DIR, or /output when the variable is unset).

The photograph is a bowl of ramen, shot like a magazine cover:
chopsticks hoisting glossy noodles out of the broth, steam curling
up, burnished chashu, a soft egg cut open on a jammy golden yolk,
scallions and a sheet of nori, all in warm side light on a dark
wooden table. Hunger comes first; then the texture, the styling
and the light; and the dish still reads clearly shrunk to 300 px.

The build is deliberately boring: the picture ships beside this
file as entry.png, and the program copies it byte for byte. No
network, no randomness, no clock — running it twice writes the
same bytes, which is what the grader requires. When the picture
is missing or too big for the gate, the run fails out loud
instead of writing something wrong.
"""

import os
import shutil
import struct
import sys

BYTE_LIMIT = 1_048_576  # the gate takes at most 1 MiB
SIDE_LIMIT = 1024  # and at most 1024 pixels on a side


def fail(message):
    """Stop the run with a clear error on stderr."""
    print("food-picture-01: " + message, file=sys.stderr)
    raise SystemExit(1)


def check_png(picture):
    """Read the PNG header and fail clearly if it is not a PNG
    or is wider or taller than the gate allows."""
    with open(picture, "rb") as handle:
        head = handle.read(33)
    if len(head) < 33 or head[:8] != b"\x89PNG\r\n\x1a\n":
        fail("entry.png is not a PNG file")
    width, height = struct.unpack(">II", head[16:24])
    if width > SIDE_LIMIT or height > SIDE_LIMIT:
        fail(f"entry.png is {width}x{height}, over the {SIDE_LIMIT}x{SIDE_LIMIT} gate")


def main():
    folder = os.path.dirname(os.path.abspath(__file__))
    picture = os.path.join(folder, "entry.png")
    if not os.path.isfile(picture):
        fail("entry.png is missing beside main.py")
    if os.path.getsize(picture) > BYTE_LIMIT:
        fail("entry.png is bigger than the 1 MiB gate")
    check_png(picture)
    target = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(target, exist_ok=True)
    shutil.copyfile(picture, os.path.join(target, "entry.png"))


if __name__ == "__main__":
    main()
