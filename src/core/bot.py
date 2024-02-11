#! /usr/bin/env python3

import os

import nextcord
from nextcord.ext import commands

from ..utils import config as _config
from ..utils import logger as _logger


config = _config.Config(f"config.json")
logger = _logger.Logger(config.get_log_config())

_intents = nextcord.Intents(
    emojis_and_stickers=True,
    guild_messages=True,
    guild_reactions=True,
    guild_typing=True,
    members=True,
    message_content=True,
    reactions=True,
    scheduled_events=True,
    voice_states=True,
    webhooks=True,
)
bot = commands.Bot(
    owner_ids=config.get_owner_ids(),
    command_prefix=config.get_bot_config()["command_prefix"],
    intents=_intents
)


class CoreBot(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        # _load_extensions()
        logger.write(f"Ready!", log_level=_logger.LogLevel.INFO)


def setup(bot: commands):
    bot.add_cog(CoreBot(bot))


if __name__ == "__main__":
    core_extensions = [
        "bot",
        "extension_manager"
    ]
    for core_ext in core_extensions:
        bot.load_extension(f"src.core.{core_ext}")

    bot.run(config.get_token())
