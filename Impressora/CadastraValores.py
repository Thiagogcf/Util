import time

import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
driver.get(r'https://docs.google.com/spreadsheets/d/1Myhk6LYAvVK6xNn0SgUjdWS2RA0w7aYMaTe8IsciZuM/edit?usp=sharing')
time.sleep(2)
try:
    driver.find_element(By.CLASS_NAME, 'waffle-chip-walkthrough-promo-close goog-inline-block goog-flat-button').click()
except:
    print("não gerou msg chata")
# time.sleep(1)
pyautogui.PAUSE = .1
pyautogui.keyDown("ctrl")
pyautogui.press('down')
pyautogui.keyUp('ctrl')
arquivo = open('Valores.txt','r')
pyautogui.press('down')
pyautogui.press('enter')
for x in arquivo:
    pyautogui.typewrite(x)
    pyautogui.press('enter')
    time.sleep(1)
arquivo.close()
arquivo = open('Valores.txt','w').close()
time.sleep(1)
driver.close()
exit(0)