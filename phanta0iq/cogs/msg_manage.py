import disnake; from disnake.ext import commands;
import os

BAD_WORDS = os.getenv('BAD_WORDS')
GIF_URLS = {'shikimori_shocked' : 'https://tenor.com/view/shikimori-shikimoris-not-just-cute-shikimoris-not-just-a-cutie-anime-anime-anime-girl-gif-26002811'}

class MessageManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(description="удаляет определенное кол-во сообщений на канале")
    async def clear(self, ctx, count: int):
        embed = disnake.Embed(title="Clear", description=f"Deleted {count} messages", color=0x00ff00)
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        await ctx.response.send_message(embed=embed)
        await ctx.channel.purge(limit=count+1)
        
    
    @commands.Cog.listener()
    async def on_member_join(self, member: disnake.Member):
        welcome_channel_id = 1295386052151873582  
        channel = self.bot.get_channel(welcome_channel_id)
        
        if channel is not None:
            embed = disnake.Embed(title="Зарова кожаный ублюдок", description=f"{member.mention}", color=0x00ff00)
            embed.set_thumbnail(url=member.avatar.url if member.avatar else self.bot.user.avatar.url)
            embed.set_footer(text="Присоединился к серверу")
            embed.set_author(name=member.display_name, icon_url=member.avatar.url if member.avatar else self.bot.user.avatar.url)
            
            await channel.send(embed=embed)
        
    @commands.Cog.listener()
    async def on_message(self, message):
        shikimori_shocked_gif = GIF_URLS['shikimori_shocked']

        if message.author == self.bot.user:
            return

        for word in message.content.split():
            if word.lower() in BAD_WORDS.lower().split():
                await message.channel.send(f'{message.author.mention} ай ай что за слова такие!\n{shikimori_shocked_gif}')

        if self.bot.user in message.mentions:
            await message.channel.send('НЕ ТЫКАЙТЕ В МЕНЯ!!!')

    @commands.slash_command(description="скажи что нибудь через меня")
    async def say(self, ctx, message, user: disnake.User):
        await ctx.send(f'{user.mention} {message}')

def setup(bot):
    bot.add_cog(MessageManager(bot))