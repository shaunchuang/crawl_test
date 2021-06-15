import requests
from bs4 import BeautifulSoup
import time
import jieba
import jieba.posseg
import numpy as np
import pandas as pd
import operator
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}


def parse_html(url, headers):
    return BeautifulSoup(requests.get(url, headers=headers).text, 'lxml')


def find_article_link(soup):
    list1 = []
    # list2=[]
    divs = soup.select('div.title > a')
    # for title in divs:
    #     list2.append(title.text.strip())
    for a in divs:
        list1.append('https://www.ptt.cc'+a.get('href'))
    return list1


def content_crawler(list1, headers):
    for a in list1:
        soup = parse_html(a, headers)
        time.sleep(3)
        return soup.text.strip()


# def jieba_parsing(content):
#     jieba.set_dictionary('dict.txt.big')
#     # jieba.load_userdict('userdict.txt')
#     words = jieba.cut(content, cut_all=False)
#     break_words = []
#     for j in words:
#         break_words.append(j)
#     stopwords = []
#     for word in open('stopwords.txt', 'a', encoding='utf-8'):
#         stopwords.append(word.strip())
#     del_stopwords = []
#     for k in break_words:
#         if k not in stopwords:
#             del_stopwords.append(k)
#     df = pd.DataFrame(del_stopwords)
#     data_clean = df[df[0].str.match('focus')]
#     data_clean.columns = ['car']
#     data_clean = data_clean[data_clean.words != '\n']
#     kk = []
#     for i in range(len(data_clean)):
#         kk.append(data_clean.values[i][0])
#     word_count = dict()
#     for word in kk:
#         if word in word_count.keys():
#             word_count[word] += 1
#         else:
#             word_count[word] = 1
#     sorted_wc = sorted(word_count.items(),
#                        key=operator.itemgetter(1), reverse=True)
#     return sorted_wc


# def save_csv(dict1):
#     with open('test1.csv', 'a', newline='', encoding='utf-8') as dictfile:
#         dictfile.writerows(dict1)


for i in reversed(range(5001)):
    url = f'https://www.ptt.cc/bbs/car/index{i}.html'
    content = content_crawler(find_article_link(
        parse_html(url, headers)), headers)
    # save_csv(jieba_parsing(content))
