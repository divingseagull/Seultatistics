#! /usr/bin/env python3

import os
import logging

import discord
from discord.ext import commands

from ..utils.config import get_config


bot = commands.Bot(
    command_prefix="?",  # 명령어 접두사
    intents=discord.Intents.default()
)
handler = logging.FileHandler(get_config()['logging']['filename'], 'a')


def _get_token() -> str:
    return os.getenv(get_config()['token_env'])


def _get_core_extensions() -> list[str]:
    core_extensions = []

    for (dirpath, _, filenames) in os.walk("src.bot"):
        dirpath: str

        if dirpath.endswith("__pycache__"):
            continue
        if dirpath.endswith("src/utils"):
            continue

        for filename in filenames:
            filename: str = filename.removesuffix(".py")

            if filename.startswith('_'):
                continue
            if f"{dirpath}/{filename}" in get_config()['extension']['not_extension']:
                continue

            core_extensions.append(f"{dirpath}/{filename}")

    return core_extensions


@bot.command(name='ping')
async def ping(ctx: commands.Context):
    await ctx.send("pong!")


@bot.event
async def on_ready():
    core_extensions = _get_core_extensions()
    for extension in core_extensions:
        await bot.load_extension(extension)


if __name__ == "__main__":
    token = _get_token()

    try:
        bot.run(token)
    except discord.errors.LoginFailure:
        pass
    except TypeError:
        pass
    except KeyboardInterrupt:
        pass
