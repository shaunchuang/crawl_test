import pandas as pd
import requests
from bs4 import BeautifulSoup
from pprint import pprint


url = 'https://www.abccar.com.tw//abcapi/search'
headers = {'accept': 'application/json, text/javascript, */*; q=0.01',
           'accept-encoding': 'gzip, deflate, br',
           'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
           'content-length': '50',
           'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
           'cookie': '_gcl_au=1.1.1728982988.1624089038; __gads=ID=70384f1bba64682e:T=1624089037:S=ALNI_MaR4p9PPy2_PlilD7HCz9ni9a8exg; _ga=GA1.3.1085617352.1624089037; __BWfp=c1624089042902xd364ed052; _gid=GA1.3.2115392437.1624176184; _fbp=fb.2.1624176889577.974609533; abc_session=80nlnao0r7pljpqau4l9ggnecccs9srr; _gat_UA-76403875-5=1',
           'origin': 'https://www.abccar.com.tw',
           'referer': 'https://www.abccar.com.tw/search?tab=1&SearchType=1&OrderByField=0&page=1',
           'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
           'sec-ch-ua-mobile': '?0',
           'sec-fetch-dest': 'empty',
           'sec-fetch-mode': 'cors',
           'sec-fetch-site': 'same-origin',
           'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
           'x-requested-with': 'XMLHttpRequest'}
# headers = {
# 'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
# 'accept-encoding':'gzip, deflate, br',
# 'accept-language':'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
# 'cookie':'_gcl_au=1.1.1728982988.1624089038; __gads=ID=70384f1bba64682e:T=1624089037:S=ALNI_MaR4p9PPy2_PlilD7HCz9ni9a8exg; _ga=GA1.3.1085617352.1624089037; __BWfp=c1624089042902xd364ed052; abc_session=9rkbrposdmtg4rgk4dl1oklafd4i3c2r; _gid=GA1.3.2115392437.1624176184; _fbp=fb.2.1624176889577.974609533',
# 'sec-ch-ua':'" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
# 'sec-ch-ua-mobile':'?0',
# 'sec-fetch-dest':'document',
# 'sec-fetch-mode':'navigate',
# 'sec-fetch-site':'none',
# 'sec-fetch-user':'?1',
# 'upgrade-insecure-requests':'1',
# 'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'}
r = requests.get(url, headers=headers)
pprint(r.text.strip())
soup = BeautifulSoup(r.text, 'lxml')
pprint(soup.text.strip())
