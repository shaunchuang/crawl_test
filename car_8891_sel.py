from selenium import webdriver
import time
import numpy as np
import pandas as pd

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
time.sleep(1)
df = pd.DataFrame(columns=['Brand', 'Type', 'Title',
                  'Describe', 'Price', 'Year', 'Distance'])
for x in range(1, 4):
    url = f'https://auto.8891.com.tw/?page={x}'
    driver.get(url)
    time.sleep(3)

    for i in range(1, 41):
        title = driver.find_element_by_xpath(
            f'//*[@id="search-result"]/a[{i}]/div/div[2]/div[1]/span')
        Brand = title.text.split(' ', 1)[0]
        Type = title.text.split(' ', 1)[1]
        year_type = title.text.rsplit(' ', 2)[1]
        Exhaust = title.text.rsplit(' ', 2)[2]

        describe = driver.find_element_by_xpath(
            f'//*[@id="search-result"]/a[{i}]/div/div[2]/div[2]')

        price = driver.find_element_by_xpath(
            f'//*[@id="search-result"]/a[{i}]/div/div[3]/span[1]/b')

        year = driver.find_element_by_xpath(
            f'//*[@id="search-result"]/a[{i}]/div/div[3]/span[2]/b')

        distance = driver.find_element_by_xpath(
            f'//*[@id="search-result"]/a[{i}]/div/div[3]/span[3]')

        df = df.append({'Brand': Brand, 'Type': Type, 'year_type': year_type, 'Exhaust': Exhaust, 'Title': title.text, 'Describe': describe.text, 'Price': price.text,
                       'Year': year.text, 'Distance': distance.text}, ignore_index=True)


print(df)
df.to_csv('car.csv', encoding='utf-8-sig')
driver.close()
