import datetime

hoje = datetime.datetime.today().timestamp()
inicio = datetime.datetime(2022, 5, 1).timestamp()
prazo = datetime.datetime(2025, 8, 1).timestamp()
print("foram:")
print(datetime.datetime.today()-datetime.datetime(2022, 5, 1)) #foram
print("Total:")
print(datetime.datetime(2025, 5, 1)-datetime.datetime(2022, 5, 1)) #Total
print("faltam:")
print(datetime.datetime(2025, 5, 1) - datetime.datetime.today()) #faltam
print(((hoje-inicio)/(prazo-inicio))*100)