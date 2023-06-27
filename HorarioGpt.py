import ctypes
import time
from datetime import datetime
from tqdm import tqdm


def create_progress_bar(percentage, bar_length=30, description=None):
    filled_length = int(round(bar_length * percentage / 100))
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    if description:
        return f"{description}: |{bar}| {percentage:.2f}%"
    else:
        return f"|{bar}| {percentage:.2f}%"


inicio = datetime.now().timestamp()
inicioexpediente = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 7, 41, 30).timestamp()
iniciotarde = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 13, 0, 0).timestamp()
iniciohora = datetime.now().time()
final = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 17, 30, 0).timestamp()
final2 = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 12, 0, 5).timestamp()

while final > datetime.now().timestamp():
    print("\n" * 10)
    print('\033[0m', iniciohora)

    if 100 >= (((datetime.now().timestamp() - inicio) * 100) / (final2 - inicio)) >= 0:
        remaining_time = (datetime.fromtimestamp(final2) - datetime.now()).total_seconds()
    else:
        remaining_time = (datetime.fromtimestamp(final) - datetime.now()).total_seconds()

    percentage1 = ((datetime.now().timestamp() - inicio) * 100) / (final - inicio)
    percentage2 = ((datetime.now().timestamp() - iniciotarde) * 100) / (final - iniciotarde)
    percentage3 = ((datetime.now().timestamp() - inicioexpediente) * 100) / (final - inicioexpediente)

    if 100 >= (((datetime.now().timestamp() - inicio) * 100) / (final2 - inicio)) >= 0:
        percentage4 = ((datetime.now().timestamp() - inicio) * 100) / (final2 - inicio)
        percentage5 = ((datetime.now().timestamp() - inicioexpediente) * 100) / (final2 - inicioexpediente)
    else:
        percentage4 = None
        percentage5 = None

    print(create_progress_bar(percentage1, description='\033[91m'))
    print(create_progress_bar(percentage2, description='\033[96m'))
    print(create_progress_bar(percentage3, description='\033[92m'))

    if percentage4 is not None and percentage5 is not None:
        print(create_progress_bar(percentage4, description='\033[93m'))
        print(create_progress_bar(percentage5, description='\033[95m'))

    time.sleep(1)

print(ctypes.windll.user32.MessageBoxW(0, "Barbeiro", "Aviso", 0))
