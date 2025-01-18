import requests
import bs4
import time

time.sleep(3)

url = 'https://ge.globo.com/futebol/times/vasco/'

requisicao = requests.get(url)
pagina = bs4.BeautifulSoup(requisicao.text, 'html.parser')

lista_noticias = pagina.find_all('a', class_='feed-post-link')

for noticia in lista_noticias:
    print(noticia.text)
    print(noticia.get('href'))
    print('----------------------------------')