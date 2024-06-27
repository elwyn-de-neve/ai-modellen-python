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

response = client.images.generate(
  model="dall-e-3",
  prompt=prompt,
  n=1,
  size="1024x1024"
)

print(response.data[0].url)
