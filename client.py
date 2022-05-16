import discord
import logging
import util.config.config as config

log = logging.getLogger(__name__)

prefix = "e!"

cfg = config.Config("./config.yml")

MY_GUILD = discord.Object(id=971921325826379786)

class Client(discord.Client):

    def __init__(self, *, intents: discord.Intents, application_id: int):
        super().__init__(intents=intents, application_id=application_id)

        self.cfg = cfg

    async def on_ready(self) -> None:
        log.info(f'logged in as {self.user}')
        # log the invite link for the bot
        log.info(f'https://discord.com/api/oauth2/authorize?client_id={self.cfg.appid}&scope=bot%20applications.commands&permissions=0')

    async def setup_hook(self):
        # This copies the global commands over to your guild.
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)

    async def start(self) -> None:
        await super().start(cfg.token, reconnect=True)

    @super.tree.command()
    async def hello(interaction: discord.Interaction):
        """Says hello!"""
        await interaction.response.send_message(f'Hi, {interaction.user.mention}')
