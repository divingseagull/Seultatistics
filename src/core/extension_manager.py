from nextcord.ext import commands
from ..core.bot import bot


class CoreExtensionManager(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.group(name="ext")
    async def extension_(self, ctx: commands.Context):
        pass

    @extension_.command(name='load')
    async def extension_load(self, ctx: commands.Context, extension: str):
        bot.load_extension(extension)
        await ctx.send(f'Extension loaded: `{extension}`')

    @extension_.command(name='unload')
    async def extension_unload(self, ctx: commands.Context, extension: str):
        bot.unload_extension(extension)
        await ctx.send(f'Extension unloaded: `{extension}`')

    @extension_.command(name='reload')
    async def extension_reload(self, ctx: commands.Context, extension: str):
        bot.reload_extension(extension)
        await ctx.send(f'Extension reloaded: `{extension}`')

    @extension_.command(name='list')
    async def extension_list(self, ctx: commands.Context):
        indent = '\n    '
        await ctx.send(f"```[\n"
                       f"    {indent.join(self.bot.extensions.keys())}"
                       f"\n]```")


def setup(bot: commands.Bot):
    bot.add_cog(CoreExtensionManager(bot))
