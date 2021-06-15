from selenium import webdriver
import requests
import time
url= 'https://fact-checker.line.me/category?type=verified&params=%7B%22size%22%3A12,%22sort%22%3A%7B%22updatedAt%22%3A%7B%22dir%22%3A%22desc%22,%22default%22%3Atrue%7D%7D,%22page%22%3A0%7D&displayList=true&filterType=all'
driver = webdriver.Safari()
driver.maximize_window()
driver.get(url)

time.sleep(3)
driver.close()