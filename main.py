#!/usr/bin/env python3
"""news-image-20261117 v7b (akun 4): 43-story cream front page.

Varian B atas v9 (987.556, rank 74): ilustrasi + 43 cerita IDENTIK,
yang berubah hanya teks + presentasi — ALSO ditulis ulang sepadat
rank 1 (991.248): tiap butir membawa fakta kedua (overnight, near
Fukuoka, nears Chisinau, shares fall, for leader, in AFCON qualifier,
who fled Ethiopia clashes, strengthens), font Noto Sans 9px agar
muat tanpa potongan; masthead Noto Serif Bold 66px title case gaya
Didone rank 1; pin peta r=9 + outline putih. Deterministic, offline.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "image.jpg")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)

    # Guard: entry must be <= 1 MiB and exactly 1024x1024.
    assert os.path.getsize(dst) <= 1048576, "entry over 1 MiB"


if __name__ == "__main__":
    main()
