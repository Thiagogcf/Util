import datetime
import random
valor = 60466176
senha = random.randint(1,valor)
print(senha)
inicio = datetime.datetime.now()
for x in range(1,valor,1):
    # if x == senha:
    #     print('achou') # calcular o final
    #     print(x)
    if x == int(round(valor/100)):
        agora = datetime.datetime.now()
        print((agora-inicio)*100)


fim = datetime.datetime.now()
print(fim-inicio)