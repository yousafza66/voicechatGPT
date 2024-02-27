from openai import OpenAI
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

text= completion.choices[0].message.content


response = client.audio.speech.create(
    model="tts-1",
    voice="shimmer",
    input= text,
)

response.stream_to_file("output.mp3")
