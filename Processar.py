import time

import pyautogui
from pyperclip import copy

file = open("Txt/Gpt", "r", encoding="utf-8")
pyautogui.PAUSE = 0.2
def Enviar(texto,continuar=True):
    copy(texto)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')
    if continuar:
        time.sleep(4)
        pyautogui.hotkey('tab')
        pyautogui.hotkey('enter')
        pyautogui.hotkey('shift', 'tab')
        pyautogui.hotkey('shift', 'tab')

char = 0
texto = ""
cont = 1
input("Pressione |ENTER| para iniciar")
print("OK...")
time.sleep(5)
Enviar("Irei te mandar um texto fragmentado em varias partes")
for line in file:
    #if (char+len(line))<4080:
    if (char+len(line))<8160:
        char += len(line)
        texto += line
    else:
        Enviar((texto+ "\n{essa é a parte " + str(cont) + " do texto}"))
        cont+=1
        print(cont)
        print("\n=================================\n")
        char = 0
        texto = ""
        char += len(line)
        texto += line
Enviar("Texto finalizado, voce compreendeu o texto?",False)