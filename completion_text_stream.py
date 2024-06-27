import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

# Initialize the OpenAI client with the API key
client = OpenAI(
    api_key=api_key
)

# Ask a question to OpenAI
prompt = input("Ask a question to OpenAI: ")

# Get the response from OpenAI with streaming
stream = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": prompt}
    ],
    stream=True,
)

# Print the output as it streams
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
