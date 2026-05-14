from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import json
import os


PORT = 8000
ROOT = Path(__file__).resolve().parents[1]
FRONTEND = ROOT / "frontend"


def evaluate(data):
    """Apply ticket classification rules."""
    issue = data.get("issue")
    users = data.get("users")
    impact = data.get("impact")

    # Many affected users or high impact means the ticket should be escalated.
    if users == "many" or impact == "high":
        return {
            "decision": "Priority 1 escalation",
            "reason": "The issue affects business work or many users, so it needs urgent handling."
        }

    # Password issues usually have a known standard process.
    if issue == "password":
        return {
            "decision": "Send password reset steps",
            "reason": "Password tickets are common and can usually be solved with standard instructions."
        }

    # Hardware problems often need physical inspection.
    if issue == "hardware":
        return {
            "decision": "Assign to hardware technician",
            "reason": "Hardware issues may require device checking or replacement."
        }

    return {
        "decision": "Assign to level 1 support",
        "reason": "The ticket has normal impact and can start with basic troubleshooting."
    }


class Handler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/api/evaluate":
            self.send_error(404)
            return

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

