from nextcord.ext import commands

from ..core.bot import logger
from ..utils.logger import LogLevel


class CoreExtensionManager(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.group(name="ext")
    async def extension_(self, ctx: commands.Context):
        pass

    @extension_.command(name='load')
    async def extension_load(self, ctx: commands.Context, extension: str):
        self.bot.load_extension(extension, package="src")
        logger.write(f"Extension loaded: src{extension}", log_level=LogLevel.INFO)
        await ctx.send(f'Extension loaded: `src{extension}`')

    @extension_.command(name='unload')
    async def extension_unload(self, ctx: commands.Context, extension: str):
        self.bot.unload_extension(extension, package="src")
        logger.write(f"Extension unloaded: src{extension}", log_level=LogLevel.INFO)
        await ctx.send(f'Extension unloaded: `src{extension}`')

    @extension_.command(name='reload')
    async def extension_reload(self, ctx: commands.Context, extension: str):
        self.bot.reload_extension(extension, package="src")
        logger.write(f"Extension reloaded: src{extension}", log_level=LogLevel.INFO)
        await ctx.send(f'Extension reloaded: `src{extension}`')

    @extension_.command(name='list')
    async def extension_list(self, ctx: commands.Context):
        indent = '\n    '
        await ctx.send(f"```[\n"
                       f"    {indent.join(self.bot.extensions.keys())}"
                       f"\n]```")


def setup(bot: commands.Bot):
    bot.add_cog(CoreExtensionManager(bot))
