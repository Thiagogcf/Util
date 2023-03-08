import ctypes
import time
from datetime import datetime
inicio = datetime.now().timestamp()
inicioexpediente = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 7, 41,30).timestamp()
iniciotarde = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 13, 0,00).timestamp()
iniciohora = datetime.now().time()
final = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 17, 30, 0).timestamp()
final2 = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 11, 51, 5).timestamp()
while(final>datetime.now().timestamp()):
    print("\n"*10)
    print('\033[0m',iniciohora)
    if 100 >= (((datetime.now().timestamp() - inicio) * 100) / (final2 - inicio)) >= 0:
        print('\033[0m',((datetime.fromtimestamp(final2))-datetime.now()))
    else:
        print('\033[0m', ((datetime.fromtimestamp(final))-datetime.now()))
    print('\033[91m',((datetime.now().timestamp()-inicio)*100)/(final-inicio))
    print('\033[96m',((datetime.now().timestamp()-iniciotarde)*100)/(final-iniciotarde))
    print('\033[92m',((datetime.now().timestamp()-inicioexpediente)*100)/(final-inicioexpediente))
    if 100 >= (((datetime.now().timestamp() - inicio) * 100) / (final2 - inicio)) >= 0:
        print('\033[93m',((datetime.now().timestamp()-inicio)*100)/(final2-inicio))
        print('\033[95m',((datetime.now().timestamp()-inicioexpediente)*100)/(final2-inicioexpediente))
    time.sleep(1)
print(ctypes.windll.user32.MessageBoxW(0, "Barbeiro", "Aviso",0))