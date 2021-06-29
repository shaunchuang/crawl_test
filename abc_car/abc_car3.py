import pandas as pd
import requests
from bs4 import BeautifulSoup
from pprint import pprint


# 'referer':'https://www.abccar.com.tw/search?tab=1&SearchType=1&OrderByField=0&page=1'


headers = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding':'gzip, deflate, br',
'accept-language':'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
'cache-control':'max-age=0',
'cookie':'_gcl_au=1.1.1728982988.1624089038; __gads=ID=70384f1bba64682e:T=1624089037:S=ALNI_MaR4p9PPy2_PlilD7HCz9ni9a8exg; _ga=GA1.3.1085617352.1624089037; __BWfp=c1624089042902xd364ed052; _gid=GA1.3.2115392437.1624176184; FavCars=1440564; visited=4; abc_session=044oe1v189j3egom694bsvn1t7ughrg8; _fbp=fb.2.1624246810183.1916500634; SearchCarCacheKey=CacheSearchResultAll_Zone0_12',
'sec-ch-ua':'" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
'sec-ch-ua-mobile':'?0',
'sec-fetch-dest':'document',
'sec-fetch-mode':'navigate',
'sec-fetch-site':'same-origin',
'sec-fetch-user':'?1',
'upgrade-insecure-requests':'1'}
url='https://www.abccar.com.tw/car/1440564?car_source=index-top-dealer'

r=requests.get(url,headers=headers)
pprint(r.text)
