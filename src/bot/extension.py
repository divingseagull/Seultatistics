from discord.ext import commands


class Extension(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="load")
    @commands.is_owner()
    async def load(self, ext: str):
        await self.bot.load_extension(ext)

    @commands.command(name="unload")
    @commands.is_owner()
    async def unload(self, ext: str):
        await self.bot.unload_extension(ext)

    @commands.command(name="reload")
    @commands.is_owner()
    async def reload(self, ext: str):
        await self.bot.reload_extension(ext)


async def setup(bot: commands.Bot):
    await bot.add_cog(Extension(bot))
