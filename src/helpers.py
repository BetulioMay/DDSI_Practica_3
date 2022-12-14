'''
Funciones de utilidad.
'''

from datetime import datetime
import os

if os.getenv("DEV") == "1":
	def log(message):
		log_dt = datetime.now()
		print(f"[{log_dt.year}-{log_dt.month}-{log_dt.day} {log_dt.hour}:{log_dt.minute}:{log_dt.second}]: {message}")
else:
	def log(message):
		pass
