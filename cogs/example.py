from utility import Cog, setup_cog
import discord

class Example(Cog):
  # Your code here
  # Begin
  

  # End

  # EXAMPLE COMMAND
  @discord.app_commands.command(name="hello", description="Đẹp trai bố đời")
  async def introduce(self, interaction: discord.Interaction, name: str):
    # Defer to make sure command can finish before Interaction token expires
    await interaction.response.defer()
    await interaction.followup.send(f"Hello {name}!")

setup = setup_cog(Example)
