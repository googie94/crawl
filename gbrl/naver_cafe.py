import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:/Users/SAMSUNG/Downloads/chromedriver_win32/chromedriver.exe")

driver.get("https://m.search.naver.com/search.naver?where=m_article&sm=mtb_opt&query=")
keyword = driver.find_element_by_name("query")

keyword.send_keys("플랩풋볼")

time.sleep(2)

driver.find_element_by_id("nx_query").send_keys(Keys.ENTER)

driver.find_element_by_xpath('//*[@id="addParemt"]/li[1]/div[1]/a').click()

driver.switch_to.window

html = driver.page_source
soups = bs(driver.page_source, 'html.parser')

title = soups.find("h2.tit")
print(title)

para = soups.find_all("p")
print(para)

#driver.switch_to.default_content() #처음 상태로 되돌아옴

#git add --all
#git status 
#git commit -am ""
#git push origin master 