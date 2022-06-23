import random
import time

import pyautogui
import math

R = 400
(x, y) = pyautogui.size()
(X, Y) = pyautogui.position(x / 2, y / 2)
pyautogui.moveTo(X + R, Y)
try:
    while True:
        for i in range(360):
            if i % 6 == 0:
                pyautogui.moveTo(X + R * math.cos(math.radians(i)), Y + R * math.sin(math.radians(i)))
                if random.randint(1,50) == 1:
                    pyautogui.leftClick()
                    pyautogui.hotkey('ESC')
        ale = random.randint(10, 120)
        print(ale)
        time.sleep(ale)

except KeyboardInterrupt:
    pass
