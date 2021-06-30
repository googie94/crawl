# 게시글 날짜 b
# 계정 이름 b
# likes 오류 해결... (빼자)
# 태그 테이블은 따로 만들기
# 하루날짜(범위 내) 게시글 뽑기
# 이미지 



# py my_instagram.py

# from selenium import webdriver
# from bs4 import BeautifulSoup
# import time

# driver = webdriver.chrome()
# driver.implicitly_wait(3)

# driver.get('https://www.instagram.com/explore/tags/%ED%94%8C%EB%9E%A9%ED%92%8B%EB%B3%BC/')
# time.sleep(3)

# from selenium import webdriver
# driver = webdriver.Chrome('C:/Users/user/crawl/meoru')

import pymysql

# Selenium 임포트
from selenium import webdriver

# etc
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from tqdm.notebook import tqdm
import requests
import time
import re
import sys
import io
import codecs
import datetime
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
# sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# SQL에 담기
host = 'sego.c3jqlg47t2v5.ap-northeast-2.rds.amazonaws.com'
user = 'sego_admin'
pw = 'googie0126!'
db = 'sego'
conn = pymysql.connect(host=host, user=user, passwd=pw, db=db, charset='utf8')
cur = conn.cursor()
cur.execute('USE scraping')
def store_post(code, content, likes, hashtag):
	cur.execute(
		'INSERT INTO meoru_gram (code, content, likes, hashtag) VALUES (%s, %s, %s, %s)',
		(code, content, likes, hashtag)
	)
	cur.connection.commit()

# host = 'sego.c3jqlg47t2v5.ap-northeast-2.rds.amazonaws.com'
# user = 'sego_admin'
# pw = 'googie0126!'
# db = 'sego'
# conn = pymysql.connect(host=host, user=user, passwd=pw, db=db, charset='utf8')
# cur = conn.cursor()
# cur.execute('USE scraping')
# def store_post(post_id, category, title, content, created_date, link):
# 	cur.execute(
# 		'INSERT INTO naver_post (post_id, category, title, content, created_date, link) VALUES (%s, %s, %s, %s, %s, %s)',
# 		(post_id, category, title, content, created_date, link)
# 	)
# 	cur.connection.commit()



print('한글 GKSRMF')
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
id = 'dpwls031@naver.com'
ps = 'miligram!'

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
time.sleep(2)

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
bodys = driver.find_elements_by_css_selector('#react-root > section > main > article > div.EZdmt div._9AhH0')
# print(body_list)
# print(bodys)

