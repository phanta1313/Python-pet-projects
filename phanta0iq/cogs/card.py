import disnake; from disnake.ext import commands;

class UserCard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.user_data = {}

    @commands.slash_command(description="добавить очки")
    async def add_points(self, ctx, member: disnake.Member, points: int):
        if member.id not in self.user_data:
            self.user_data[member.id] = 0
        self.user_data[member.id] += points
        await ctx.send(f"Было добавлено {points} очков к {member.mention}. Теперь у него {self.user_data[member.id]} очков.")

    @commands.slash_command(description="отнять очки")
    async def remove_points(self, ctx, member: disnake.Member, points: int):
        if member.id not in self.user_data:
            self.user_data[member.id] = 0
        self.user_data[member.id] -= points
        await ctx.send(f"Было взято {points} очков у {member.mention}. Теперь у него {self.user_data[member.id]} очков.")

    @commands.slash_command(description='узнать свои очки')
    async def card(self, ctx, member: disnake.Member = None):
        if member is None:
            member = ctx.author
        points = self.user_data.get(member.id, 0)
        embed = disnake.Embed(title=f"Карточка {member.name}", description=f"Очки: {points}", color=0x00ff00)
        embed.set_thumbnail(url=member.avatar.url)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(UserCard(bot))