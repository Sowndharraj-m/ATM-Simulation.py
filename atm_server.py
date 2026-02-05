"""
ATM Web Server - No external dependencies required!
Uses Python's built-in http.server module.

Run with: python atm_server.py
Then open: http://localhost:8000
"""

import http.server
import socketserver
import webbrowser
import os

PORT = 8000

# Change to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print("=" * 50)
print("🏧 Python ATM Web Server")
print("=" * 50)
print(f"\n✅ Server starting on port {PORT}...")
print(f"🌐 Open your browser at: http://localhost:{PORT}/ATM_Web.html")
print("\n💡 Press Ctrl+C to stop the server\n")

# Auto-open browser
webbrowser.open(f'http://localhost:{PORT}/ATM_Web.html')

# Create and start the server
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n👋 Server stopped. Goodbye!")
