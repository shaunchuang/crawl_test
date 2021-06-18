from selenium import webdriver
import time
import json

# driver = webdriver.Chrome('./chromedriver')
# driver.maximize_window()
# time.sleep(1)

# url = 'https://shopee.tw/search?keyword=%E5%8F%A3%E7%BD%A9&page=0'

# driver.get(url)
# time.sleep(2)

# driver.close()
# with open('new1.json','r') as f:
#     new = json.loads(f.read())
#     json.dumps(,ensure_ascii=False)
#     print(new)
import requests


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68',
    'x-api-source': 'pc',
}

url = 'https://shopee.tw/api/v2/item/get_ratings?filter=0&flag=1&itemid=3286556671&limit=6&offset=0&shopid=97937210&type=0'
r = requests.get(url, headers=headers)


data = r.json()
