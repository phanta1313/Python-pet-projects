import disnake
from disnake.ext import commands
from yt_dlp import YoutubeDL

YDL_OPTIONS = {'format': 'bestaudio/best', 'noplaylist': True, 'quiet': False}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description='Воспроизвести аудио из YouTube(пока работает только с локальными аудио)')
    async def play(self, ctx):
        # Отправляем предварительный ответ
        await ctx.response.defer()

        if ctx.author.voice is None:
            await ctx.send("Вы должны быть в голосовом канале, чтобы использовать эту команду.")
            return

        voice_channel = ctx.author.voice.channel
        voice_client = ctx.guild.voice_client

        if voice_client is None:
            voice_client = await voice_channel.connect()
        else:
            await voice_client.move_to(voice_channel)

        # with YoutubeDL(YDL_OPTIONS) as ydl:
        #     info = ydl.extract_info(url, download=False)
        #     audio_url = info['formats'][0]['url']

        # voice_client.play(disnake.FFmpegPCMAudio(audio_url, **FFMPEG_OPTIONS))
        voice_client.play(disnake.FFmpegPCMAudio('./audio/warheit.MP3'))
        # Обновляем сообщение после выполнения команды
        # await ctx.edit_original_response(content=f"Сейчас играет: {info['title']}")
        await ctx.edit_original_response(content=f"Сейчас играет: phantasmagoria osu replay - [Wahrheit - Yousei Teikoku]")

def setup(bot):
    bot.add_cog(Music(bot)) 
