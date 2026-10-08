import json
import signal
import sys
from pathlib import Path

from flask import Flask, jsonify

app = Flask(__name__)

DATA_FILE = Path(__file__).parent / "data" / "cookies.json"


def load_cookies():
    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


@app.route("/")
def get_cookies():
    return jsonify(load_cookies())


@app.route("/<int:cookie_id>")
def get_cookie(cookie_id):
    cookies = load_cookies()

    cookie = next(
        (cookie for cookie in cookies if cookie["id"] == cookie_id),
        None
    )

    if cookie is None:
        return jsonify({"message": "Cookie introuvable"}), 404

    return jsonify(cookie)


def handle_sigterm(signum, frame):
    print("SIGTERM reçu, arrêt du backend")
    sys.exit(0)


signal.signal(signal.SIGTERM, handle_sigterm)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
