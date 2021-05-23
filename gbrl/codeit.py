from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("C:/Users/SAMSUNG/Downloads/chromedriver_win32/chromedriver.exe") 

driver.get("https://cafe.naver.com/re4mo")    
driver.implicitly_wait(3)

driver.find_element_by_name('query').send_keys('플랩풋볼')  
driver.find_element_by_name("query").send_keys(Keys.ENTER)  # 엔터를 입력해 검색
time.sleep(2)  # 2초 대기

driver.switch_to.frame("cafe_main")

for i in range(1, 5):
    req = driver.page_source
    soup = BeautifulSoup(req, 'html.parser')
    titles = soup.select("#main-area > div:nth-child(7) > table > tbody > tr")

#main-area > div.article-board.result-board.m-tcol-c > table > tbody > tr:nth-child(2) 
#> td.td_article > div.board-list > div > a.article

#app > div > div.container > div > div.SectionSearchContent > div.section_search_content > div > div.article_list_area > ul 
# > li:nth-child(1) > div > div > div > a
    print('----' + str(i) + ' 번째 페이지 -----')
    list3 = []

    for title in titles:
        list = title.select_one(' td.td_article > div.board-list > div > a').text
        list2 = ''.join(list.split())
        list3.append(list2)

    list4_sr = pd.Series(list3)
    print(list4_sr)

    # for a in range(1, 3):
        # driver.find_element_by_xpath(f'//*[@id="main-area"]/div[5]/table/tbody/tr[{a}]/td[1]/div[2]/div/a').click()
        # time.sleep(3)
        # driver.back()
        # time.sleep(2)
        # driver.switch_to.frame("cafe_main")
        ## 게시글을 클릭하고 뒤로 돌아온 경우에는 switch로 다시 iframe을 선택해 주어야 한다.
    if i<4:
        driver.find_element_by_xpath(f'//*[@id="main-area"]/div[7]/a[{i}+1]').click()
        # 결과 다음 페이지로 가는 구문, 다음페이지로 간 경우 iframe 은 선택 되어 있으므로
        # 스위치를 안써줘도 된다.

