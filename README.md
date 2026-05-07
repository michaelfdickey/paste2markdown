# paste2markdown

A local paste-to-markdown converter. Paste rendered content (from web pages, emails, documents) and get raw Markdown back instantly. All conversion happens in your browser, no data is sent anywhere.

## Quick Start

```bash
python3 launcher.py -p 5005
```

Then open http://localhost:5005 in your browser.

## Usage

1. Copy rendered content from any source (webpage, email, Google Doc, etc.)
2. Paste into the input area (Ctrl+V / Cmd+V)
3. Raw Markdown appears immediately in the output area
4. Click "Copy to Clipboard" to grab the Markdown

## Local Hoster Compatible

This app works with [local-hoster](https://github.com/michaelfdickey/local-hoster):

- **Frontend:** http://localhost:5005
- **Backend:** N/A (pure client-side app)
- Launcher scripts accept `-p` (frontend port) and `-b` (backend port) flags

## Files

```
paste2markdown/
├── index.html       # The web app UI
├── server.py        # Simple Python HTTP server
├── turndown.js      # HTML-to-Markdown library (downloaded on first run)
├── launcher.sh      # Shell launcher for local-hoster
├── launcher.py      # Python launcher for local-hoster
└── README.md
```

## 

![screencap](https://raw.githubusercontent.com/michaelfdickey/paste2markdown/refs/heads/main/screencap.png?token=GHSAT0AAAAAADGG6NUVKZSARSQT5JNUFW5G2P5BVRQ)
