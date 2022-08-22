import datetime
import time

hoje = datetime.datetime.today()
inicio = datetime.datetime(2022, 5, 1)
prazo = datetime.datetime(2025, 5, 1)
print(hoje)
print(prazo)
print(prazo-hoje)
print((prazo-hoje).days*100/(prazo-inicio).days)