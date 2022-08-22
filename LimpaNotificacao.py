import time

import pyautogui

notificacao = pyautogui.locateOnScreen('Notificacao/notificacao.png')
pyautogui.moveTo(notificacao)
time.sleep(.3)
ret = pyautogui.locateOnScreen('Notificacao/Ret.png')
pyautogui.click(ret)
time.sleep(.2)
pyautogui.moveRel(50,70)
pyautogui.click()