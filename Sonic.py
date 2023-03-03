import requests

# Define as informações de login
payload = {'username': 'thiago.ferronato', 'password': 'pz6!vh%R'}

# Envia a solicitação de login para o site
url = 'http://192.168.1.1/sonicui/7/login/#/?cid=4'
response = requests.post(url, data=payload)

# Verifica se o login foi bem-sucedido
if response.status_code == 200:
    print('Login realizado com sucesso!')
else:
    print('Erro ao realizar login.')
