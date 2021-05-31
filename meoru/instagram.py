from selenium import webdriver
from bs4 import BeautifulSoup
from tqdm import tqdm
from urllib.request import urlopen
import re
import pandas as pd
import time
import sys

def PAGE_DOWN():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    
keyword = input("인스타그램에서 원하는 검색어를 입력하세요: ")
count_down = int(input('스크롤 다운 횟수를 입력하세요(정수입력):'))

driver = webdriver.Chrome("C:\dev_python\Webdriver\chromedriver.exe")
driver.get("https://www.instagram.com/")
time.sleep(3)
id_ = ''
pw = ''
# 로그인 
id_input = driver.find_element_by_css_selector('#loginForm > div > div:nth-child(1) > div > label > input')
id_input.send_keys(id_)
password_input = driver.find_element_by_css_selector('#loginForm > div > div:nth-child(2) > div > label > input')
password_input.send_keys(pw)
driver.find_element_by_css_selector("#loginForm > div > div:nth-child(3)").click()
time.sleep(3)
state = input('로그인이 잘 되었나요?[y/n]:')
if state == 'n' or state == 'N' or state == 'ㅜ':
    print('종료합니다.')
    driver.close()
    sys.exit()
else:
    pass
# 검색어 결과 페이지로 이동
url = 'https://www.instagram.com/explore/tags/'
driver.get(url+keyword)
time.sleep(3)
body = driver.find_element_by_tag_name('body')

    
# 하이퍼 링크 추출
link_url_lst = []
for down in range(count_down):
    PAGE_DOWN()
    contents_lst = body.find_elements_by_class_name('v1Nh3')
    # 게시글 리스트 생성
    try:
        for contents_url in contents_lst:
            link_url = contents_url.find_element_by_tag_name('a').get_attribute('href')
            link_url_lst.append(link_url)
        link_url_lst = list(set(link_url_lst))
    except:
        print('게시글 리스트 에러')
        pass


id_lst=[]
cont_lst=[]
hash_tag=[]
like_lst=[]
comt_lst=[]
img_lst=[]

n=1
for link_url in tqdm(link_url_lst, '크롤링중'):
    # 본문 없는경우 첫번째 댓글을 무조건 본문으로 간주
    driver.get(link_url)
    time.sleep(3)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    # ID
    try:
        user_id = soup.find(class_='sqdOP').get_text()
        id_lst.append(user_id)
    except:
        continue
        
    # 이미지
    try:
#         for i in imgs:
#             print(i )
#             imgUrl = i['data-source']
#             with urlopen(imgUrl) as f:
        imgs = soup.find(class_='KL4Bh').img['src']
        img_lst.append(imgs)
        print(imgs)
        with urlopen(imgs) as f:
            with open('./crawl/image/img' + str(n)+'.jpg','wb') as h: # w - write b - binary
                img = f.read()
                h.write(img)
#             with open('./'+'jpg', 'wb') as p:
#                 img = q.read()
#                 p.write(img) 
                n += 1
    except:
        img_lst.append('동영상')

    
    # 무조건 첫번째 있는 글은 본문으로 규정
    class_C4VMK = soup.find_all('div',class_='C4VMK')
    doc = soup.select('div.C4VMK > span')[0].text
    doc = re.sub('[^0-9a-zA-Zㄱ-ㅣ가-힣!? ]',"",doc)
    cont_lst.append(doc)

    # 해시태그
    tags = soup.select('div.C4VMK > span > a')
    temptag_lst=[]
    for tag in tags:
        temptag_lst.append(re.sub('[^0-9a-zA-Zㄱ-ㅣ가-힣!?]',"",tag.text))
    hash_tag.append(temptag_lst)

    # 좋아요
    try:
        like = soup.find('div',class_='Nm9Fw').find('span').text
        like = int(like.replace(",",""))
    except:
        like = 0
    like_lst.append(like)
    # 댓글
    try:
        comt_tag = soup.select('div.C4VMK > span')
        comt = ''
        for i in range(1,len(comt_tag)):
            comt = comt + ' ' + comt_tag[i].text
            comt = re.sub('[^0-9a-zA-Zㄱ-ㅣ가-힣!?]',"",comt)
    except:
        comt = ''
    comt_lst.append(comt)

    
data_df=pd.DataFrame({'아이디':id_lst,'본문':cont_lst,'해시태그':hash_tag,
                      '좋아요':like_lst,'댓글':comt_lst, '이미지':img_lst})
driver.close()
data_df.to_csv("./"+keyword+"_instagram_crawling.csv",encoding="cp949")
print("./"+keyword+"_instagram_crawling.csv에 저장 완료!")
data_df