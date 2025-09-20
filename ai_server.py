import openai

openai.api_key = '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'

client = openai.OpenAI()
response = client.chat(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response['choices'][0]['message']['content'])
