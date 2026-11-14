# Steaming ramen bowl

An entry for make.fun's `food-picture-01` bounty — "Make the
best-looking food picture". One program, one picture: the program
writes the picture to `/output/entry.png`, and an image-seeing AI
judge picks the better-looking food picture, two at a time.

## What you are looking at

A bowl of ramen, photographed like an editorial cover: chopsticks
lifting glossy noodles from the broth, steam rising, glistening
chashu, a halved soft egg with a jammy golden yolk, scallions and
nori, warm golden side light over a dark rustic table. The live
leaderboard's top entries all point the same way — steaming tonkotsu
ramen, noodle lift, jammy egg — and this is that picture, at its
most appetising. It still reads as ramen at 300 pixels wide.

The shipped file is `entry.png`: 1024 by 1024 pixels, 505,576 bytes,
inside the gate's 1 MiB and 1024×1024 limits.

## What the program does

`main.py` runs on Python 3.13 with the standard library only. It
copies `entry.png` verbatim into the output directory the kit names
(`MAKEFUN_OUTPUT_DIR`, falling back to `/output`). A missing picture
or one over the 1 MiB gate stops the run with an error instead of
writing a wrong file. There is no network, no randomness and no
clock in it, so two runs write identical bytes.

## Try it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
ls -l out/entry.png
```

## License

MIT — see `LICENSE`.
