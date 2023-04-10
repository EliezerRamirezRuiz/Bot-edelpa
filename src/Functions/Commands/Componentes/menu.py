"""Archivo que contiene el menu con multiples opciones 
que apretando alguna realiza la accion conrrespondiente"""

from Functions.Database.Funciones.alertas import LeerAlerta
from Functions.Database.Funciones.estado_robot import EstadoRobot
from Functions.Database.Funciones.obtener_stock import ObtenerStock
from Functions.Database.Funciones.reporte_dia import ReporteDia
from discord.ui import Select

import discord

alert = LeerAlerta()
estado_robot =  EstadoRobot()
obtener_stock = ObtenerStock()
reporte_dia = ReporteDia()


class Menu(Select):
    def __init__(self, bot, ctx, bot_command):
        self.bot = bot
        self.ctx = ctx
        self.bot_command = bot_command

        options = [
            discord.SelectOption(
            label="Default",
            description="default",
            default=True,
            value="Default"),

            discord.SelectOption(
            label="Consultar Stock",
            description="Consultar stock de producto X",
            value="Consultar Stock"),

            discord.SelectOption(
            label="Estado Robot",
            description="Saber el estado actual del robot",
            value="Estado Robot"),

            discord.SelectOption(
            label="Ultimas Alertas",
            description="Saber la cantidad de Bobinas que contiene un pallet",
            value="Ultimas Alertas"),

            discord.SelectOption(
            label="Reporte del dia",
            description="Saber la cantidad hecha por dia",
            value="Reporte del dia"),

            discord.SelectOption(
            label="prueba",
            description="Saber la cantidad hecha por dia",
            value="prueba"),]

        super().__init__(custom_id="Menu", placeholder="Menu",
                        min_values=1, max_values=1,
                        options=options, row=2)

    async def callback(self, interaccion: discord.Interaction):

        # Caso 1
        if self.values[0] == "Consultar Stock":
            try:
                await interaccion.response.send_message('Escriba el codigoa consultar!')
                message = await self.bot.wait_for('message', check=lambda m: m.author == self.ctx.author, timeout=30.0)
                result = await obtener_stock.query(str(message.content))
                await self.ctx.send(result)

            except TimeoutError as error:
                await self.ctx.send(f'error:{error}')

        # Caso 2
        elif self.values[0] == "Estado Robot":
            await interaccion.response.send_message('Verificando')
            """next code"""

        # Caso 3
        elif self.values[0] == "Ultimas Alertas":
            try:
                await interaccion.response.send_message("Obteniendo alertas")
                result = await alert.query()
                await self.ctx.send(result)
        
            except Exception as ex:
                await self.ctx.send(f"ultimas alertas:{ex}")

        #Caso 4
        elif self.values[0] == "Reporte del dia":
            try:
                await interaccion.response.send_message("Obteniendo reporte")
                await reporte_dia.query()
        
            except Exception as ex:
                await self.ctx.send(f"ultimas alertas:{ex}")

