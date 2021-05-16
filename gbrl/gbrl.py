import re # 정규식 
import requests as req # 웹 요청 
from bs4 import BeautifulSoup # 웹 정보 추출 
naver_cafe_url = "https://cafe.naver.com/re4mo/1513599" # 네이버 카페 주소 
naver_cafe_article = "https://cafe.naver.com/nhn?clubid=" 

url = naver_cafe_url  # https://cafe.naver.com/re4mo 
res = req.get(url=url) # URL 요청 
soup = BeautifulSoup(res.text, 'lxml') 
p_clubid = re.compile(r'var g_sClubId = \"(\w+)\"') # 정규식 설정 
clubid = p_clubid.findall(str(soup.select('script')[0]))[0] # script태그 내에서 정규식에 해당하는 정보 추출 

print(clubid)

# https://cafe.naver.com/CafeProfileView.nhn?clubid=21588277
article_url = naver_cafe_article + clubid
info_res = req.get(url=article_url)
soup = BeautifulSoup(info_res.text, 'lxml')

ths = soup.select('h3.title_text') 

print(ths)

#clubid : 13988016

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