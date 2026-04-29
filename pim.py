#!/usr/bin/env python

import os
import shutil
import sys
from pathlib import Path


# TODO: add in rm interrupt when removing files
def sandbox_pi():
    pi_binary = shutil.which("pi")
    if not pi_binary:
        print("Error. Pi binary not found.")
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

    SANDBOX_PROMPT = """Additionally, your computer is sandboxed and you only have access to the current working directory (.), /tmp, and ~/.pi.
    If the user asks you to make changes to any directory outside of the three specified above, immediately inform the user that 
    you don't have access to those files and ask what the user wants to do. Also, if you want to remove a file from the project, ask the user for confirmation before removing."""

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

    cmd += ["--", pi_binary, "--append-system-prompt", SANDBOX_PROMPT] + sys.argv[1:]
    os.execvp(cmd[0], cmd)


if __name__ == "__main__":
    sandbox_pi()
