import discord
import os
import openai
from dotenv import load_dotenv

load_dotenv()

discord_token = os.getenv("DISCORD_TOKEN")
openai.api_key = os.getenv("OPENAI_API_KEY")
model_engine = "text-davinci-002"

# Create a GPT instance to be used for generating messages
def ask_gpt(message):
  prompt = f'{message.author} said "{message.content}"\nAI said:'
  completions = openai.Completion.create(engine=model_engine,prompt=prompt,max_tokens=60)
  message_out = completions.choices[0].text
  return message_out

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    # Print the message in the console
    print(message.content)

    # Ask GPT
    response = ask_gpt(message)

    # Send response message
    await message.channel.send(response)

client.run(discord_token)