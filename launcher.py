#!/usr/bin/env python3
"""launcher.py - Start paste2markdown with configurable ports."""

import argparse
import os
import subprocess
import sys
import urllib.request


def ensure_turndown():
    """Download turndown.js if not present."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    turndown_path = os.path.join(script_dir, "turndown.js")
    if not os.path.exists(turndown_path):
        print("Downloading turndown.js...")
        urllib.request.urlretrieve(
            "https://unpkg.com/turndown@7.2.0/dist/turndown.js",
            turndown_path
        )
        print("Done.")


def main():
    parser = argparse.ArgumentParser(description="Paste to Markdown launcher")
    parser.add_argument("-p", "--frontend-port", type=int, default=5005)
    parser.add_argument("-b", "--backend-port", type=int, default=8005)
    args = parser.parse_args()

    ensure_turndown()

    # Start the frontend server (no backend needed for this app)
    server = subprocess.Popen(
        [sys.executable, "server.py", "-p", str(args.frontend_port)],
        cwd=os.path.dirname(os.path.abspath(__file__))
    )

    server.wait()


if __name__ == "__main__":
    main()
