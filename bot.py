import discord
import random

# This is a simple Discord bot that sends a random meme image when a user types !meme in the chat.
MEME_URLS = [
   "https://i.imgur.com/abc123.jpg",  # Example URL, replace with real image links
    "https://i.imgur.com/def456.jpg",
    "https://i.imgur.com/ghi789.jpg",
    "https://i.imgur.com/jkl012.jpg",
    "https://i.imgur.com/mno345.jpg"
]

# Function to get a random meme URL
def get_meme():
    return random.choice(MEME_URLS)
  
# Define the Discord client
class MyClient(discord.Client):
  # This is the client that will handle events
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))
    # This function is called when the bot is ready and logged in.
  async def on_message(self, message):
    if message.author == self.user:
      return
    if message.content.startswith('!meme'):
      await message.channel.send(get_meme())

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('TOKEN CODE') 

# The token in this example is a placeholder and should not be used.
# Make sure to download the discord.py library and replace 'TOKEN CODE' with your actual bot token.
