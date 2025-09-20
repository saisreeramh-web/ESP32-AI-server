from flask import Flask, request, jsonify
import speech_recognition as sr
import openai
import io

app = Flask(__name__)

import os
openai.api_key = os.getenv("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")

@app.route('/upload', methods=['POST'])
def upload():
    try:
        # 1. Save audio
        audio_data = request.data
        audio_file = io.BytesIO(audio_data)

        # 2. Recognize speech
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)

        text = recognizer.recognize_google(audio)
        print("🎤 Recognized:", text)

        # 3. Get AI reply
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": text}]
        )
        reply = response.choices[0].message.content

        # 4. Send back real answer
        return jsonify({"response": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



