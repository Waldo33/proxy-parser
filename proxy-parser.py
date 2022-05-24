from urllib import response
from weakref import proxy
import requests
from bs4 import BeautifulSoup

session = requests.session()

URL = "https://hidemy.name/ru/proxy-list/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/101.0.4951.64',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}
PARAMS = {'type':'h', 'start': '0'}

def get_rows(URL, headers, params):
    res = session.get(URL, headers=HEADERS, params=params)
    soup = BeautifulSoup(res.text, 'html.parser')
    rows = soup.find_all('tr')
    return rows

def get_page(rows):
    proxies_page = ''
    for row in rows:
        ip_addr = row.find_all('td')[0].text
        port = row.find_all('td')[1].text
        proxy = f'{ip_addr}:{port}'
        if(proxy != 'IP адрес:Порт'):
            proxies_page += f"{proxy}\n"
    return proxies_page

pages = 10
proxy_list = ''  
for i in range(pages):
    print(f"Get the {i+1} page of {pages}")
    params = {'type':'h', 'start': f"{(i)*64}#list"}
    page = get_rows(URL, HEADERS, params)
    # proxy_list += f"___ PAGE {i} ____\n"
    proxy_list += get_page(page)  

with open('proxy.txt', 'w', encoding='utf-8') as f:
    f.write(proxy_list)