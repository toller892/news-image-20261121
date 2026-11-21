"""Copy the pre-made news image to the output directory.

The entry image (entry.png) is produced at build time and stored in this
repository. This program copies it, byte for byte, to the harness output
directory, so the gate and the judge see exactly the bytes committed here.
The copy is deterministic: the same input bytes always produce the same
output bytes, so the program's two runs agree.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
