import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    data = request.data
    print("Received data length:", len(data))
    return jsonify({"response": "Hello! I got your audio."})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    @app.route("/", methods=["GET"])
def home():
    return "Server is running!"


