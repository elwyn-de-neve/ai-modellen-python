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

# Get the response from OpenAI
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

# Save the output in a variable
output = response.choices[0].message.content

# Print the output
print(output)
