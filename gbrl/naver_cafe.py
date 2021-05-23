import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(3)

# 들어가는거
driver.get('https://m.cafe.naver.com/ca-fe/home/search/articles?q=%ED%94%8C%EB%9E%A9%ED%92%8B%EB%B3%BC')
time.sleep(1)

# driver.back()

for index in range(1,480):
	time.sleep(3)
	print(index)
	print(type(index))
	index = str(index)
	print(type(index))
	# 클릭한다
	a = driver.find_element_by_xpath("//*[@id='ct']/div/div/div/div[2]/div/div/div/div[2]/div["+index+"]/div/a/div[1]/strong")
	a.click()
	time.sleep(3)
	# 가져온다
	print(driver.find_element_by_xpath('//*[@id="ct"]/div[1]/div/h2').text)
	print(driver.find_element_by_xpath('//*[@id="postContent"]/div/div/div').text)
	time.sleep(3)
	# 나간다
	driver.back()
	time.sleep(3)

driver.quit()

