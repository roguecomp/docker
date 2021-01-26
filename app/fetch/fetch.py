from bs4 import BeautifulSoup as bs
import requests
import time

page_url = "https://finance.yahoo.com/quote/TSLA/news/"
page = requests.get(page_url)
soup = bs(page.content, 'html.parser')

u = soup.find_all('a')
url = []
for i in u:
    for word in str(i).split(' '):
        if(word[:7]=='href="/'):
            end = word.find('l"')
            url.append(word[7:end+1])

urls = []
for i in url:
    urls.append(page_url + i)

urls = list(set(urls))

urls = urls[-2:]

url = ""
for url in urls:
    page = requests.get(url)
    soup = bs(page.content, 'html.parser')
    a = soup.find_all('p')
    print(a[2])
