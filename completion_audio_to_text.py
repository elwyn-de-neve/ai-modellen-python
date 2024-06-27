import os
from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

# Initialize the OpenAI client with the API key
client = OpenAI(
    api_key=api_key
)

audio_file = open("speech.mp3", "rb")
transcription_response = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file,
    # response_format="verbose_json",
    # timestamp_granularities=["segment"] # ["word"]
)

# Get the transcribed text
prompt = transcription_response.json()

# Get the response from OpenAI
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": prompt}
    ],
)

# Save the output in a variable
output = response.choices[0].message.content

speech_file_path = Path(__file__).parent / "speech_out.mp3"
with client.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice="alloy",
        input=output,
) as response:
    response.stream_to_file(speech_file_path)
