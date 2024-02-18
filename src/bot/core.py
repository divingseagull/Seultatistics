#! /usr/bin/env python3

import asyncio

import discord
from discord.ext import commands


bot = commands.Bot(
    command_prefix="?",  # 명령어 접두사
    intents=discord.Intents.default()
)


if __name__ == "__main__":
    main()
