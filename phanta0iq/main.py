import disnake
from disnake.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('TOKEN')

intents = disnake.Intents.all()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents, test_guilds=[1295386052151873577])

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


bot.load_extensions("cogs")


bot.run(TOKEN)
