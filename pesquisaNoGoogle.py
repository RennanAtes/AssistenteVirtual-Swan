import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
r = requests.get('https://www.google.com/search?q=primeira+guerra+mundial&sxsrf=AJOqlzU3sEwLNYvvPUGSgnjF97g9KZul2Q%3A1675379443901&ei=80LcY6LaNsWO5OUPq9ikiAI&ved=0ahUKEwjin_jk-vf8AhVFB7kGHSssCSEQ4dUDCA8&uact=5&oq=primeira+guerra+mundial&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECCMQJzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoKCAAQRxDWBBCwAzoLCC4QgAQQsQMQgwE6CwgAEIAEELEDEIMBOgoIABCxAxCDARBDOgQILhBDOggIABCxAxCDAToHCC4QsQMQQzoECAAQQzoHCAAQsQMQQzoRCC4QgAQQsQMQgwEQxwEQ0QM6BwgAEIAEEAo6DQgAEIAEELEDEIMBEAo6DgguEIAEELEDEIMBENQCOggIABCABBCxAzoOCAAQgAQQsQMQgwEQyQM6EAguEIAEELEDEIMBENQCEAo6EAgAEIAEELEDEIMBEMkDEAo6DQguEIAEELEDEIMBEAo6CggAEIAEELEDEApKBAhBGABKBAhGGABQ5wlYwhpg_xpoAXABeACAAdsBiAHcEpIBBjUuMTUuMZgBAKABAcgBCMABAQ&sclient=gws-wiz-serp',headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')
print(soup)
texto = soup.find(class_='kno-rdesc')
filtrando = texto
texto2 = filtrando.find('span').get_text()
print(texto2)