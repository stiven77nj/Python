
from datetime import datetime

fechaHora = datetime.now()

año = fechaHora.year
mes = fechaHora.month
dia = fechaHora.day

hora = fechaHora.hour
minutos = fechaHora.minute
segundos = fechaHora.second

print(f"La hora es: {hora}:{minutos}:{segundos}")
print(f"La fecha es: {año}|{mes}|{dia}")
