"""Dev server: static files + POST /shot saves a dataURL JPEG to .claude/shots/.
Used by the agent verification loop (SW.shot() -> fetch POST -> Read file)."""
import base64, http.server, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHOTS = os.path.join(ROOT, '.claude', 'shots')
os.makedirs(SHOTS, exist_ok=True)

class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

    def do_POST(self):
        if self.path.startswith('/shot'):
            name = self.path.split('=')[-1] if '=' in self.path else 'shot'
            n = int(self.headers.get('Content-Length', 0))
            data = self.rfile.read(n).decode()
            b64 = data.split(',', 1)[1] if ',' in data else data
            with open(os.path.join(SHOTS, name + '.jpg'), 'wb') as f:
                f.write(base64.b64decode(b64))
            self.send_response(200); self.end_headers(); self.wfile.write(b'ok')
        else:
            self.send_response(404); self.end_headers()

    def log_message(self, *a):
        pass

http.server.ThreadingHTTPServer(('127.0.0.1', int(sys.argv[1]) if len(sys.argv) > 1 else 8123), H).serve_forever()
