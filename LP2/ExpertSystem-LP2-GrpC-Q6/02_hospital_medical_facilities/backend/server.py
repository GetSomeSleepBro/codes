from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import json
import os


PORT = 8000
ROOT = Path(__file__).resolve().parents[1]
FRONTEND = ROOT / "frontend"


def evaluate(data):
    """Apply hospital triage rules."""
    fever = data.get("fever")
    breathing = data.get("breathing")
    pain = data.get("pain")
    injury = data.get("injury")

    # Breathing issues and major injuries should be treated urgently.
    if breathing == "yes" or injury == "major":
        return {
            "decision": "Emergency care required",
            "reason": "Breathing difficulty or major injury can become serious quickly."
        }

    # Severe pain or high fever needs doctor attention soon.
    if pain == "severe" or fever == "high":
        return {
            "decision": "Priority doctor consultation",
            "reason": "The symptoms are significant and should be checked by a doctor."
        }

    # Minor injury can usually be handled by first aid.
    if injury == "minor":
        return {
            "decision": "First aid and observation",
            "reason": "Minor injury usually needs cleaning, dressing, and monitoring."
        }

    return {
        "decision": "General outpatient visit",
        "reason": "The symptoms appear stable and can be handled through normal consultation."
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

