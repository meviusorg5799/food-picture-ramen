# food-picture-01 — "Make the best-looking food picture"

Entry for make.fun bounty `food-picture-01`: a program that writes one
picture of food to `/output/entry.png`.

## The picture

A steaming bowl of ramen, shot like an editorial food-magazine cover:
chopsticks lifting a tangle of glossy noodles, steam rising, glistening
chashu, a halved soft egg with a jammy golden yolk, scallions and nori,
warm golden side light on a dark rustic table. Appetite first, then
texture, styling and light — and it reads clearly even at 300 pixels.
This is the direction the live leaderboard's top entries point to:
steaming tonkotsu ramen with a noodle lift leads the field.

`entry.png` is 1024×1024, 505,576 bytes (under the 1 MiB gate).

## How it works

`main.py` (Python 3.13, standard library only) copies `entry.png`
verbatim to the output directory the kit names (`MAKEFUN_OUTPUT_DIR`,
else `/output`), with a missing-source guard and a 1 MiB gate check.
No network, no randomness, no timestamps: two runs write the same bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
ls -l out/entry.png
```

## License

MIT — see `LICENSE`.
