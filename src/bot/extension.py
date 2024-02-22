from discord.ext import commands


class Extension(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.group(name="ext")
    @commands.is_owner()
    async def _ext(self, ctx: commands):
        pass

    @_ext.command(name="load", aliases=["l"])
    async def ext_load(self, ctx: commands.Context, ext: str):
        await self.bot.load_extension(ext)
        await ctx.send(f"Loaded")

    @_ext.command(name="unload", aliases=["ul", "u"])
    async def ext_unload(self, ctx: commands.Context, ext: str):
        await self.bot.unload_extension(ext)
        await ctx.send(f"Unloaded")

    @_ext.command(name="reload", aliases=["rl", "r"])
    async def ext_reload(self, ctx: commands.Context, ext: str):
        await self.bot.reload_extension(ext)
        await ctx.send(f"Reloaded")

    @_ext.command(name="list", aliases=["ll"])
    async def ext_list(self, ctx: commands.Context):
        s = "```[\n"
        for ext, _ in self.bot.extensions.items():
            s += f"    {ext}\n"
        s += ']```'
        await ctx.send(s)


async def setup(bot: commands.Bot):
    await bot.add_cog(Extension(bot))
