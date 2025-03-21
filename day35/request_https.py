import requests

url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)

if response.status_code == 200:
    print("Sucesso!")
    data = response.json()

    print("Esta piada é do Chuck Norris")
    print(data['value'])
else:
    print("Erro ao chamar a API.")
