import os
from flask import Flask, jsonify
from src.api import fetch_pokemon

app = Flask(__name__)

@app.route("/")
def index():
    data = fetch_pokemon()
    if data:
        return jsonify({
            "first_pokemon": data["results"][0]["name"]
        })
    else:
        return jsonify({"error": "Failed to fetch Pokémon data"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

