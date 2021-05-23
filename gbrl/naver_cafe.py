import time
from selenium import webdriver

driver = webdriver.Chrome('C:/Users/SAMSUNG/Downloads/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(3)

driver.get('https://m.cafe.naver.com/ca-fe/home/search/articles?q=%ED%94%8C%EB%9E%A9%ED%92%8B%EB%B3%BC')
time.sleep(1)

driver.find_element_by_xpath('//*[@id="ct"]/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/a/div[1]/strong').click()

print(driver.find_element_by_xpath('//*[@id="ct"]/div[1]/div/h2').text)
print(driver.find_element_by_xpath('//*[@id="postContent"]/div/div/div').text)

driver.back()



for i in range(1,5):
	print(i)
	click = driver.find_element_by_css_selector('#ct > div > div > div > div:nth-child(2) > div > div > div > div.SearchResultsListItemContainer.list_item_container.article_list > div:nth-child({}) > strong').format(i)
	click.click()
	print(driver.find_element_by_xpath('//*[@id="ct"]/div[1]/div/h2').text)
	print(driver.find_element_by_xpath('//*[@id="postContent"]/div/div/div').text)
	driver.back()


driver.quit()

