import requests

url = 'https://libretranslate.com/translate'
myobj = {'q': "Socorro",
		'source': "pt",
		'target': "en",
		'format': "text",
		'api_key': ""}

x = requests.post(url, json = myobj)

print(x.text)
