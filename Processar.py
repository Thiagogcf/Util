import time

import pyautogui
from pyperclip import copy

file = open("Txt/Gpt", "r")
char = 0
texto = ""
cont = 0
time.sleep(5)
for line in file:
    if (char+len(line))<4096:
        char += len(line)
        texto += line
    else:
        copy(texto)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('enter')
        time.sleep(2)
        pyautogui.hotkey('tab')
        pyautogui.hotkey('enter')
        pyautogui.hotkey('shift', 'tab')
        pyautogui.hotkey('shift', 'tab')
        cont+=1
        print(cont)
        time.sleep(2)
        print("\n=================================\n")
        char = 0
        texto = ""
    # print(len(line))