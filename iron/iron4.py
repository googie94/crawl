import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from openpyxl import Workbook

import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.instagram.com/')
soup = BeautifulSoup(response.text, 'html.parser')

#wb = Workbook(write_only=True)
#ws = wb.create_sheet('인스타그램_플랩풋볼')
#ws.append(['URL', '내용', '태그'])


driver = webdriver.Chrome("/Users/iron/Documents/iron/crawl/driver/chromedriver")
driver.implicitly_wait(1)

driver.get('https://www.instagram.com/')
time.sleep(1)

driver.find_elements_by_css_selector('.f0n8F')[0].send_keys('footballtobe11@gmail.com')
time.sleep(1)
driver.find_elements_by_css_selector('.f0n8F')[1].send_keys('plab0104!')
time.sleep(1)
driver.find_element_by_css_selector('.Igw0E > .L3NKy').click()
time.sleep(1)

driver.find_element_by_css_selector('.yWX7d')
time.sleep(0.5)
driver.find_element_by_css_selector('.LWmhU').click()
time.sleep(1)
driver.find_elements_by_css_selector('ul.OOMiW > div > a.-qQT3')[0].click()
time.sleep(1)
driver.fullscreen_window()
time.sleep(1)
#last_height = driver.execute_script('return document.body.scrollHeight')

#while True:
    #driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    #time.sleep(1)

    #new_height = driver.execute_script('return document.body.scrollHeight')
    #if new_height == last_height:
        #break
    #last_height = new_height

y = 0
post_text = []
texts = []
tags = []
#context = []
#count_post = driver.find_element_by_css_selector('span.g47SY').text
#last_number = int(count_post.replace(',', ''))

post_thumbnail = driver.find_elements_by_css_selector('._9AhH0')[9]
post_thumbnail.click()

#여기서부터 반복문을 돌리고 싶다. 다음 버튼을 누르고, url과 내용, 태그를 차례로 수집. 다 수집하면 다음 버튼 클릭. url과 내용, 태그를 수집
post_url = driver.current_url
post_text = driver.find_element_by_css_selector('.C4VMK > span').text.strip().split()
for text in post_text:
    if '#' in text:
        tags.append(text)
    else:
        texts.append(text)
    #ws.append([post_url, texts, tags])
context = [post_url, texts, tags]
next_button = driver.find_element_by_css_selector('._65Bje')
next_button.click()

time.sleep(1)

print(context)

driver.quit()