from konlpy.tag import Okt
okt = Okt()

print(okt.pos('아버지가 방에 들어가신다'))
print(okt.pos('아버지가방에들어가신다'))


# import time
# from selenium import webdriver
# from openpyxl import Workbook

# from selenium.common.exceptions import NoSuchElementException
# wb = Workbook(write_only=True)
# ws = wb.create_sheet('블로그글')

# ws.append(['제목', '내용', '작성일'])

# driver = webdriver.Chrome("C:/Users/SAMSUNG/Downloads/chromedriver_win32/chromedriver.exe")
# driver.implicitly_wait(3)

# # 들어가는거
# driver.get('https://m.blog.naver.com/SectionPostSearch.naver?orderType=sim&searchValue=%ED%94%8C%EB%9E%A9%ED%92%8B%EB%B3%BC')
# time.sleep(4) 

# #현 scrollheight 가져오기
# last_height = driver.execute_script("return document.body.scrollHeight")

# while True:
#     # scrollHeight까지 스크롤
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(1)

#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#     	break 
#     last_height = new_height
    
# for index in range(52,100):
# 	time.sleep(3)
# 	print(index)
# 	print(type(index))
# 	index = str(index)
# 	print(type(index))
# 	# 클릭한다
# 	try:
# 		a = driver.find_element_by_xpath("//*[@id='root']/div[2]/div[2]/div[2]/div/div[2]/div["+index+"]/div/a/div[2]/strong")
# 		driver.execute_script("arguments[0].click();", a)
# 		time.sleep(3)

# 		title = driver.find_element_by_css_selector("div.se-module.se-module-text.se-title-text").text
# 		contents = driver.find_element_by_class_name("se-main-container").text
# 		write_time = driver.find_element_by_class_name("blog_date").text

# 		print(title)
# 		print(contents)
# 		print(write_time)

# 		time.sleep(4)
# 		driver.back()

# 		time.sleep(4)
# 		ws.append([title, contents, write_time])
	
# 	except NoSuchElementException:
# 		print('NO FOUND')

# driver.quit()

# wb.save('블로그글.xlsx')
