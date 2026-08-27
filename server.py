import http.server
import socketserver
import json
import os
import sys
from fast_agent import run_fast_admission_agent

DEFAULT_PORT = 8000

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOCAL_STITCH_DIR = os.path.join(BASE_DIR, "stitch_ai_admission_os")
DESKTOP_STITCH_DIR = r"C:\Users\Atharva\Desktop\stitch_ai_admission_os\stitch_ai_admission_os"

STITCH_DIR = LOCAL_STITCH_DIR if os.path.exists(LOCAL_STITCH_DIR) else DESKTOP_STITCH_DIR

# Terminal Colors for Live Presentation
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"
RESET = "\033[0m"

class AdmissionOSHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        clean_path = self.path.split('?')[0]

        if clean_path == "/" or clean_path == "/index.html":
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            file_path = os.path.join(STITCH_DIR, "conversational_intake_ai_admission_os", "code.html")
            with open(file_path, "rb") as f:
                self.wfile.write(f.read())
            return
        
        elif clean_path == "/matched":
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            file_path = os.path.join(STITCH_DIR, "matched_colleges_ai_admission_os", "code.html")
            with open(file_path, "rb") as f:
                self.wfile.write(f.read())
            return

        elif clean_path == "/auto-apply":
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            file_path = os.path.join(STITCH_DIR, "auto_apply_demo_ai_admission_os", "code.html")
            with open(file_path, "rb") as f:
                self.wfile.write(f.read())
            return

        elif clean_path == "/reviews":
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            file_path = os.path.join(STITCH_DIR, "academic_precision", "code.html")
            with open(file_path, "rb") as f:
                self.wfile.write(f.read())
            return

        super().do_GET()

    def do_POST(self):
        clean_path = self.path.split('?')[0]

        if clean_path == "/api/process":
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode('utf-8'))
                query = data.get('query', '')
                
                print(f"\n{BOLD}{CYAN}==================================================={RESET}")
                print(f"{BOLD}{MAGENTA}[HTTP POST /api/process]{RESET} Received Student Prompt: '{query}'")
                print(f"{BOLD}{CYAN}==================================================={RESET}")
                print(f"{YELLOW}[1/3] PROFILE AGENT:{RESET} Extracting structured constraints...")
                print(f"{YELLOW}[2/3] DISCOVERY AGENT:{RESET} Searching college cutoff databases...")
                print(f"{YELLOW}[3/3] REVIEW AGENT:{RESET} Analyzing student sentiment & placement reviews...")
                
                agent_result = run_fast_admission_agent(query)
                
                print(f"{GREEN}[SUCCESS] Agent Execution Completed! Returning Payload.{RESET}\n")

            except Exception as e:
                print(f"\033[91m[API Error] {e}\033[0m")
                agent_result = {"error": str(e)}

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(agent_result).encode('utf-8'))
            return

        super().do_POST()

def start_server():
    socketserver.TCPServer.allow_reuse_address = True
    ports_to_try = [DEFAULT_PORT, 8080, 8001, 5000]
    
    for port in ports_to_try:
        try:
            httpd = socketserver.TCPServer(("", port), AdmissionOSHandler)
            print(f"{BOLD}{GREEN}Admission OS Web Server running at http://localhost:{port}{RESET}")
            print(f"Serving files from: {STITCH_DIR}")
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("\nStopping server.")
            break
        except OSError as e:
            print(f"{YELLOW}Port {port} unavailable ({e}), trying next port...{RESET}")

if __name__ == "__main__":
    start_server()
