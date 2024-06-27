import os
import time

from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

# Initialize the OpenAI client with the API key
client = OpenAI(
    api_key=api_key
)

my_assistant = client.beta.assistants.create(
    instructions="You are a helpful assistant that can answer questions about any topic.",
    name="Assistant",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4o",
)

thread = client.beta.threads.create()

prompt = input("Ask a question to the assistant: ")

thread_message = client.beta.threads.messages.create(
    thread.id,
    role="user",
    content=prompt,
)

message = client.beta.threads.messages.retrieve(
    message_id=thread_message.id,
    thread_id=thread.id,
)

run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=my_assistant.id,
)

while run.status != "completed":
    run = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )

    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )

    if run.status == "completed":
        print("Run completed!")
        print(messages)
        break

    time.sleep(1)
