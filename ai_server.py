from flask import Flask, request, jsonify
import openai
import speech_recognition as sr
import io

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = "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"

@app.route("/upload", methods=["POST"])
def upload_audio():
    # Get raw audio data from ESP32
    audio_data = request.data
    if not audio_data:
        return jsonify({"error": "No audio received"}), 400

    # Convert bytes to an audio file for recognition
    audio_file = io.BytesIO(audio_data)
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)
            print("Recognized text:", text)
    except Exception as e:
        return jsonify({"error": f"Speech recognition failed: {str(e)}"}), 500

    # Send text to OpenAI for response
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": text}]
        )
        ai_text = response.choices[0].message.content
        print("AI response:", ai_text)
    except Exception as e:
        return jsonify({"error": f"OpenAI request failed: {str(e)}"}), 500

    return jsonify({"response": ai_text})

if __name__ == "__main__":
    # Run on all interfaces (Render) on port 5000
    app.run(host="0.0.0.0", port=5000)

