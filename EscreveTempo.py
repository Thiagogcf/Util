import time
from datetime import datetime

import pyautogui
time.sleep(2)
for x in range(0, 100):
    pyautogui.typewrite(datetime.now().strftime("%H:%M:%S")+'\n', interval=0.01)
    time.sleep(1)

