import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"
    ,'x-api-source': 'pc'}
url = 'https://shopee.tw/search?keyword=%E5%8F%A3%E7%BD%A9&page=0'
def parse_html(url, headers):
    return BeautifulSoup(requests.get(url, headers=headers).text, 'lxml')

soup=parse_html(url,headers)
print(soup)