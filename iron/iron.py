import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#options = Options()
#options.add_argument("--headless")
#options.add_argument("window-size=1920,1080")

driver = webdriver.Chrome("/Users/iron/Documents/iron/crawl/driver/chromedriver") #,options=options
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
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/ul/div[1]/a').click()
time.sleep(3)

post_urls = []

x = 1
y = 1

while x < 9:
    for y in range(1, 4):
        post_selector = '#react-root > section > main > article > div:nth-child(3) > div > div:nth-child({}) > div:nth-child({}) > a'.format(x, y)
        post_url = driver.find_element_by_css_selector(post_selector).get_attribute('href')
        post_urls.append(post_url)
    time.sleep(1)
    x += 1

print(post_urls)

driver.quit()