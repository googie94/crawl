import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook

driver = webdriver.Chrome("/Users/iron/Documents/iron/crawl/driver/chromedriver")
driver.implicitly_wait(3)

driver.get('https://www.instagram.com/')
time.sleep(1)

driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('footballtobe11@gmail.com')
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys('plab0104!')
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
time.sleep(1)

driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[1]').click()
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/ul/div[1]/a').click()
time.sleep(3)

wb = Workbook(write_only=True)
ws =wb.create_sheet()
ws.append(['이미지 주소'])

x = 1
y = 1

while x < 9:
    for y in range(1, 4):
        post_selector = '#react-root > section > main > article > div:nth-child(3) > div > div:nth-child({}) > div:nth-child({}) > a'.format(x, y)
        post_url = driver.find_element_by_css_selector(post_selector).get_attribute('href').text.strip()
        ws.append(post_url)
    x += 1

driver.quit()

wb.save('해시태그_플랩풋볼.xlsx')