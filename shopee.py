from selenium import webdriver
import requests
import json
import urllib
from pprint import pprint
from selenium import webdriver
import time

# driver = webdriver.Chrome('./chromedriver')
# driver.maximize_window()
# url_first = 'https://shopee.tw/search?keyword=%E7%94%B7%E5%A5%B3%E9%9E%8B%E6%AC%BE&page=0'
# driver.get(url_first)
# time.sleep(2)
# item = driver.find_element_by_xpath(
#     '//*[@id="main"]/div/div[3]/div/div[2]/div[2]/div[2]/div[1]/a')
# id = item.getAttribute('href')
# print(id)
# # //*[@id="main"]/div/div[3]/div/div[2]/div[2]/div[2]/div[{i}]/a   total 50
# driver.click()

# driver.back()
# driver.close()

keyword = '男女鞋款'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68',
    'x-api-source': 'pc',
    'referer': f'https://shopee.tw/search?keyword={urllib.parse.quote(keyword)}'
}

s = requests.Session()
url = 'https://shopee.tw/api/v4/search/product_labels'
r = s.get(url, headers=headers)

base_url = 'https://shopee.tw/api/v2/search_items/'
query = f"by=relevancy&keyword={keyword}&limit=50&newest=0&order=desc&page_type=search&version=2"
url = base_url + '?' + query
r = s.get(url, headers=headers)
if r.status_code == requests.codes.ok:
    data = r.json()

# with open('shopee.json', 'w', encoding='utf-8') as f:
#     f.write(r.text)
