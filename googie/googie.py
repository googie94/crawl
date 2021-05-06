from urllib.request import urlopen, Request
import requests
# 
from bs4 import BeautifulSoup
from selenium import webdriver
# 
import time
# # 사용자 인증서 필요
import  os, ssl
if  ( not  os.environ.get ( 'PYTHONHTTPSVERIFY', '') and getattr (ssl, '_create_unverified_context', None)) : 
	ssl._create_default_https_context =  ssl._create_unverified_context

# # 한글 키워드 인코드(귀멸의 칼날)
# keyword = '%EA%B7%80%EB%A9%B8%EC%9D%98%20%EC%B9%BC%EB%82%A0'
# keyword.encode('utf-8')
# url = 'https://namu.wiki/w/'+keyword

# # 나무위키에서는 유저 정보가 없으면 막고 있는 것 같음. 유저 정보를 헤더에 담아 요청을 보냄
# req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})


# # 위에 내용은 신경쓰지 않아도 됩니다. 이번주 하기로 한 것에만 집중하면 됩니다.
# html = urlopen(req)
# bs = bs(html.read(), 'html.parser')
# print(bs)

# ========================================



url = 'https://blog.naver.com//PostView.nhn?blogId=nam4510&logNo=222301794649&redirect=Dlog&widgetTypeCall=true&directAccess=false'
html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')
title = bs.find('span', {'class': 'se-fs- se-ff-nanummaruburi'}).text
print('===============제목===============')
print(title)
print('===============내용===============')
for content in bs.findAll('span', {'class': 'se-fs- se-ff-nanummaruburi'}):
	print(content.get_text())


# ========================================


# driver = webdriver.Chrome()
# driver.implicitly_wait(3)

# # GET URL

# keyword = '%ED%94%8C%EB%9E%A9%ED%92%8B%EB%B3%BC'
# keyword.encode('utf-8')
# url = 'https://m.cafe.naver.com/ca-fe/web/cafes/re4mo/articles/1513599?useCafeId=false&query='+keyword+'&buid=8957b977-a4ae-4cae-b947-5d0be546d7db&art=ZXh0ZXJuYWwtc2VydmljZS1uYXZlci1ldGMtZm9yLWNvbW1lbnQ.eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjYWZlVHlwZSI6IkNBRkVfSUQiLCJhcnRpY2xlSWQiOjE1MTM1OTksImlzc3VlZEF0IjoxNjIwMjUzNDExMDIzLCJjYWZlSWQiOjEzOTg4MDE2fQ.0tXAbmqJXxSb_RLm4lml8pJyUghH6BkQyh44tUNnAT8'
# driver.get(url)


# # FUNCTIONS
# def clickSelector(path):
# 	item = driver.find_element_by_css_selector(path)
# 	item.click()

# # clickSelector('a.total_dsc')
# # driver.implicitly_wait(10)
# content = driver.find_element_by_css_selector('#ct > div:nth-child(1) > div > h2')
# print(content.text)
# time.sleep(3)
# driver.quit()


































