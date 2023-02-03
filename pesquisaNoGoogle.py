import requests
from bs4 import BeautifulSoup



def obtendoResposta(pergunta):
    print(pergunta)
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
    r = requests.get(f'https://www.google.com/search?q={pergunta}',headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    texto = soup.find(class_='kno-rdesc')
    filtrando = texto
    print(filtrando)
    texto2 = filtrando.find('span').get_text()
    return texto2