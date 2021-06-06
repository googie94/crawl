
# py my_instagram.py

# from selenium import webdriver
# from bs4 import BeautifulSoup
# from tqdm import tqdm
# import time

# driver = webdriver.chrome()
# driver.implicitly_wait(3)

# driver.get('https://www.instagram.com/explore/tags/%ED%94%8C%EB%9E%A9%ED%92%8B%EB%B3%BC/')
# time.sleep(3)

# from selenium import webdriver
# driver = webdriver.Chrome('C:/Users/user/crawl/meoru')

# Selenium 임포트
from selenium import webdriver

# etc
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from tqdm.notebook import tqdm
import requests
import time
import sys
import io
import codecs
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
# sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


# 크롬 드라이버 생성
driver = webdriver.Chrome('C:/Users/user/crawl/meoru/chromedriver.exe')
driver.implicitly_wait(3)

# 들어가는거
# keyword = input('무엇을 검색할까요? ')
keyword = '플랩풋볼'
driver.get('https://www.instagram.com/')
time.sleep(3)
# driver.get(f'https://www.instagram.com/explore/tags/{keyword}')

# 로그인
# id = input('id? ')
# ps = input('password? ')
id = ''
ps = ''

# 로그인 시도
# login = driver.find_element_by_css_selector('#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg > div > div > div > div > div.Igw0E.IwRSH.eGOV_.vwCYk.M2CRh > div:nth-child a')
# login.click()

id_cell = driver.find_element_by_css_selector('#loginForm > div > div:nth-child(1) > div > label > input')
ps_cell = driver.find_element_by_css_selector('#loginForm > div > div:nth-child(2) > div > label > input')

id_cell.click()

id_cell.send_keys(id)
ps_cell.send_keys(ps)

enter = driver.find_element_by_css_selector('#loginForm > div > div:nth-child(3) > button')
enter.click()

time.sleep(5)

# 플랩풋볼 드가기
driver.get(f'https://www.instagram.com/explore/tags/{keyword}')
time.sleep(3)

# # 파싱
# url = driver.current_url
# print(url)
# res = requests.get(url)
# soup = BeautifulSoup(res.content, 'html.parser')
# print(soup)

# # 본문 url 수집
# cont_lst = soup.find_all('div', {'class': 'v1Nh3 kIKUG  _bz0w'})
# for i in cont_lst:
# 	print(i)

# 본문 클릭해서 들어가기
body_list = driver.find_elements_by_css_selector('#react-root > section > main > article > div.EZdmt div._9AhH0')
# print(body_list)
for body in body_list:
	print(body)
	body.click()

	cont = driver.find_elements_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > div.EtaWk > ul div.C4VMK > span')
	print(cont[0].text)

	hash_lst = driver.find_elements_by_css_selector('div.C4VMK > span > a')
	for hash in hash_lst:
		print(hash.text)

	imgs_lst = driver.find_elements_by_css_selector('div.eLAPa._23QFA > div.KL4Bh')
	for imgs in imgs_lst:
		print(imgs.img['src'])
	# for cont in cont_list:
	# 	print(cont.text)

	# 다음 버튼
	next_lst = driver.find_elements_by_css_selector('div._2dDPU.CkGkG > div.EfHg9 a')

	a = 1

	while len(next_lst) > 0:

		# print(len(next_lst))

		for next in next_lst:
			print(f'{a}_page')
			# print('next_page')
			next.click()

			driver.implicitly_wait(3)

			try:
				cont = driver.find_elements_by_css_selector('ul div.C4VMK > span')
				print(cont[0].text)
			except:
				print('no_content')

			try:
				hash_lst = driver.find_elements_by_css_selector('div.C4VMK > span > a')
				for hash in hash_lst:
					print(hash.text)

			except:
				print('no_hash')

			try:
				imgs_lst = driver.find_elements_by_css_selector('div.eLAPa._23QFA > div.KL4Bh')
				for imgs in imgs_lst:
					print(imgs.img['src'])
			except:
				print('no_img')

			a += 1






	# for row in body:
	# 	print(row)
	# 	post = row.find_elements_by_css_selector('#react-root > section > main > article > div.EZdmt div.v1Nh3 kIKUG  _bz0w')
	# 	print(post)
	# 	post.click()
	# posts = i.find_elements_by_css_selector('a.xil3i')
	# for post in posts:
	# 	print(post)


# for i in cont_url:
# 	print(i)
# 	print(i.attrs['href'])
# # res = urlopen(url)

# time.sleep(3)

# soup = BeautifulSoup(res, 'html.parser')

# time.sleep(3)

# data = soup.select('#react-root > section > main > article > div.EZdmt > div > div a > div.eLAPa > div._9AhH0')
# for item in data:
#     print(item.get_text())





# # 게시물 하나씩
# content = driver.find_element_by_css_selector('#react-root > section > main > article > div.EZdmt > div > div a > div.eLAPa > div._9AhH0')
# content.click()

# # user
# user = driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > div.EtaWk > ul > div > li > div > div > div.C4VMK > h2 > div > span > a')
# print(user)

# # 본문
# cont_lst = driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > div.EtaWk > ul > div > li > div > div > div.C4VMK > span')
# for cont in cont_lst:
# 	print(cont)



# # html 가져오기
# url = driver.current_url
# print(url)
# html = requests.get(url)
# print(html)

# soup = BeautifulSoup(html.text, 'html.parser') 

# # print(soup)
# cont_lst = soup.select('#react-root > section > main > article > div.EZdmt > div > div a')
# for cont in cont_lst:
# 	print(cont)

# 	react-root > section > main > article > div.EZdmt > div > div > div:nth-child(1) > div:nth-child(1) > a


# cont_lst = soup.select_all('div', class_ = '_9AhH0')

# for cont in cont_lst:
# 	print(cont.text)