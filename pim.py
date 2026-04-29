#!/usr/bin/env python

import os
import shutil
import sys
from pathlib import Path


# TODO: For this to actually work as intended, enable subprocess execution so killing the script kills pi
# TODO: add in rm interrupt when removing files
def sandbox_pi():
    pi_binary = shutil.which("pi")
    if not pi_binary:
        print("Error. Pi binary found.")
        exit(1)

    ALLOWED_DIRS = [
        Path.cwd(),
        Path.home() / ".pi",
        Path("/tmp"),
    ]
    EXCLUDED_DIRS = [
        Path.home() / ".ssh",
        Path.home() / ".aws",
    ]

    # TODO: COnfirm this blocks sudo level calls
    cmd = [
        "bwrap",
        "--unshare-all",
        "--share-net",  # Required for Pi to talk to LLMs
        "--dev",
        "/dev",
        "--proc",
        "/proc",
        "--ro-bind",
        "/",
        "/",
    ]

    for path in ALLOWED_DIRS:
        if path.exists():
            p = str(path.resolve())
            cmd += ["--bind", p, p]
    for path in EXCLUDED_DIRS:
        if path.exists():
            cmd += ["--tmpfs", str(path.resolve())]

    cmd += ["--", pi_binary] + sys.argv[1:]
    os.execvp(cmd[0], cmd)


if __name__ == "__main__":
    sandbox_pi()
