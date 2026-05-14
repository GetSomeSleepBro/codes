from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import json
import os


PORT = 8000
ROOT = Path(__file__).resolve().parents[1]
FRONTEND = ROOT / "frontend"


def evaluate(data):
    """Apply employee performance rules."""
    attendance = data.get("attendance")
    quality = data.get("quality")
    targets = data.get("targets")
    teamwork = data.get("teamwork")

    # Strong work quality and high target completion indicate excellent performance.
    if quality == "good" and targets == "high" and attendance == "good":
        return {
            "decision": "Excellent performance",
            "reason": "The employee has good attendance, high targets, and good work quality."
        }

    # Poor attendance or quality needs improvement even if other areas are acceptable.
    if attendance == "poor" or quality == "poor":
        return {
            "decision": "Needs improvement",
            "reason": "Attendance and work quality are core performance factors."
        }

    # Good teamwork and medium/high targets show reliable performance.
    if teamwork == "good" and targets in ("medium", "high"):
        return {
            "decision": "Good performance",
            "reason": "The employee contributes well and meets useful work targets."
        }

    return {
        "decision": "Average performance",
        "reason": "The employee meets basic expectations but can improve in some areas."
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

