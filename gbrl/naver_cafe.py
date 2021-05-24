import time
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook

wb = Workbook(write_only=True)
ws = wb.create_sheet('카페글')
ws.append(['제목', '내용'])

driver = webdriver.Chrome("C:/Users/SAMSUNG/Downloads/chromedriver_win32/chromedriver.exe")
driver.implicitly_wait(3)

# 들어가는거
driver.get('https://m.cafe.naver.com/ca-fe/home/search/articles?q=%ED%94%8C%EB%9E%A9%ED%92%8B%EB%B3%BC')
time.sleep(1)

#현 scrollheight 가져오기
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # scrollHeight까지 스크롤
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
    	break 
    last_height = new_height

#total = 

for index in range(1,5):
	time.sleep(2)
	print(index)
	print(type(index))
	index = str(index)
	print(type(index))
	# 클릭한다
	a = driver.find_element_by_xpath("//*[@id='ct']/div/div/div/div[2]/div/div/div/div[2]/div["+index+"]/div/a/div[1]/strong")
	
	driver.execute_script("arguments[0].click();", a)
	time.sleep(2)
	# 가져온다
#>>>>>> 84a942792f08b2426861d9b440d7b54fa85bc018

	title = driver.find_element_by_xpath('//*[@id="ct"]/div[1]/div/h2').text
	contents = driver.find_element_by_xpath('//*[@id="postContent"]/div/div/div').text
	print(title)
	print(contents)
	time.sleep(3)
	# 나간다
	driver.back()
	time.sleep(2)
	ws.append([title, contents])

driver.quit()
wb.save('카페글.xlsx')

#댓글 ,글, 뎃글의 작성일 
#해야할 것 : 스크롤 끝까지 내리기. 전체 몇개인지 파악하기. 
#csv 저장 