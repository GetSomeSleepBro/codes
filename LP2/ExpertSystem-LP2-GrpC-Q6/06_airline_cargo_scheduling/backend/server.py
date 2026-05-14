from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import json
import os


PORT = 8000
ROOT = Path(__file__).resolve().parents[1]
FRONTEND = ROOT / "frontend"


def evaluate(data):
    """Apply airline and cargo scheduling rules."""
    urgency = data.get("urgency")
    weather = data.get("weather")
    capacity = data.get("capacity")
    cargo = data.get("cargo")

    # Stormy weather can make flights unsafe.
    if weather == "storm":
        return {
            "decision": "Delay and reschedule",
            "reason": "Storm conditions can affect flight safety."
        }

    # Emergency medical cargo should get the fastest available slot.
    if urgency == "emergency" or cargo == "medical":
        return {
            "decision": "Assign priority flight slot",
            "reason": "Emergency or medical cargo should be scheduled before normal cargo."
        }

    # Full capacity means the cargo must move to another flight.
    if capacity == "full":
        return {
            "decision": "Move cargo to next available flight",
            "reason": "The selected flight does not have enough capacity."
        }

    if cargo == "fragile":
        return {
            "decision": "Schedule with special handling",
            "reason": "Fragile cargo needs careful loading and handling instructions."
        }

    return {
        "decision": "Schedule normally",
        "reason": "Weather and capacity are acceptable for normal scheduling."
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

