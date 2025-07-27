from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # autorise l'accès depuis Netlify ou d'autres domaines

@app.route("/api/greet", methods=["POST"])
def greet():
    data = request.get_json()
    name = data.get("name", "inconnu")
    return jsonify({"message": f"Bonjour, {name} !"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

