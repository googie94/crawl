from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
# 

html = urlopen('https://sports.news.naver.com/news.nhn?oid=413&aid=0000117830')
# b = html.read()
# print(b)
# print(b.h1)
bs = bs(html.read(), 'html.parser')
print(bs.h4.text)