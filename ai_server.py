from flask import Flask, request, jsonify
import openai
import io
import wave

app = Flask(__name__)

# Replace this with your new OpenAI API key
openai.api_key = "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"

@app.route("/upload", methods=["POST"])
def upload():
    audio_bytes = request.data
    print(f"Received audio of length: {len(audio_bytes)} bytes")

    # Save audio temporarily as a WAV file
    wav_file = "temp.wav"
    with wave.open(wav_file, "wb") as wf:
        wf.setnchannels(1)        # mono
        wf.setsampwidth(2)        # 16-bit
        wf.setframerate(16000)    # 16 kHz
        wf.writeframes(audio_bytes)

    # Send audio to OpenAI for transcription
    try:
        with open(wav_file, "rb") as f:
            transcription = openai.Audio.transcriptions.create(
                model="whisper-1",
                file=f
            )

        # Extract the transcribed text
        user_text = transcription["text"]
        print(f"User said: {user_text}")

        # Generate a direct answer using GPT
        completion = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an assistant that gives direct, precise answers."},
                {"role": "user", "content": user_text}
            ]
        )

        answer = completion.choices[0].message["content"]
        print(f"AI answer: {answer}")

        return jsonify({"response": answer})

    except Exception as e:
        print("Error:", e)
        return jsonify({"response": "Error processing audio"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
