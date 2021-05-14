pip3 install selenium

import requests
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://m.cafe.naver.com/ca-fe/web/cafes/re4mo/articles/1521375?useCafeId=false&or=m.search.naver.com&query=%ED%94%8C%EB%9E%A9%ED%92%8B%EB%B3%BC&buid=243694f9-97c6-4793-8187-510c5b693fa8&art=ZXh0ZXJuYWwtc2VydmljZS1uYXZlci1ldGMtZm9yLWNvbW1lbnQ.eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjYWZlVHlwZSI6IkNBRkVfSUQiLCJhcnRpY2xlSWQiOjE1MjEzNzUsImlzc3VlZEF0IjoxNjIwNTUxMTM0NzE4LCJjYWZlSWQiOjEzOTg4MDE2fQ.oqMPhTIuDcsdFUvE4qJKrGR_d5phBy4tUGRCaK3-EFs"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req)

bs = BeautifulSoup(html ,'html.parser')
results = bs.find('h2', {'class': 'tit'})

print(results.text)

#urllib = url라이브러리 
#bs = BeautifulSoup
#html을 받고 그것에 접근할 수 있게 하는 함수

#select 

#find = 첫번째 위 꺼만 찾아줌
#find_all = 전체 찾아줌 + for 문 통해 찾아냄 

#변경사항 발생 시, add 먼저 하고 / am = add+commit
#git add 저장소에 올리기 전 단계 , stage 올릴때 선택하는 과정
#git status
#commit 로컬에 있는 것을 저장하는 단계 

#git pull origin master
#q!
#git push origin master 
#commit add  

#parser? , html.read?

#자바스크립트 방식 로그인. 

#주말 : 셀레니움 듣기,  
#.git 이 있어야 깃에서 관리 되는 파일
#git commit -am"gbrl" => 수정된 사항 확인 