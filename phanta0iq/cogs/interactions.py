import disnake; from disnake.ext import commands;
import random
from links.gifs import PAT_GIFS, KISS_GIFS, HUG_GIFS, KICK_GIFS


class Interactions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.user_data = {}

    @commands.slash_command(description="PAT")
    async def pat(self, ctx, user: disnake.User):
        embed = disnake.Embed(title=f'{ctx.author} гладит {user}')
        embed.set_image(url=PAT_GIFS[random.randint(0, len(PAT_GIFS)-1)])
        await ctx.send(user.mention, embed=embed)
    
    @commands.slash_command(description="KISS")
    async def kiss(self, ctx, user: disnake.User):
        embed = disnake.Embed(title=f'{ctx.author} целует {user}')
        embed.set_image(url=KISS_GIFS[random.randint(0, len(KISS_GIFS)-1)])
        await ctx.send(user.mention, embed=embed)
     
    @commands.slash_command(description="HUG")
    async def hug(self, ctx, user: disnake.User):
        embed = disnake.Embed(title=f'{ctx.author} обнимает {user}')
        embed.set_image(url=HUG_GIFS[random.randint(0, len(HUG_GIFS)-1)])
        await ctx.send(user.mention, embed=embed)
    
    @commands.slash_command(description="KICK")
    async def kick(self, ctx, user: disnake.User):
        embed = disnake.Embed(title=f'{ctx.author} бьет {user}')
        embed.set_image(url=KICK_GIFS[random.randint(0, len(KICK_GIFS)-1)])
        await ctx.send(user.mention, embed=embed)

def setup(bot):
    bot.add_cog(Interactions(bot))