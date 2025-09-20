from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    try:
        data = request.data
        print("Received audio data length:", len(data))
        # For testing, you can save the audio temporarily
        with open("audio.raw", "wb") as f:
            f.write(data)
        # Respond with a mock AI text for now
        response_text = "AI says: Hello! I received your audio."
        return jsonify({"response": response_text})
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
