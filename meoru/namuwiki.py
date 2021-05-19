# find, find_all 활용

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
import requests
import time
import re

# 사용자 인증서 필요
import  os, ssl
if  ( not  os.environ.get ( 'PYTHONHTTPSVERIFY', '') and getattr (ssl, '_create_unverified_context', None)) : 
    ssl._create_default_https_context =  ssl._create_unverified_context

# 한글 키워드 인코드(귀멸의 칼날)
keyword = '%EA%B7%80%EB%A9%B8%EC%9D%98%20%EC%B9%BC%EB%82%A0'
keyword.encode('utf-8')
url = 'https://namu.wiki/w/'+keyword

namu_html = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

namu_soup = bs(namu_html.text, "html.parser")
namu_soup

content = ''

# table = namu_soup.select('#app > div article div.wiki-table-wrap.table-center > table > tbody > tr strong')
# print(table)

# content_lst = namu_soup.find_all('span', class_ ='wiki-color wiki-dynamic-f40ad4f4303238e4bd0706d6a7af7317')
a = 0
content_lst = namu_soup.select('#app > div article div.wiki-table-wrap.table-center > table > tbody div > strong > span')
for content in content_lst:
#     print(content)
    a += 1
    while a >= 5:
        print(content.text)
#     if a == 8:
#         print(content.text)
#         a = 0
            
#         for i in content:
#             print(i.text)
#     for i in range(0,3):
#     if len(i.text) > 3:
#         print(i)
# for i in table:
#     content_lst = i.find('span', class_ ='wiki-color wiki-dynamic-f40ad4f4303238e4bd0706d6a7af7317')
#     print(content_lst)
#     for cont in content_lst:
#         print('내용 : ' + cont.text)

# for cont in content_lst:
#     print('내용 : ' + cont.text)