#!/bin/bash
# launcher.sh - Start paste2markdown with configurable ports

# Default ports
FRONTEND_PORT=5005

# Parse arguments from Local Hoster
while getopts "p:b:" opt; do
    case $opt in
        p) FRONTEND_PORT="$OPTARG" ;;
        b) ;; # No backend needed for this app
    esac
done

cd "$(dirname "$0")"

# Download turndown.js if not present
if [ ! -f "turndown.js" ]; then
    echo "Downloading turndown.js..."
    python3 -c "import urllib.request; urllib.request.urlretrieve('https://unpkg.com/turndown@7.2.0/dist/turndown.js', 'turndown.js')"
fi

# Start the server
python3 server.py -p "$FRONTEND_PORT"