for body in bodys:
	# print(body)
	body.click()

	# 첫 게시글
	print(f'='*20 + 'post 1' + '='*20)

	# 첫 게시글 코드
	print('==GET CODE')
	# f_codes = driver.find_elements_by_css_selector('div._2z6nI > article div a')
	# //*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[3]/div[1]/a	print(f_codes)	
	driver.switch_to.window(driver.window_handles[-1])
	driver.implicitly_wait(3)
	url = driver.current_url
	f_code = url[-12:-1]
	print(f_code)
	code = f_code
	# res = requests.get(url)
	# soup = BeautifulSoup(res.content, 'html.parser')
	# print(soup)

	#react-root > section > main > div > div._2z6nI > article > div:nth-child(1) > div > div:nth-child(3) > div:nth-child(1) > a

	# f_codes = soup.find_all(attrs={'class':'a'})
	# print(f_codes)
	# for i in f_codes:
	# 	print(i[href])



	# a = driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[3]/div[1]/a	print(f_codes)').click()
	# f_codes = driver.get(a[0].get_attribute('href'))
	# print(f_codes)
	# for f_code in f_codes:
	# 	print(f_code)
	# 	print('-----')
	# 	print(f_code.text)
	# 	print('-----')
	# 	# code = driver.find_elements_by_css_selector('a[href]')
	# 	# print(code)
	# 	# print('-----')
	# 	print(f_code['href'])

	# 첫 게시글 이름
	print('==GET NAME')
	name = driver.find_elements_by_css_selector('div.o-MQd a.sqdOP')
	# print(name)
	for n in name:
		print(n.text)

	# 게시글 내 본문
	print('==GET CONTENET')
	cont = driver.find_elements_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > div.EtaWk > ul div.C4VMK > span')
	print(cont[0].text)
	content = cont[0].text

	# date_sel_2 = driver.find_elements_by_css_selector('div.k_Q0X.I0_K8.NnvRN > a > time')
	# for t in date_sel_2:
	# 	print(t['datetime'])

	# # 좋아요 잠깐 제거
	# print('==GET LIKE')	
	# try:
	# 	like_lst = driver.find_elements_by_css_selector('section.EDfFK.ygqzn a > span')
	# 	for like in like_lst:
	# 		likes = like.text
	# 		print(likes)

	# except:
	# 	likes = 'no_like'
	# 	print(likes)

	# 해시태그
	print('==GET TAG')
	hashs = driver.find_elements_by_css_selector('div.C4VMK > span > a')
	hash_lst = []
	# print(hashs.text)
	try:
		for hash in hashs:
			# print(hash.text)
			# 정규화
			hash = re.sub('[^0-9a-zA-Zㄱ-ㅣ가-힣!?]', "", hash.text)
			hash_lst.append(hash)
		print(hash_lst)

		hashtag = hash_lst
		for tag in hash_lst:
			print(code + ' ' + tag)
			# hash_lst.append(hash)

	except:
		hash_lst.append('no_hash')
		hashtag = hash_lst


	# 첫 게시글 날짜
	html = driver.page_source
	soup = BeautifulSoup(html, 'html.parser')

	print('==GET DATE')
	
	date = soup.select('time._1o9PC.Nzb55')
	for d in date:
		dt = d['datetime'][:10]
		print(dt)

	# 이미지 시도
	# imgs = driver.find_elements_by_css_selector('div.eLAPa._23QFA > div.KL4Bh')
	# for img in imgs:
	# 	print(img.img['src'])
	# for cont in cont_list:
	# 	print(cont.text)

	# sql로 첫 게시글 데이터 저장
	# store_post(code, content, likes, hashtag)

	# 다음 버튼
	next_lst = driver.find_elements_by_css_selector('div._2dDPU.CkGkG > div.EfHg9 a')

	page = 2

	while len(next_lst) > 0:

		# print(len(next_lst))

		# 다음 버튼 누르기
		for next in next_lst:
			# print('next_page')

			# 두번째 게시글부터
			print(f'================= POST {page} =================')
			next.click()

			driver.switch_to.window(driver.window_handles[-1])
			driver.implicitly_wait(5)

			# 두번째 게시글부터 코드
			print('==GET CODE')
			try:
				url = driver.current_url
				code = url[-12:-1]
				print(code)
			except:
				code = 'no_code'

			# 두번째 게시글부터 이름
			print('==GET NAME')
			try:
				name = driver.find_elements_by_css_selector('div.o-MQd a.sqdOP')
				for n in name:
					print(n.text)

			except:
				name = 'no_name'
				print(name)

			# 두번째 게시글부터 본문
			print('==GET CONTENET')
			try:
				cont = driver.find_elements_by_css_selector('ul div.C4VMK > span')
				print(cont[0].text)
				content = cont[0].text
				# cont_lst.append('cont_text')

			except:
				print('no_content')
				content = 'no_content'
				# cont_lst.append('no_content')

			# 두번째 게시글부터 해시태그
			print('==GET TAG')
			hash_lst = []
			try:
				hashs = driver.find_elements_by_css_selector('div.C4VMK > span > a')
				for hash in hashs:
					hash = re.sub('[^0-9a-zA-Zㄱ-ㅣ가-힣!?]', "", hash.text)
					hash_lst.append(hash)
				print(hash_lst)
				hashtag = hash_lst
				for tag in hash_lst:
					print(code + ' ' + tag)

			except:
				print('no_hash')
				hash_lst.append('no_hash')
				hashtag = hash_lst
			
			# 오늘 날짜
			print('==TODAY')
			dt_now = datetime.datetime.now()
			today = dt_now.date()
			print(today)

			# 두번째 게시글부터 날짜
			print('==GET DATE')
			time.sleep(3)
			html = driver.page_source
			soup = BeautifulSoup(html, 'html.parser')
			try:
				date = soup.select('time._1o9PC.Nzb55')
				for d in date:
					dt = d['datetime'][:10]
					print(dt)

			except:
				print('no_date')

			if today == dt:
				print('GO TO APP')


			# # 두번째 게시글부터 좋아요 잠깐 제거
			# print('==GET LIKE')
			# try:
			# 	like_lst = driver.find_elements_by_css_selector('section.EDfFK.ygqzn a > span')
			# 	for like in like_lst:
			# 		likes = like.text
			# 		print(likes)

			# except:
			# 	likes = 'no_like'
			# 	print(likes)

			# store_post(code, content, likes, hashtag)



			# try:
			# 	imgs_lst = driver.find_elements_by_css_selector('div.eLAPa._23QFA > div.KL4Bh')
			# 	for imgs in imgs_lst:
			# 		print(imgs.img['src'])
			# except:
			# 	print('no_img')

			page += 1

	else:
		print('페이지 오류입니다')







# ================= POST 93 =================
# ==GET CODE
# BkwiLnChOkI
# == GET CONTENT
# 초면에 플립플랩 주인공:어지러운::두_눈: ㅤ
# ㅤ
# :스튜디오_마이크:플랩 인터뷰ㅤ
# “모르는 사람들이랑 축구를 하자고 하면 거부감을 갖는 친구들이 많아요. 그런데 플랩은 매니저분들이 계시고, 사람들이 즐길 수 있게 환경을 만들어 주니까...무엇보다 실력에 상관 없이 와서 서로 응원하고 화이팅 넘치게 하니까 언제든지 참여하셔도 괜찮을 것 같습니다!” #송진완ㅤ
# ㅤ
# #플랩풋볼 #혼자와도 #축구 #풋살 #할수있다 @plabfootball #축덕 #축스타그램
# ==GET DATE
# 2018-07-03 14:53:52
# ==GET LIKE
# 30
# [‘송진완ㅤ‘, ‘플랩풋볼‘, ‘혼자와도‘, ‘축구‘, ‘풋살‘, ‘할수있다‘, ‘축덕‘, ‘축스타그램’]
# ==GET TAG
# BkwiLnChOkI 송진완ㅤ
# ==GET TAG
# BkwiLnChOkI 플랩풋볼
# ==GET TAG
# BkwiLnChOkI 혼자와도
# ==GET TAG
# BkwiLnChOkI 축구
# ==GET TAG
# BkwiLnChOkI 풋살
# ==GET TAG
# BkwiLnChOkI 할수있다
# ==GET TAG
# BkwiLnChOkI 축덕
# ==GET TAG
# BkwiLnChOkI 축스타그램

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