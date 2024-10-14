import disnake; from disnake.ext import commands;
from disnake.ui import Button, View


class TicTacToe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.board = ['?' for x in range(9)]

    async def create_private_channel(self, ctx, user1: disnake.Member, user2: disnake.Member):
        guild = ctx.guild

        overwrites = {
            guild.default_role: disnake.PermissionOverwrite(read_messages=False),  # Запрещаем доступ всем
            user1: disnake.PermissionOverwrite(read_messages=True, send_messages=True),  # Разрешаем доступ user1
            user2: disnake.PermissionOverwrite(read_messages=True, send_messages=True),  # Разрешаем доступ user2
            ctx.author: disnake.PermissionOverwrite(read_messages=True, send_messages=True)  # Разрешаем доступ автору
        }

        channel = await guild.create_text_channel(f'private-{user1.name}-{user2.name}', overwrites=overwrites)

        await channel.send(f"{user1.mention} и {user2.mention}, вас отправили в приватный канал!")
        

    def format_board(board):
        return f"""
        {board[0]} | {board[1]} | {board[2]}
        ---------
        {board[3]} | {board[4]} | {board[5]}
        ---------
        {board[6]} | {board[7]} | {board[8]}
        """
    
    async def show_table(self, ctx):
        await ctx.send(embed=disnake.Embed(title='Крестики нолики', description=self.format_board(self.board)))

    @commands.slash_command(description="крестики нолики")
    async def tictactoe(self, ctx, user1: disnake.Member, user2: disnake.Member):
        await self.create_private_channel(ctx, user1, user2)
        await self.show_table(ctx)



def setup(bot):
    bot.add_cog(TicTacToe(bot))