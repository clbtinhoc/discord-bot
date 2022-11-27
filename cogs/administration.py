#                  ;)
#         _..._.-;_/
#      .-'     ` (
#     /      ;   \
#    ;.' ;`  ,;  ;
#   .'' ``. (  \ ;
#  / L_ _f t r oq\
#  \/|` '|\/;; <;/
# ((; \_/  (()       lftroq?_NooberrUwU
#      "

import discord
from discord.ext import commands
from discord.ext.commands import (
  ExtensionAlreadyLoaded,
  ExtensionError,
)
from utility import Cog, setup_cog, Embed

class Administration(Cog):
  @discord.app_commands.command(name="reload", description="Reload the bot.")
  async def reload(self, interaction: discord.Interaction):
    await interaction.response.defer()
    result = ""
    color = "DARK_GRAY"
    for cog in list(self.client.extensions.keys()):
      try:
        await self.client.unload_extension(cog)
        await self.client.load_extension(cog)
        result += f"✅ Reloaded successfully: **{cog}**!\n"
      except Exception as e:
        color = "RED"
        result += f"⛔ Reloaded unsuccessfully: **{cog}**! ({e})\n"
    await interaction.followup.send(embed=Embed(
      "Reloading process:",
      color,
      result
    ))

setup = setup_cog(Administration)