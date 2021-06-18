from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
time.sleep(1)

url = 'https://shopee.tw/search?keyword=%E5%8F%A3%E7%BD%A9&page=0'

driver.get(url)
time.sleep(2)

driver.close()