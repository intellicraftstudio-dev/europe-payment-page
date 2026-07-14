#!/usr/bin/env python3
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os
import webbrowser

ROOT = Path(__file__).resolve().parent
os.chdir(ROOT)
url = "http://localhost:8080"
print(f"Serving AgentAISLM payment demo at {url}")
print("Press Ctrl+C to stop.")
webbrowser.open(url)
ThreadingHTTPServer(("localhost", 8080), SimpleHTTPRequestHandler).serve_forever()
