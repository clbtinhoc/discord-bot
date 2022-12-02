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

from typing import Dict
from utility import Cog, setup_cog, async_get_json_data, async_save_json_data, Embed
from discord.ext import commands

default_level_to_increase = 1
default_level_to_handle = 0

class Level(Cog):
  def handle_exp_and_level(self, user_id: int, user_ranking_data: Dict, exp_to_handle: int = default_level_to_increase, lvl_to_handle: int = default_level_to_handle) -> bool:
    exp = user_ranking_data["exp"]
    lvl = user_ranking_data["level"]
    handled_exp = exp + exp_to_handle
    new_lvl = handled_exp // 10

    if new_lvl > lvl or lvl_to_handle:
      user_ranking_data = {
        "exp": 0,
        "level": new_lvl + lvl_to_handle
      }
    else:
      user_ranking_data["exp"] = handled_exp
    return (new_lvl > lvl), user_ranking_data
  
  
  # Increase user's total exp by 'default_level_to_increase' and handle it
  @commands.Cog.listener()
  async def on_message(self, message):
    # Check whether the message author is not the bot
    if message.author.bot:
      return

    author_id = message.author.id
    ranking_data = await async_get_json_data("data/ranking.json")
    user_ranking_data = ranking_data.setdefault(str(author_id), {
      "exp": 0,
      "level": 1
    })
    handled_user_ranking_data = self.handle_exp_and_level(author_id, user_ranking_data)

    # If leveled up
    if handled_user_ranking_data[0]:
      await message.channel.send(embed=Embed(
        "🥳 LEVELED UP!",
        "GREEN",
        f"{message.author.mention} has afegege just leveled up to **{handled_user_ranking_data[1]['level']}**!"
      ))
    
    # Save data
    ranking_data[str(author_id)] = handled_user_ranking_data[1]
    await async_save_json_data("data/ranking.json", ranking_data)

setup = setup_cog(Level)
