import http.server
import socketserver
import json
import os
from fast_agent import run_fast_admission_agent

PORT = 8000
STITCH_DIR = r"C:\Users\Atharva\Desktop\stitch_ai_admission_os\stitch_ai_admission_os"

class AdmissionOSHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open(os.path.join(STITCH_DIR, "conversational_intake_ai_admission_os", "code.html"), "rb") as f:
                self.wfile.write(f.read())
            return
        
        elif self.path == "/matched":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open(os.path.join(STITCH_DIR, "matched_colleges_ai_admission_os", "code.html"), "rb") as f:
                self.wfile.write(f.read())
            return

        elif self.path == "/auto-apply":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open(os.path.join(STITCH_DIR, "auto_apply_demo_ai_admission_os", "code.html"), "rb") as f:
                self.wfile.write(f.read())
            return

        elif self.path == "/reviews":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open(os.path.join(STITCH_DIR, "academic_precision", "code.html"), "rb") as f:
                self.wfile.write(f.read())
            return

        super().do_GET()

    def do_POST(self):
        if self.path == "/api/process":
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode('utf-8'))
                query = data.get('query', '')
                print(f"[API] Processing query: {query}")
                agent_result = run_fast_admission_agent(query)
            except Exception as e:
                print(f"[API Error] {e}")
                agent_result = {"error": str(e)}

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(agent_result).encode('utf-8'))
            return

        super().do_POST()

if __name__ == "__main__":
    print(f"🚀 Admission OS Web Server running at http://localhost:{PORT}")
    with socketserver.TCPServer(("", PORT), AdmissionOSHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopping server.")
