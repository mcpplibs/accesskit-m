#!/usr/bin/env python3
"""src/accesskit.cppm is what tools/gen_module.py makes of upstream's header.

The header is read from the release archive upstream/documents.json names,
its SHA-256 verified — not from whatever a local package store holds.

    python3 tools/check_module.py [--archive accesskit-c-0.23.1.zip]
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import urllib.request
import zipfile

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / "upstream/documents.json").read_text())
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--archive", type=Path, help="an already downloaded copy of the release archive")
args = parser.parse_args()
with tempfile.TemporaryDirectory() as directory:
    archive = args.archive or Path(directory) / "accesskit-c.zip"
    if not args.archive:
        urllib.request.urlretrieve(manifest["upstream"], archive)
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    if digest != manifest["upstream_sha256"]:
        sys.exit(f"{archive}: sha256 {digest}, not {manifest['upstream_sha256']}")
    with zipfile.ZipFile(archive) as zip:
        name = next(n for n in zip.namelist() if n.endswith("/include/accesskit.h"))
        header = Path(directory) / "accesskit.h"
        header.write_bytes(zip.read(name))
    sys.exit(subprocess.run([sys.executable, str(root / "tools/gen_module.py"), str(header),
                             "--check", str(root / "src/accesskit.cppm")]).returncode)
