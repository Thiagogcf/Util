import time

import pyautogui
t_end = time.time() + 3
cont = 0.0
pyautogui.PAUSE = 0.05
while time.time() < t_end:
    pyautogui.hotkey('Capslock')
    pyautogui.hotkey('scrolllock')
    pyautogui.hotkey('numlock')
    cont+=1
    print(cont)
if (cont % 2 != 0):
    pyautogui.hotkey('Capslock')
    pyautogui.hotkey('scrolllock')
    pyautogui.hotkey('numlock')
