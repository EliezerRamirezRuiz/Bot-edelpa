"""library used - All are in requirements.txt"""
import os
import logging
import discord

from discord.ext import commands
from Funciones import *
from dotenv import load_dotenv


load_dotenv()


"""Variables"""
token = os.environ["BOT_SECRET_TOKEN"]
descripcion = """Hola soy el bot de Edelpa S.A, \nte ayudare a enterarte de las alertas mas recientes del robot."""
alert = Alerta()


""" Obligatory to retry connection"""
intents = discord.Intents.default()
intents.message_content = True


""" Instance Bot """
bot = commands.Bot(command_prefix='!', description=descripcion,
                   intents=intents, help_command=CustomHelpCommand())


"""Configuration Bot"""
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='r+')


@bot.event
async def on_ready():
    """Evento que esta disponible cuando el bot se conecta de manera correcta \n
    y realiza el registro de las subclases de de Commands.cog, para que esten \n
    disponible los comandos anidados"""
    await bot.add_cog(MyEvents(bot))
    await bot.add_cog(MenuCommands(bot))
    await bot.add_cog(PrincipalCommands(bot))
    await bot.change_presence(activity=discord.Game(name="Working hard"))
    'bot.loop.create_task()'


def main():
    """ Funcion para que el bot pueda correr y ante cualquier 
    inconveniente mande una excepecion expecion """
    try:
        bot.run(token)
        
    except Exception as ex:
        raise ex


if __name__ == '__main__':
    main()