from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():
    try:
        data_len = len(request.data)
        print("📥 Got POST with", data_len, "bytes")
        return jsonify({"status": "ok", "received_bytes": data_len})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
