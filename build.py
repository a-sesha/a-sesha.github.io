#!/usr/bin/env python3
"""Build this site with the blog engine (https://github.com/a-sesha/blog-template): the code, theme and built-in pieces live
there; this repository holds only the site's own content. The engine is found at ./engine (a git submodule or a checkout) or,
next to this folder, at ../blog-template.

    python build.py                 # build into public/, drafts included
    python build.py --publish --check
"""
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
for candidate in (HERE / "engine" / "build.py", HERE.parent / "blog-template" / "build.py"):
    if candidate.exists():
        break
else:
    sys.exit("the blog engine was not found: put a copy of blog-template at ./engine or next to this folder as ../blog-template")
sys.exit(subprocess.call([sys.executable, str(candidate), "--site", str(HERE), *sys.argv[1:]]))
