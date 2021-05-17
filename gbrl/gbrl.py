import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get("https://m.cafe.naver.com/ArticleSearchList.nhn?search.query=%ED%94%8C%EB%9E%A9%ED%92%8B%EB%B3%BC&search.menuid=&search.searchBy=0&search.sortBy=sim&search.clubid=13988016")

response.status_code
200
dom = BeautifulSoup(response.text, "html.parser")
post_elements = dom.select("#articleList ul.list_tit li")
len(post_elements)
20
post_element = post_elements[0]

url = post_element.select_one("a").get("href")
print(url)

title = post_element.select_one("h3").text.strip()
print(title)

contents = post_element.select_one("div.post_area").text.strip()
print(contents)

data = ["title", "url", "contents"]
df = pd.DataFrame(columns=["Title", "URL"])
df

-------------------------------------------------------------------

#titles = post_elements.find_element_by_css_selector('h3').text

#for post_element in post_elements:
    #post_elements.append(h3)
#print(titles)

#for post_element in post_elements:
    #url = post_element.select_one("a").get("href")
    #title = post_element.select_one("a").text.strip()
    
    #data = {"URL": url, "Title": title, "contents" : contents}
    #df.loc[len(df)] = data   # row 에다 추가하는 부분
#df


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