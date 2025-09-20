from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Add your new OpenAI API key here
OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY

@app.route('/upload', methods=['POST'])
def upload():
    audio_data = request.data
    print(f"Received {len(audio_data)} bytes of audio")

    # If you want, add SpeechRecognition code to convert audio_data to text
    user_text = "Hello, this is a test"  # Placeholder

    # Send to OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_text}]
    )
    ai_text = response.choices[0].message.content
    print(f"AI says: {ai_text}")
    return jsonify({"response": ai_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
