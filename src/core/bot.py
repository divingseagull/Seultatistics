#! /usr/bin/env python3

from nextcord.ext import commands
from ..utils import config as _config


config = _config.Config(f"config.json")
bot = commands.Bot(
    owner_ids=config.get_owner_ids()
)


class CoreBot(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


def setup(bot: commands):
    bot.add_cog(CoreBot(bot))


if __name__ == "__main__":
    bot.run(config.get_token())
