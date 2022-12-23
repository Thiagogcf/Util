import datetime

hoje = datetime.datetime.today().timestamp()
inicio = datetime.datetime(2022, 5, 1).timestamp()
prazo = datetime.datetime(2025, 5, 1).timestamp()
print("Foram "+datetime.datetime.today()-datetime.datetime(2022, 5, 1))
print(((hoje-inicio)/(prazo-inicio))*100)