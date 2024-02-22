import json
import os

import discord
from discord import TextChannel, VoiceChannel
from discord.ext import commands

from ..utils.data import message_
from ..utils.config import get_config


class Message(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="fetch_history")
    async def fetch_history(self, ctx: commands.Context, target: TextChannel | VoiceChannel, limit: int = 100):
        history = target.history(limit=limit)
        json_data = []
        msg_content = "Collecting history..."
        msg = await ctx.send(msg_content)

        async with ctx.typing():
            async for message in history:
                json_data.append(message_.message_to_dict(message))
        msg_content += "\ndone!"
        await msg.edit(content=msg_content)

        data_dir = f"{get_config()['data']['directory']}/history"
        data_filename = f"{data_dir}/{target.id}.json"
        try:
            os.mkdir(data_dir)
        except FileExistsError:
            pass

        with open(data_filename, "w") as f:
            json.dump(json_data, f)
        msg_content += f"\ndata saved in {data_filename}"
        await msg.edit(content=msg_content)

    @commands.command(name="request_history")
    async def request_history(self, ctx: commands.Context, target: TextChannel | VoiceChannel):
        try:
            file = discord.File(f"{get_config()['data']['directory']}/history/{target.id}.json",
                                      filename=f"{target.id}_history.json")
        except FileNotFoundError:
            await ctx.send("History data not found")
        else:
            await ctx.send(file=file)


async def setup(bot: commands.Bot):
    await bot.add_cog(Message(bot))
