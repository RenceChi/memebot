import discord
import random

MEME_URLS = [
    "https://media.discordapp.net/attachments/825010473954574369/1405918383484174479/images3.jpg?ex=68a09307&is=689f4187&hm=6fe4d3ae55f98f643cda5a091b9fabc29b4550c5b154c98456de2fab865c3e2f&=&format=webp",
    "https://media.discordapp.net/attachments/825010473954574369/1405918383748157672/images4.jpg?ex=68a09307&is=689f4187&hm=b21a71f5b347a30a4e869230255d3e57c2606a2ec720550701de58ee23269604&=&format=webp",
    "https://media.discordapp.net/attachments/825010473954574369/1405918383958134855/images.jpg?ex=68a09307&is=689f4187&hm=77c61c5adc6a67d6b4399ae60fd1d4839aa011a3ace7c5aa5cca5e31c1a2cd29&=&format=webp",
    "https://media.discordapp.net/attachments/825010473954574369/1405918384176234506/images_1.jpg?ex=68a09307&is=689f4187&hm=ae318eded24a1b49fb66933d5d655fb710ae50c82614bdd20c03b0ed0d097dbd&=&format=webp",
    "https://media.discordapp.net/attachments/825010473954574369/1405918384402468924/images_2.jpg?ex=68a09307&is=689f4187&hm=5908606dab79bb51b3cde1b2af2a767ffb8cc0f4b3e7bfce30fca124c1172c75&=&format=webp"
]
def get_meme():
    return random.choice(MEME_URLS)

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))
  async def on_message(self, message):
    if message.author == self.user:
      return
    if message.content.startswith('!meme'):
      await message.channel.send(get_meme())

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTQwNTg0OTQ3MDYyOTA1MjQ0Ng.GcDEFf.uA7zJNOXZMj24PKfjBENeTRk0eLOZLtZtrCQnY') # Replace with your own token.

# Note: Make sure to keep your token secure and do not share it publicly.
# The token in this example is a placeholder and should not be used.

# To run this bot, you need to install the discord.py library and have a valid bot token.