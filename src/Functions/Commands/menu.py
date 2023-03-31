from discord.ext import commands
from discord.ui import View
from Functions.Components.menu_component import Menu
from asyncio import TimeoutError

from Functions.Database.db import get_stock

class MenuCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.group()
    async def menu(self, ctx):
        select = Menu(self.bot, ctx, self)
        view = View(timeout=180)
        view.add_item(select)
        await ctx.send(select.placeholder, view=view)
    

    @menu.command()
    async def stock(self, ctx):
        """Funcion que funciona solo si el padre menu lo llama, ademas consultar stock a pedir"""
        try:
            await ctx.send("Porfavor escriba el codigo del stock a consultar:")
            message = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=30.0)

            result = await get_stock(str(message.content), ctx)
            await ctx.send(result)
        
        except TimeoutError:
            return f"Lo siento se excedio el tiempo para responder, reintente con !menu"


    @menu.command()
    async def robot(self, ctx):
        try:
            pass

        except TimeoutError:
            await ctx.send(f"""Lo siento se excedio el tiempo para responder, reintente con !menu """)

