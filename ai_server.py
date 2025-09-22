from flask import Flask, request, jsonify
import os
import speech_recognition as sr
import openai

# ====== Config ======
openai.api_key = os.getenv("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")  # put in Render environment

app = Flask(__name__)

@app.route("/")
def home():
    return "sandy loading .loading max iq✅"

@app.route("/upload", methods=["POST"])
def upload_audio():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    filepath = os.path.join("uploads", file.filename)
    os.makedirs("uploads", exist_ok=True)
    file.save(filepath)

    # ===== Speech Recognition =====
    recognizer = sr.Recognizer()
    text = ""
    try:
        with sr.AudioFile(filepath) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)  # Free Google Speech API
    except Exception as e:
        return jsonify({"error": f"Speech recognition failed: {str(e)}"}), 500

    # ===== Call OpenAI GPT =====
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # change to gpt-4 if you have access
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": text}
            ]
        )
        ai_reply = response["choices"][0]["message"]["content"]
    except Exception as e:
        return jsonify({"error": f"OpenAI API failed: {str(e)}"}), 500

    return jsonify({"transcribed_text": text, "ai_reply": ai_reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
