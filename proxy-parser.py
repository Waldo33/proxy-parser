from urllib import response
import requests
from bs4 import BeautifulSoup

session = requests.session()

URL = "https://hidemy.name/ru/proxy-list/?type=hs#list"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/101.0.4951.64',
    'Cookie': 'fp=537c55bbc31eb775746b3a393ceaa132; __utmc=104525399; __utmz=104525399.1653408895.1.1.utmcsr=yandex.ru|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; __utma=104525399.1208731747.1653408895.1653408895.1653408895.1; __utmb=104525399.1.10.1653408895; __gads=ID=a8ab341c7f94ea54-22320cc79ccd00a3:T=1653408895:RT=1653408895:S=ALNI_MZThr9Tqjc6q5TcKzv4C6Olohmhug; __gpi=UID=000006b73f34753b:T=1653408895:RT=1653408895:S=ALNI_MZfaY5bKwdeHJ7oMTj2IrJ3KhhSeQ'
}
PARAMS = {'type':'hs','maxtime': '1000'}

res = session.get(URL, headers=HEADERS, params=PARAMS)
soup = BeautifulSoup(res.text, 'html.parser')

rows = soup.find_all('tr')

proxy_list = ''
for row in rows:
    ip_addr = row.find_all('td')[0].text
    port = row.find_all('td')[1].text
    proxy = f'{ip_addr}:{port}'
    if(proxy != 'IP адрес:Порт'):
        proxy_list += f"{proxy}\n"
with open('proxy.txt', 'w', encoding='utf-8') as f:
    f.write(proxy_list)