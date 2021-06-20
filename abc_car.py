import pandas as pd
import requests


url = 'https://www.abccar.com.tw/search?tab=1&SearchType=1&OrderByField=0&page=1'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}

r = request.get(url,headers=headers)
soup=Beautifulsoup(r.text,'lxml')
