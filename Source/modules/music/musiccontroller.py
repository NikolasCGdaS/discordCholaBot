from discord.ext import commands
from .musicservice import MusicService

class MusicController(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.service = MusicService()

    @commands.command(name="play")
<<<<<<< HEAD
    async def play(self, ctx, *, query: str):
        await self.service.play_music(ctx, query)
    
=======
    async def play(self, ctx, *, url: str):
        """Toca uma música pelo link."""
        await self.service.play_music(ctx, url)

>>>>>>> a17bb87cd98ccfe0725622ed89470b83f4a4067f
    @commands.command(name="pause")
    async def pause(self, ctx):
        await self.service.pause(ctx)

    @commands.command(name="resume")
    async def resume(self, ctx):
        await self.service.resume(ctx)

    @commands.command(name="stop")
    async def stop(self, ctx):
        await self.service.stop(ctx)
<<<<<<< HEAD
    
    @commands.command(name="queue")
    async def queue(self, ctx):
        await self.service.queue(ctx)

    @commands.command(name="skip")
    async def skip(self, ctx):
        await self.service.skip(ctx)

=======
>>>>>>> a17bb87cd98ccfe0725622ed89470b83f4a4067f


async def setup(bot):
    await bot.add_cog(MusicController(bot))
