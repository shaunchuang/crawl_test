
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import sys


log = 'check_in_log.csv'


def writecsv(log, message):
    with open(log, 'a', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([message])


def date_check():
    a = datetime.now().strftime('%d')
    inta = int(a)
    # print(inta)
    # inta=7
    list2 = [1, 2, 6, 7, 8, 9, 10, 11, 12, 15, 17, 21, 22, 23, 26, 28, 29, 30, 31]
    
    if inta in list2:
        return True
    else:
        return False


def to_line(message):
    try:
        headers = {
            "Authorization": "Bearer " + "wAjixamOyIoL3uSXnF6rpWUGpzlSo7v94hLkOfTyq0q",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        params = {"message": message}
        r = requests.post("https://notify-api.line.me/api/notify",
                          headers=headers, params=params)
        if r.status_code == 200:
            print("傳送line通知成功")
        else:
            raise Exception('傳送line通知失敗')
    except Exception as err:
        writecsv(log, err)


def parse_html(htmlfile):
    soup = BeautifulSoup(htmlfile.text, 'lxml')
    tag_p = soup.find_all('p')
    list1 = []
    for time in tag_p:
        list1.append(time.text)
    return list1[2]
# def parse_html(htmlfile):
#     list=[]
#     soup = BeautifulSoup(htmlfile.text,'lxml')
#     tag_p = soup.find('title')
#     list.append(tag_p)
#     return list[0]





url = 'https://manage.iiiedu.org.tw/api/class/remoteAttendance?qrcode=eyJjbGFzc0lEIjoiSkpCRFNFVDIxMDkiLCJFbWFpbCI6InpodXNoYXVuOTIwQGdtYWlsLmNvbSIsIk5hbWUiOiLojormlL_nhYoiLCAiY3VzdG9tZXJTTiI6IjIwMDkxMzE2MDgwNyIsIklzTWVhdExlc3MiOiJOIn0'
if __name__ == '__main__':
    if(date_check()):
        try:
            htmlfile = requests.get(url)
            if htmlfile.status_code == requests.codes.ok:
                print("打卡成功")
            else:
                raise Exception('打卡失敗')
        except Exception as err:
            writecsv(log, err)

        message = parse_html(htmlfile)
        to_line(message)

        writecsv(log, message)
    else:
        sys.exit()
