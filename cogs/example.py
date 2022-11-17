import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio
load_dotenv()

# Example cog class
class example(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

    @discord.app_commands.command(name="hello", description="Basic command to say hello")
    async def introduce(self, interaction: discord.Interaction, name: str):
        # Defer to make sure command can finish before Interaction token expires
        await interaction.response.defer()
        await interaction.followup.send(f"Hello {name}!")

async def setup(client):
    await client.add_cog(example(client), guild=discord.Object(id=os.getenv("GUILD_ID")))   