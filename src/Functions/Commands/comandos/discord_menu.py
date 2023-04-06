from discord.ext import commands
from discord.ui import View

from Functions.Commands.Componentes.menu import Menu


class MenuCommands(commands.Cog):
    """Aqui se define una clase con metodos que son 
    comandos que solo pueden ser llamadas por el menu"""
    def __init__(self, bot):
        self.bot = bot


    @commands.group()
    async def menu(self, ctx):
        """Menu con opciones, las opciones son funciones"""
        select = Menu(self.bot, ctx, self)
        view = View(timeout=180)
        view.add_item(select)
        await ctx.send(select.placeholder, view=view)