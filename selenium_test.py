from selenium import webdriver
import time
# driver = webdriver.Chrome("/Users/shaunchuang/Code_Learning/crawl_test/chromedriver")
# driver = webdriver.Chrome('./chromedriver')
driver = webdriver.Safari()
driver.get("https://www.books.com.tw/?loc=tw_logo_001")
time.sleep(5)
driver.close()