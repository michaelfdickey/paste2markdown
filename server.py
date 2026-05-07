#!/usr/bin/env python3
"""Simple HTTP server to serve the paste2markdown app."""

import argparse
import http.server
import os
import sys


def main():
    parser = argparse.ArgumentParser(description="Paste to Markdown server")
    parser.add_argument("-p", "--port", type=int, default=5005,
                        help="Port to serve on (default: 5005)")
    args = parser.parse_args()

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    handler = http.server.SimpleHTTPRequestHandler
    server = http.server.HTTPServer(("127.0.0.1", args.port), handler)

    print(f"Paste to Markdown running at http://localhost:{args.port}")
    print("Press Ctrl+C to stop.")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down.")
        server.shutdown()


if __name__ == "__main__":
    main()
