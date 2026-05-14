from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import json
import os


PORT = 8000
ROOT = Path(__file__).resolve().parents[1]
FRONTEND = ROOT / "frontend"


def evaluate(data):
    """Apply simple expert-system rules and return a decision."""
    sensitivity = data.get("sensitivity")
    frequency = data.get("frequency")
    backup = data.get("backup")
    sharing = data.get("sharing")

    # Highly sensitive data needs strong security first.
    if sensitivity == "high":
        return {
            "decision": "Use restricted encrypted storage",
            "reason": "High sensitivity data should have access control, encryption, and audit logs."
        }

    # Critical backups should be protected even if sensitivity is not high.
    if backup == "critical":
        return {
            "decision": "Use daily backup with version control",
            "reason": "Critical data must be recoverable after accidental deletion or system failure."
        }

    # Shared and frequently used information should be easy to access.
    if sharing == "yes" and frequency == "frequent":
        return {
            "decision": "Use a shared cloud document system",
            "reason": "Frequently shared information needs quick access and controlled collaboration."
        }

    return {
        "decision": "Use normal categorized storage",
        "reason": "The data does not need advanced handling, so organized folders and normal backup are enough."
    }


class Handler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/api/evaluate":
            self.send_error(404)
            return

        # Read the JSON sent by the frontend.
        length = int(self.headers.get("Content-Length", 0))
        data = json.loads(self.rfile.read(length) or b"{}")
        result = evaluate(data)

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(result).encode())


if __name__ == "__main__":
    os.chdir(FRONTEND)
    print(f"Open http://localhost:{PORT}")
    ThreadingHTTPServer(("localhost", PORT), Handler).serve_forever()

