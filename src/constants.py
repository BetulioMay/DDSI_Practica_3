"""
Constantes o variables globales.
"""

import os
from enum import Enum

# Credenciales
HOST = os.getenv("ORACLE_DB_HOST")
PORT = os.getenv("ORACLE_DB_PORT")
USER = os.getenv("ORACLE_DB_USER")
PASSWD = os.getenv("ORACLE_DB_PASSWD")
DSN = os.getenv("ORACLE_DB_DNS")

# Enums
class MENU_OPTION(Enum):
    PAREJAS_ENTRENADOR = 1
    PAGAR_COMPRA = 2
    GUARDAR_PARTIDO = 3
    EXIT_MENU = 4


# Styles
HEADER = "-" * 15
IN_PROMPT = "> "
