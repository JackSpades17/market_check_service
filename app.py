#https://www.perekrestok.ru/cat
import time
from bs4 import BeautifulSoup
import requests

product = 'cat/123/p/ajco-kurinoe-roskar-ekstra-so-10st-44323'

r = requests.get(f'https://www.perekrestok.ru/{product}')
soup = BeautifulSoup(r.text,'html.parser')
a = soup.find('div', class_='price-card-unit-value')
print(a.get_text().split()[0])