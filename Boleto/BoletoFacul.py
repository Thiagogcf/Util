import datetime
import ctypes

arquivo = open("pago.txt",'r')

if (datetime.datetime.now().day >= 11 and datetime.datetime.now().day <= 16 and datetime.datetime.now().weekday() and arquivo.read() != "1"):
    resp = ctypes.windll.user32.MessageBoxW(0, "Pagou o boleto da faculdade?", "Boleto da faculdade",4)
    if(resp == 6):
        open("pago.txt",'w').writelines("1")
    print(resp)#6sim 7nao
    print("boleto")
elif (datetime.datetime.now().day == 16 and arquivo.read() == "1"):
    open("pago.txt",'w').writelines("0")
    print("Resetando o mes, logo pagaras")
print(arquivo.readlines())