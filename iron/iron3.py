import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from openpyxl import Workbook

import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.instagram.com/')
soup = BeautifulSoup(response.text, 'html.parser')

wb = Workbook(write_only=True)
ws = wb.create_sheet('인스타그램_플랩풋볼')
ws.append(['게시물 주소', '내용', '태그'])


driver = webdriver.Chrome("/Users/iron/Documents/iron/crawl/driver/chromedriver")
driver.implicitly_wait(3)

driver.get('https://www.instagram.com/')
time.sleep(1)

driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('footballtobe11@gmail.com')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys('plab0104!')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
time.sleep(1)

driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[1]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/ul/div[1]/a').click()
time.sleep(1)
driver.fullscreen_window()
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

y = 0

for y in range(9, 18):
    post_thumbnail = driver.find_elements_by_css_selector('._9AhH0')[y]
    post_thumbnail.click()
    post_url = driver.current_url
    time.sleep(1)
    post_text = driver.find_element_by_css_selector('.C4VMK > span').text.strip()
    ws.append([post_url, post_text])
    time.sleep(1)
    close_button = driver.find_element_by_css_selector('.Igw0E > .wpO6b > .QBdPU')
    close_button.click()
    time.sleep(1)

wb.save('인스타그램_플랩풋볼.xlsx')

driver.quit()