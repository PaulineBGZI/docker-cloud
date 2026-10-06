import signal
import sys

from flask import Flask, jsonify

app = Flask(__name__)

cookies = [
    {
        "id": 1,
        "nom": "Chocolat",
        "description": "Cookie moelleux avec des pépites de chocolat.",
        "prix": 2.50
    },
    {
        "id": 2,
        "nom": "Triple chocolat",
        "description": "Cookie au chocolat avec plusieurs types de pépites.",
        "prix": 3.00
    },
    {
        "id": 3,
        "nom": "Caramel",
        "description": "Cookie fondant avec des morceaux de caramel.",
        "prix": 2.80
    },
    {
        "id": 4,
        "nom": "Noisette",
        "description": "Cookie moelleux avec des éclats de noisette.",
        "prix": 2.90
    },
    {
        "id": 5,
        "nom": "Chocolat blanc",
        "description": "Cookie doux avec des morceaux de chocolat blanc.",
        "prix": 2.90
    },
    {
        "id": 6,
        "nom": "Spéculoos",
        "description": "Cookie gourmand au goût de spéculoos.",
        "prix": 3.10
    },
    {
        "id": 7,
        "nom": "Pistache",
        "description": "Cookie fondant avec une touche de pistache.",
        "prix": 3.20
    },
    {
        "id": 8,
        "nom": "Framboise",
        "description": "Cookie sucré avec des morceaux de framboise.",
        "prix": 3.00
    }
]


@app.route("/")
def get_cookies():
    return jsonify(cookies)


def handle_sigterm(signum, frame):
    print("SIGTERM reçu, arrêt du backend")
    sys.exit(0)


signal.signal(signal.SIGTERM, handle_sigterm)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)