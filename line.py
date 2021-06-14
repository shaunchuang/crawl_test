from selenium import webdriver
import time
# driver = webdriver.Chrome("/Users/shaunchuang/Code_Learning/crawl_test/chromedriver")
# driver = webdriver.Chrome('./chromedriver')
driver = webdriver.Safari()
driver.maximize_window()
driver.get("https://fact-checker.line.me/category?type=verified&params=%7B%22size%22%3A12,%22sort%22%3A%7B%22updatedAt%22%3A%7B%22dir%22%3A%22desc%22,%22default%22%3Atrue%7D%7D,%22page%22%3A0%7D&displayList=true&filterType=all")
time.sleep(2)
for i in range(1,13):
    TF= driver.find_element_by_xpath(f'//*[@id="app"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/table/tbody/tr[{i}]/td[2]/div[2]/div[3]/div/div[1]/text()')
    if TF.text == '不實':
        link_in=driver.find_element_by_xpath(f'//*[@id="app"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/table/tbody/tr[{i}]/td[2]/div[2]/div[1]/div/div/span/span')
        link_in.click()
        time.sleep(2)
        content=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/h3/text()')
        hyperlink=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[2]/div[1]/div[3]/span/div/div/div[2]/div[2]/a')
        HL1=hyperlink.get_attribute('href')
        print(HL1)
        print(content.text)
        driver.back()
        time.sleep(2)


time.sleep(3)
driver.close()
# //*[@id="app"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/div[2]/div[3]/div/div[1]/text()
# //*[@id="app"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/table/tbody/tr[3]/td[2]/div[2]/div[3]/div/div[1]/text()
# //*[@id="app"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/div[2]/div[1]/div/div/span/span