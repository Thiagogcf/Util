import requests
import pyperclip

url = 'http://192.168.1.144/SmartCooper/api/Token'
myobj = { 'usuario': 'Infogen',  'senha': 'Inf6459'}

x = requests.post(url, json = myobj)
valor = "Bearer " + x.json()['token']
pyperclip.copy(valor)
print(valor)