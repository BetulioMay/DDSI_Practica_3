
import constants as c
import cx_Oracle
from helpers import log

#Conectar con la base de datos Oracle con las credenciales especificadas en .env.
def connect():
	try:
		conn = cx_Oracle.connect(
			user=c.USER,
			password=c.PASSWD,
			dsn=f'{c.HOST}/{c.DSN}',
			encoding='UTF-8'
		)
		log(f"Welcome! Connected to Database. Version: {conn.version}")
	except Exception as e:
		raise(e)

	if conn:
		conn.autocommit = False		# Asegurar manejo de transacciones manual
		return conn

# Cierra la conexion `conn` con la BD.
def close_connection(conn):
	if conn:
		log("Closing connection...")
		conn.close()

# Devuelve un objeto `cursor` de una conexion a BD `conn`
def get_cursor(conn):
	return conn.cursor()

# Cierra el cursor `cursor`
def close_cursor(cursor):
	if cursor:
		log("Closing cursor...")
		cursor.close()

def commit(conn):
	try:
		conn.commit()
	except Exception as e:
		log(e)

def rollback(conn):
	try:
		conn.rollback()
	except Exception as e:
		log(e)

def rollback_to(cursor, savepoint):
	try:
		cursor.execute(f"ROLLBACK TO {savepoint}")
	except Exception as e:
		log(e)

def savepoint(cursor, name):
	try:
		cursor.execute(f"SAVEPOINT {name}")
	except Exception as e:
		log(e)