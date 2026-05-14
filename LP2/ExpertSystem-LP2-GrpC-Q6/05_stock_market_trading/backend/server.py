from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import json
import os


PORT = 8000
ROOT = Path(__file__).resolve().parents[1]
FRONTEND = ROOT / "frontend"


def evaluate(data):
    """Apply simple stock trading rules."""
    trend = data.get("trend")
    news = data.get("news")
    risk = data.get("risk")
    volume = data.get("volume")

    # This is a classroom rule engine, not real financial advice.
    if trend == "up" and news == "positive" and risk != "high":
        return {
            "decision": "Buy",
            "reason": "Positive news and upward trend suggest a favorable condition."
        }

    if trend == "down" or news == "negative":
        return {
            "decision": "Sell or avoid",
            "reason": "Negative trend or news increases the chance of loss."
        }

    if risk == "high" or volume == "low":
        return {
            "decision": "Hold",
            "reason": "High risk or low volume makes the trade uncertain."
        }

    return {
        "decision": "Hold and monitor",
        "reason": "The signals are mixed, so waiting for confirmation is safer."
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

