from discord import Object, Intents
from discord.ext import commands
from os import getenv, system
from dotenv import load_dotenv
from utility import get_json_data, get_files
from subprocess import run

load_dotenv()

class Client(commands.Bot):
  def __init__(self):
    self.configurations = get_json_data("data/configuration.json")
    self.prefix = self.configurations["prefix"]
    self.cogs_not_to_load = self.configurations["cogs_not_to_load"]

    intents = Intents.default()
    intents.message_content = True

    super().__init__(
      command_prefix=self.prefix,
      intents=intents
    )

  async def on_ready(self):
      system("pyclean . -q")
      print(f"Bot is ready! Logged in as {self.user}!")

  async def setup_hook(self):
    for cog in get_files("cogs", self.cogs_not_to_load):
      await self.load_extension(f"cogs.{cog[:-3]}")

    # Syncing to prevent discord using outdated commands
    await self.tree.sync(guild=Object(id=getenv("GUILD_ID")))

client = Client()
client.run(getenv("TOKEN"))