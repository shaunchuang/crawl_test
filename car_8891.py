import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import re
import time


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}

def parse_html(url, headers):

    return BeautifulSoup(requests.get(url, headers=headers).text, 'lxml')

def content_crawler(soup):
    list1=[]
    items=soup.find_all(attr={'style':'display: block','target':'_blank'})
    for item in items:
        ib_info_title=item.find(class_='ib-info-title')
        list1.append(ib_info_title.text)
    print(list1)
    return list1

# for i in range(992):
i=1
url = f'https://auto.8891.com.tw/?page={i}'
# content = content_crawler(parse_html(url, headers))
list1=[]
soup=parse_html(url,headers)
print(soup.text)
items=soup.find_all(attr={'style':'display: block','target':'_blank'})

for item in items:
    print(item.text)
    ib_info_title=item.find(class_='ib-info-title')
    list1.append(ib_info_title.text)