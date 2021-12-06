import requests
from bs4 import BeautifulSoup

url = 'https://livedune.ru/youtube'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


block = soup.find('main', class_='main')
items = block.find('div', class_='items')
channels = items.findAll('div', class_='search-item clearfix')
for channel in channels:
    info = channel.find('div', class_='w-p')
    name = info.find('span', class_='search-item-id').text

    subinfo = channel.find('div', class_='watch-item')
    sub = subinfo.find('p', class_='search-counter-number')

    viewinfo = channel.find('div', class_='watch-item hidden-sm hidden-xs')
    view = viewinfo.find('p', class_='search-counter-number')
    #name.append(info.find('span', class_='search-item-id').text)

    with open('Names.txt', 'a', encoding="utf-8") as file:
        print(str(name) + ': SUBS --->' + str(sub.text) +
              ', TOTAL VIEWS ---> ' + str(view.text), file=file, sep='\n \n')
