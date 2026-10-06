import signal
import sys

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return {"message": "Backend opérationnel"}


def handle_sigterm(signum, frame):
    print("SIGTERM reçu, arrêt du backend")
    sys.exit(0)


signal.signal(signal.SIGTERM, handle_sigterm)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)