import time
import re
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
time.sleep(1)

driver.find_elements_by_css_selector('.f0n8F')[0].send_keys('footballtobe11@gmail.com')
time.sleep(1.5)
driver.find_elements_by_css_selector('.f0n8F')[1].send_keys('plab0104!')
time.sleep(1.5)
driver.find_element_by_css_selector('.Igw0E > .L3NKy').click()
time.sleep(1)

driver.find_element_by_css_selector('.yWX7d')
time.sleep(1.5)
driver.find_element_by_css_selector('.LWmhU').click()
time.sleep(1)
driver.find_elements_by_css_selector('ul.OOMiW > div > a.-qQT3')[0].click()
time.sleep(1)
driver.fullscreen_window()
time.sleep(1.5)

post_thumbnail = driver.find_elements_by_css_selector('._9AhH0')[9]
post_thumbnail.click()

for crawl in range(3):
    EC.presence_of_element_located((By.CSS_SELECTOR, '.C4VMK'))
    date = driver.find_element_by_css_selector('.c-Yi7 > ._1o9PC').get_attribute('title')
    post_url = driver.current_url
    try:
        post_text = driver.find_elements_by_css_selector('div.C4VMK > span')[0].text.strip()
    except:
        post_text = ''
    pure_text = post_text.split()
    only_text = re.sub('\ |\?|\.|\!|\/|\;|\:', '', pure_text)

    tags = tags = re.findall(r'#[^\s#,\\]+', post_text)

    #try:
        #tags = driver.find_elements_by_css_selector('.C4VMK > span > a')[1:].text
    #except:
        #tags = ''
    try:
        likes = driver.find_element_by_css_selector('.Nm9Fw > a.zV_Nj > span').text
    except:
        likes = ''
    try:
        comment = driver.find_elements_by_css_selector('.C4VMK > span')[1].text.stip().split()
    except:
        comment = ''
    context = [date, post_url, only_text, tags, likes]
    print(context)
    next_button = driver.find_element_by_css_selector('._65Bje')
    next_button.click()
    time.sleep(2)

