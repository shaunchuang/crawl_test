import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup

async def main():
    # 開啟瀏覽器程序
    browser = await launch()
    # 用瀏覽器連到 https://pythonclock.org/ 網站
    page = await browser.newPage()
    await page.goto('https://www.abccar.com.tw/search?tab=1&SearchType=1&OrderByField=0&page=1')    

    html_doc = await page.content()
    soup = BeautifulSoup(html_doc, 'lxml')

    
    itemdiv=soup.find('div', class_='row row--10 ng-score')
    print(itemdiv)
    await browser.close()

asyncio.set_event_loop(asyncio.new_event_loop())
asyncio.get_event_loop().run_until_complete(main())