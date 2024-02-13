#! /usr/bin/env python3

import os
from enum import Enum

import nextcord
from nextcord.ext import commands

from ..utils import config as _config
from ..utils import logger as _logger


config = _config.Config(f"config.json")
logger = _logger.Logger(config.get_data()['bot']['log'])

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
    owner_ids=config.get_data()['bot']['owner_ids'],
    command_prefix=config.get_data()['bot']['command_prefix'],
    intents=_intents
)


class _TokenStorageType(Enum):
    SYS_ENV = "SYS_ENV"
    TEXT_FILE = "TEXT_FILE"


def _load_extensions():
    for (dirpath, dirnames, filenames) in os.walk("src"):
        if dirpath.endswith("__pycache__"):
            continue

        for filename in filenames:
            if filename == "__init__.py":
                continue

            extension_path = f"{dirpath}/{filename}".removesuffix(".py").replace('/', '.')

            if extension_path in config.get_data()['extensions']['disabled']:
                logger.write(f"Skipping {extension_path}: (disabled extension)",
                             log_level=_logger.LogLevel.INFO)

            if extension_path in config.get_data()['extensions']['not_extension']:
                continue

            bot.load_extension(extension_path)
            logger.write(f"Extension loaded : {extension_path}",
                         log_level=_logger.LogLevel.INFO)


def _get_token() -> str:
    storage_type = config.get_data()['bot']['token']['storage_type']
    token_path = config.get_data()['bot']['token']['path']
    token = str()
    match storage_type:
        case _TokenStorageType.SYS_ENV.value:
            token = os.environ[token_path]
        case _TokenStorageType.TEXT_FILE.value:
            with open(token_path, 'r', encoding='utf-8') as token_io:
                token = token_io.read().strip()
        case _:
            raise ValueError(f"Invalid storage type: {storage_type}")

    return token


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
    _load_extensions()
    bot.run(_get_token())
