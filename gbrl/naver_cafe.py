import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver

driver = webdriver.Chrome("C:/Users/SAMSUNG/Downloads/chromedriver_win32/chromedriver.exe")

driver.get("https://www.naver.com")
keyword = driver.find_element_by_name("query")

keyword.send_keys("플랩풋볼")

time.sleep(2)

driver.find_element_by_id("search_btn").click()

driver.find_element_by_xpath('//*[@id="main_pack"]/section[2]/div/div[2]/panel-list/div[1]/ul/li[1]/div[1]/div/a').click()


driver.switch_to_window(driver.window_handles[-1])

driver.switch_to.frame("cafe_main")

soups = bs(driver.page_source, 'html.parser')

title = soups.find("h3.title_text")
print(title.text)

para = soups.find_all("p")
print(para.text)