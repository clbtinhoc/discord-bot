import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()

# Client class
class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="$", intents=discord.Intents.default())

    async def on_ready(self):
        print(f"{self.user} has connected to Discord")

    async def setup_hook(self):
        await self.load_extension(f"cogs.example")

        # Syncing to prevent discord using outdated commands
        await self.tree.sync(guild=discord.Object(id=os.getenv("GUILD_ID")))

client = Client()
client.run(os.getenv("TOKEN")) 