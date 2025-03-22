from bs4 import BeautifulSoup
import requests

url = "https://pt.wikipedia.org/wiki/Star_Wars"

response = requests.get(url)

if response.status_code == 200:
    print("Sucesso ao acessar a URL")
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    title = soup.title.string
    print(title)
    print("---------------------------------")
    
    paragrafo_um = soup.find("p").text
    print(paragrafo_um)
    print("---------------------------------")
    
    paragrafos = soup.find_all("p")
    
    if len(paragrafos) > 1:
        print(paragrafos[1].text)
        #no print acima pegamos o segundo paragrafo
        print("---------------------------------")
    else:
        print("Não existe mais de 1 paragrafo")
    
    links = soup.find_all("a", href=True)[:5]
    for link in links:
        print(link["href"])
        print("---------------------------------")