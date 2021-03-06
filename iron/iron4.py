import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from openpyxl import Workbook

import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.instagram.com/')
soup = BeautifulSoup(response.text, 'html.parser')

driver = webdriver.Chrome("/Users/iron/Documents/iron/crawl/driver/chromedriver")
driver.implicitly_wait(1)

driver.get('https://www.instagram.com/')
driver.fullscreen_window()
time.sleep(1)

#로그인
driver.find_elements_by_css_selector('.f0n8F')[0].send_keys('footballtobe11@gmail.com')
time.sleep(1)
driver.find_elements_by_css_selector('.f0n8F')[1].send_keys('plab0104!')
time.sleep(1)
driver.find_element_by_css_selector('.Igw0E > .L3NKy').click()
time.sleep(1.5)

#검색 #플랩풋볼
driver.find_element_by_css_selector('.yWX7d')
time.sleep(0.5)
driver.find_element_by_css_selector('.LWmhU').click()
time.sleep(1)
driver.find_elements_by_css_selector('ul.OOMiW > div > a.-qQT3')[0].click()
time.sleep(2)
#last_height = driver.execute_script('return document.body.scrollHeight')

#while True:
    #driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    #time.sleep(1)

    #new_height = driver.execute_script('return document.body.scrollHeight')
    #if new_height == last_height:
        #break
    #last_height = new_height

post_text = []
texts = []
tags = []
#context = []

count_post = driver.find_element_by_css_selector('.-nal3 > .g47SY').text
last_number = int(count_post.replace(',', ''))

post_thumbnail = driver.find_elements_by_css_selector('._9AhH0')[9]
post_thumbnail.click()

#wb = Workbook(write_only=True)
#ws = wb.create_sheet('인스타그램_플랩풋볼')
#ws.append(['URL', '내용', '태그'])

for crawl in range(30):
    EC.presence_of_element_located((By.CSS_SELECTOR, '.C4VMK'))
    post_url = driver.current_url
    post_text = driver.find_element_by_css_selector('.C4VMK > span').text.strip().split()
    for text in post_text:
        if '#' in text:
            tags.append(text)
        else:
            texts.append(text)
    context = [post_url, texts, tags]
    print(context)
    next_button = driver.find_element_by_css_selector('._65Bje')
    next_button.click()
    time.sleep(1)

time.sleep(1)



driver.quit()