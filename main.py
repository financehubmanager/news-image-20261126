#!/usr/bin/env python3
"""Entry program for make.fun's "Sum up 26 November's world news in
one image" bounty (news-image-20261126).

The image is pre-rendered (see render.py) and shipped in this
repository as entry.png, because the grading sandbox has no network:
all news facts are baked into the image at build time. This program
only copies it to the output directory, deterministically.
"""
import os
import shutil


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    # Plain byte copy: no timestamps, no randomness, no rendering at
    # run time, so the two grading runs produce identical bytes.
    shutil.copyfile(os.path.join(here, "entry.png"),
                    os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
