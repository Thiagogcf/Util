import datetime

import numpy as np

valorInserido = input('digite quantos minutos antes vc chegou: ')
if valorInserido != '':
    arquivo = open('Log.txt', 'a')
    arquivo.write(valorInserido + '\n')
    arquivo.close()

arquivo = open('Log.txt', 'r')
cumpridoAteAgora = datetime.timedelta()
cont = 0
for linha in arquivo:
    cumpridoAteAgora += datetime.timedelta(minutes=int(linha.strip()))
    cont+=1

print("horario cumprido até o momento: "+str(cumpridoAteAgora))
restante = datetime.timedelta(hours=8, minutes=42) - cumpridoAteAgora

print('voce ainda tem que repor', str(restante),'horas')
print('percentual cumprido:', str((cumpridoAteAgora / datetime.timedelta(hours=8, minutes=42)) * 100) + '%')
# considerando que a cada 2 linhas do arquivo, 1 dia se passa
# calcula a media de horas extras por dia
print('media de horas extras por meio dia:', str(cumpridoAteAgora / cont))

#tenho ate o ultimo dia util do mes para repor as horas
hoje = datetime.date.today()
ultimo_dia_mes = datetime.date(hoje.year, hoje.month+1, 1) - datetime.timedelta(days=1) if hoje.month != 12 else datetime.date(hoje.year+1, 1, 1) - datetime.timedelta(days=1)
dias_uteis_restantes = np.busday_count(hoje.isoformat(), ultimo_dia_mes.isoformat())

# Calcula quantas horas:minutos por dia precisa repor
horas_por_dia = restante / dias_uteis_restantes
print('voce precisa repor', str(horas_por_dia), 'por dia')

print('dias restantes:', dias_uteis_restantes)