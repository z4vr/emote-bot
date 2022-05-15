import discord
import util.config.config as config

prefix = "e!"

cfg = config.Config("./config.yml")

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

intents = discord.Intents.default()
intents.messages = True
client = MyClient(intents=intents)
client.run(cfg.token)