import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://sports.news.naver.com/news.nhn?oid=413&aid=0000118186"
html = urlopen(url)

bs = BeautifulSoup(html ,'html.parser')
result = bs.find('h4', {'class': 'title'})
print(result.encode('utf-8').decode('utf-8'))


#urllib = url라이브러리 
#bs = BeautifulSoup
#html을 받고 그것에 접근할 수 있게 하는 함수

#select 

#find = 첫번째 위 꺼만 찾아줌
#find_all = 전체 찾아줌 + for 문 통해 찾아냄 

#git add 추가 
#commit 최종적으로 올리는 것

#git status 

#parser? , html.read?

#자바스크립트 방식 로그인. 

#주말 : 셀레니움 듣기,  