from selenium import webdriver
import time
import pandas as pd
# driver = webdriver.Chrome("/Users/shaunchuang/Code_Learning/crawl_test/chromedriver")
# driver = webdriver.Chrome('./chromedriver')
xpath1 = '//*[@id="app"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/table/tbody'
xpath2 = '//*[@id="app"]/div[2]/div[2]/div[2]/div[1]'
url1 = 'https://fact-checker.line.me/category?type=verified&params=%7B%22size%22%3A12,%22sort%22%3A%7B%22updatedAt%22%3A%7B%22dir%22%3A%22desc%22,%22default%22%3Atrue%7D%7D,%22page%22%'
#     https://fact-checker.line.me/category?type=verified&params=%7B%22size%22%3A12,%22sort%22%3A%7B%22updatedAt%22%3A%7B%22dir%22%3A%22desc%22,%22default%22%3Atrue%7D%7D,%22page%22%3A0%7D&displayList=true&filterType=all
#  {'Verified_url':'www.google.com', 'Reliabililty':'NO', 'Fake_content':'test'},index=[0]


driver = webdriver.Safari()
driver.maximize_window()
df = pd.DataFrame(columns=['Verified_url', 'Reliability', 'Fake_content'])

for page in range(1):
    url = url1+f'3A{page}%7D&displayList=true&filterType=all'
    driver.get(url)
    time.sleep(2)

    for a in range(1, 13):
        TOF = driver.find_element_by_xpath(
            xpath1+f'/tr[{a}]/td[2]/div[2]/div[3]/div/div[1]/text()')
        TOF = str(TOF.text).strip()
        link_in = driver.find_element_by_xpath(
            xpath1+f'/tr[{a}]/td[2]/div[2]/div[1]/div/div/span/span')
        link_in.click()
        time.sleep(2)
        content = driver.find_element_by_xpath(
            xpath2+'/div[2]/div[1]/h3/text()')
        content = str(content.text).strip()

        hyperlink = driver.find_element_by_xpath(
            xpath2+'/div[3]/span/div/div/div[2]/div[2]/a')
        HL1 = hyperlink.get_attribute('href')
        # if df.empty:
        #     df = pd.DataFrame({'Verified_url':hyperlink,'Reliability':TOF,'Fake_content':content}, index=[0])
        # else:
        # temp_dict=dict({'Verified_url':hyperlink,'Reliability':TOF,'Fake_content':content})
        df = df.append({'Verified_url': HL1, 'Reliability': TOF,
                       'Fake_content': content}, ignore_index=True)

        driver.back()
        time.sleep(2)
print(df)
driver.close()
# //*[@id="app"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/div[2]/div[3]/div/div[1]/text()
# //*[@id="app"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/table/tbody/tr[3]/td[2]/div[2]/div[3]/div/div[1]/text()
# //*[@id="app"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/div[2]/div[1]/div/div/span/span
# https://fact-checker.line.me/category?type=verified&params=%7B%22size%22%3A12,%22sort%22%3A%7B%22updatedAt%22%3A%7B%22dir%22%3A%22desc%22,%22default%22%3Atrue%7D%7D,%22page%22%3A0%7D&displayList=true&filterType=all
# https://fact-checker.line.me/category?type=verified&params=%7B%22size%22%3A12,%22sort%22%3A%7B%22updatedAt%22%3A%7B%22dir%22%3A%22desc%22,%22default%22%3Atrue%7D%7D,%22page%22%3A1%7D&displayList=true&filterType=all
