import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://cafe.naver.com/re4mo/1509801"
html = urlopen(url)

bs = BeautifulSoup(html ,'html.parser')
result = bs.find('h3', {'class': 'title_text'})

print(result.text)

contents = bs.find('div', {'class' : 'se-module se-module-text'})

print(contents.text)
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
