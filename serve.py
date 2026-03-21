#!/usr/bin/env python3
"""簡易 HTTP 伺服器，用於本地預覽 SPY 量化儀表板"""
import http.server
import socketserver
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
PORT = 8080

handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"伺服器啟動於 http://localhost:{PORT}")
    httpd.serve_forever()
