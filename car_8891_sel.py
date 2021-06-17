from selenium import webdriver
import time
import numpy as np
import pandas as pd

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
time.sleep(1)
df = pd.DataFrame(columns=['Title', 'Describe', 'Price', 'Year', 'Distance'])
for x in range(1, 4):
    url = f'https://auto.8891.com.tw/?page={x}'
    driver.get(url)
    time.sleep(5)

    for i in range(1, 41):
        title = driver.find_element_by_xpath(
            f'//*[@id="search-result"]/a[{i}]/div/div[2]/div[1]/span')
        # print(title.text)

        describe = driver.find_element_by_xpath(
            f'//*[@id="search-result"]/a[{i}]/div/div[2]/div[2]')
        # print(describe.text)

        price = driver.find_element_by_xpath(
            f'//*[@id="search-result"]/a[{i}]/div/div[3]/span[1]/b')
        # print(price.text)

        year = driver.find_element_by_xpath(
            f'//*[@id="search-result"]/a[{i}]/div/div[3]/span[2]/b')
        # print(year.text)

        distance = driver.find_element_by_xpath(
            f'//*[@id="search-result"]/a[{i}]/div/div[3]/span[3]')
        # print(distance.text)
        df = df.append({'Title': title.text, 'Describe': describe.text, 'Price': price.text,
                       'Year': year.text, 'Distance': distance.text}, ignore_index=True)
        

print(df)
df.to_csv('car.csv',encoding='utf-8-sig')
driver.close()
