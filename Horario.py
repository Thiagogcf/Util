import time
from datetime import datetime

inicio = datetime.now().timestamp()
inicioexpediente = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 7, 43,30).timestamp()
iniciotarde = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 13, 0,30).timestamp()
iniciohora = datetime.now().time()
final = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 17, 38,30).timestamp()
final2 = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 12, 4,30).timestamp()
while(final>datetime.now().timestamp()):
    print("\n"*10)
    print('\033[0m',iniciohora)
    print('\033[91m',((datetime.now().timestamp()-inicio)*100)/(final-inicio))
    print('\033[96m',((datetime.now().timestamp()-iniciotarde)*100)/(final-iniciotarde))
    print('\033[92m',((datetime.now().timestamp()-inicioexpediente)*100)/(final-inicioexpediente))
    if ((((datetime.now().timestamp()-inicio)*100)/(final2-inicio)) <= 100 and (((datetime.now().timestamp()-inicio)*100)/(final2-inicio))>=0):
        print('\033[92m',((datetime.now().timestamp()-inicio)*100)/(final2-inicio))
    time.sleep(1)