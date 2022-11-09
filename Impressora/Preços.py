import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
driver.get(r'https://www.banggood.com/Flsun-V400-Triple-Speed-400-or-s-3D-Printer-300+410-Print-Size-with-Klipper-Pre-installed-or-Dual-Gear-Extruder-or-7-inch-Interactive-Screen-p-1968597.html?imageAb=1&cur_warehouse=CN&ID=47184&rmmds=search&a=1667569024.4799&DCC=BR&currency=BRL&akmClientCountry=BR')
time.sleep(1)
valor = driver.find_element(By.CLASS_NAME, "main-price")
numero = valor.text.replace('R$','')
print(numero)
valores = open('Valores.txt','a')
valores.write(numero+'\n')
valores.close()
driver.close()
exit(0)
