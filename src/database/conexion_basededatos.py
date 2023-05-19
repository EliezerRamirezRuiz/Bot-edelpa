""" importaciones """
from aioodbc import Connection, connect
from src.config.config import DSN
from pyodbc import ProgrammingError


async def conexion_db() -> Connection:
    """ Retornamos una conexion valida para conectarse a base de datos `SQL SERVER` """
    try:
        connection = await connect(dsn=DSN)
        return connection

    except Exception as ex:
            print(f'ocurrio un error durante la ejecucion, {ex}')


