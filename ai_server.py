from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Set API key from environment variable
openai.api_key = os.getenv("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")

@app.route("/")
def home():
    return "✅ SANDY IS RUNNING!!"

@app.route("/upload", methods=["POST"])
def upload():
    try:
        data = request.data
        if not data:
            return jsonify({"error": "No audio data received"}), 400

        # For now, just treat the raw bytes length as input
        text_input = f"Received {len(data)} bytes of audio. Summarize this as a greeting."

        # Call OpenAI GPT
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": text_input}
            ],
            max_tokens=100
        )

        reply = response["choices"][0]["message"]["content"].strip()

        return jsonify({"status": "ok", "response": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
