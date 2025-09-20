from flask import Flask, request, jsonify
import io
import speech_recognition as sr

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():
    audio_bytes = request.data
    print(f"Received {len(audio_bytes)} bytes")

    audio_file = io.BytesIO(audio_bytes)
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)
        return jsonify({"text": text})
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
