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

from typing import Union, Any
import json
import aiofiles
from inspect import cleandoc
from os import getenv, path, remove, listdir
from discord import (
    Embed as OriginalEmbed,
    Object
)
from discord.ext.commands import Cog as OriginalCog

OLD_COLORS = {
    "LFTROQ": "#ffc0cb",
    "RED": "#ff0000",
    "GREEN": "#00ff00",
    "BLUE": "#0000ff",
    "YELLOW": "#ffff00",
    "PINK": "#ff00ff",
    "PURPLE": "#8A2BE2",
    "CYAN": "#00ffff",
    "WHITE": "#ffffff",
    "BLACK": "#000000",
    "ORANGE": "#ffa500",
    "BROWN": "#a52a2a",
    "GREY": "#808080",
    "DARK_GREY": "#404040",
    "LIGHT_GREY": "#c0c0c0",
    "DARK_GREEN": "#006400",
    "LIGHT_GREEN": "#90ee90",
    "DARK_BLUE": "#00008b",
    "LIGHT_BLUE": "#add8e6",
    "DARK_PURPLE": "#800080",
    "LIGHT_PURPLE": "#e6e6fa",
    "DARK_CYAN": "#008b8b",
    "LIGHT_CYAN": "#00ffff",
    "DARK_RED": "#8b0000",
    "LIGHT_RED": "#ffb6c1",
    "DARK_ORANGE": "#ff8c00",
    "LIGHT_ORANGE": "#ffa07a",
    "DARK_BROWN": "#a52a2a",
    "LIGHT_BROWN": "#deb887",
    "DARK_GOLD": "#ffd700",
    "LIGHT_GOLD": "#ffefd5",
    "DARK_SILVER": "#c0c0c0",
    "LIGHT_SILVER": "#e0e0e0",
    "DARK_PINK": "#ff1493",
    "LIGHT_PINK": "#ffb6c1",
    # Down here are legacy ones (Used for backwards compatibility / Usually not used because of their deprecations)
    "C_RED": 0xff0000,
    "C_GREEN": 0x00ff00,
    "C_BLUE": 0x0000ff,
    "C_YELLOW": 0xffff00,
    "C_PURPLE": 0xff00ff,
    "C_CYAN": 0x00ffff,
    "C_WHITE": 0xffffff,
    "C_BLACK": 0x000000
}

COLORS = {
    "TEAL": 0x1abc9c,
    "DARK_TEAL": 0x11806a,
    "BRAND_GREEN": 0x57f287,
    "GREEN": 0x2ecc71,
    "DARK_GREEN": 0x1f8b4c,
    "BLUE": 0x3498db,
    "DARK_BLUE": 0x206694,
    "PURPLE": 0x9b59b6,
    "DARK_PURPLE": 0x71368a,
    "MAGENTA": 0xe91e63,
    "DARK_MAGENTA": 0xad1457,
    "GOLD": 0xf1c40f,
    "DARK_GOLD": 0xc27c0e,
    "ORANGE": 0xe67e22,
    "DARK_ORANGE": 0xa84300,
    "BRAND_RED": 0xed4245,
    "RED": 0xe74c3c,
    "DARK_RED": 0x992d22,
    "LIGHTER_GREY": 0x95a5a6,
    "LIGHTER_GRAY": 0x95a5a6,
    "DARK_GREY": 0x607d8b,
    "DARK_GRAY": 0x607d8b,
    "LIGHT_GREY": 0x979c9f,
    "LIGHT_GRAY": 0x979c9f,
    "DARKER_GREY": 0x546e7a,
    "DARKER_GRAY": 0x546e7a,
    "OG_BLURPLE": 0x7289da,
    "BLURPLE": 0x5865f2,
    "GREYPLE": 0x99aab5,
    "DARK_THEME": 0x36393f,
    "FUCHSIA": 0xeb459e,
    "YELLOW": 0xfee75c
}


def get_color(color: str, type_to_convert_to: str = "hex") -> int:
  type_to_convert_to = type_to_convert_to.lower()
  if color in COLORS:
    color = COLORS[color]
    color = str(color).strip("#")
    return int(color, 0)

  color = color.strip("#")

  types = {
    "hex": 16,
    16: 16,
    "dec": 10,
    10: 10
  }

  try:
    return int(color, types[type_to_convert_to])
  except:
    return int("ff0000", 16)


def get_json_data(directory: str) -> Union[dict, set, list, tuple]:
  with open(directory, mode="r", encoding="utf-8") as file:
    return json.loads(file.read())


def save_json_data(directory: str, data: Union[dict, set, list, tuple]) -> None:
  with open(directory, mode="w", encoding="utf-8") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)


async def async_get_json_data(directory: str) -> Union[dict, set, list, tuple]:
  async with aiofiles.open(directory, mode="r", encoding="utf-8") as file:
    return json.loads(await file.read())


async def async_save_json_data(directory: str, data: Union[dict, set, list, tuple]) -> None:
  async with aiofiles.open(directory, mode="w", encoding="utf-8") as file:
    await file.write(json.dumps(data, indent=2, ensure_ascii=False))


class Embed(OriginalEmbed):
  def __init__(self, title: str, color: Any, description: str, *args, **kwargs):
    super().__init__(
      title=title,
      color=get_color(color),
      description=cleandoc(description),
      *args,
      **kwargs
    )
    self.set_footer(
      text="Created by hanhdoo#2225 with 💖."
    )

class Cog(OriginalCog):
  def __init__(self, client, *args, **kwargs) -> None:
    self.client = client
    super().__init__(*args, **kwargs)

  async def cog_load(self):
    print(f"🐧 Loaded successfully: {self.qualified_name}!")


def setup_cog(cog: Cog):
  async def setup(client):
    await client.add_cog(cog(client), guild=Object(id=getenv("GUILD_ID")))
  return setup


def get_files(directory: str, exceptions: Union[tuple, list, set] = []) -> list:
  return [
      file for file in listdir(directory) if path.isfile(path.join(directory, file)) and file not in exceptions
  ]


def get_sub_directories(directory: str, exceptions: Union[tuple, list, set] = []) -> list:
  return [
      sub_directory for sub_directory in listdir(directory) if path.isdir(path.join(directory, sub_directory)) and sub_directory not in exceptions
  ]


def delete_file(directory: str) -> None:
  remove(directory)
