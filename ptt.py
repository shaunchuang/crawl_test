import requests
from bs4 import BeautifulSoup
import time
import re
url = "https://www.ptt.cc/bbs/car/index5000.html"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}

def parse_html(url,headers):
    return BeautifulSoup(requests.get(url,headers=headers).text, 'lxml')


soup = parse_html(url,headers)

def find_article_link(soup):
    list1=[]
    list2=[]
    divs = soup.select('div.title > a')
    for title in divs:
        list2.append(title.text.strip())

    for a in divs:
        list1.append('https://www.ptt.cc'+a.get('href'))
    return list1


def content_crawler(list1,headers):
    for a in list1:
        soup = parse_html(a,headers)
        print(soup.text)

for i in reversed(range(5001)):
    print(i)
# content_crawler(find_article_link(parse_html(url,headers)),headers)


