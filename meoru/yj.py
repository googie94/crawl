# 게시글 날짜 b
# 계정 이름 b
# likes 오류 해결... (빼자)
# 태그 테이블은 따로 만들기
# 하루날짜(범위 내) 게시글 뽑기
# 이미지 

import pymysql

# Selenium 임포트
from selenium import webdriver

# etc 임포트
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import requests
import time
<<<<<<< HEAD
import re
import sys
import io
import codecs
import datetime

# 인코딩
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
def store_post(code, name, content, hash_lst, dt):
	cur.execute(
		'INSERT INTO meoru_gram (code, name, content, hash_lst, dt) VALUES (%s, %s, %s, %s, %s)',
		(code, name, content, hash_lst, dt)
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
=======
# import sys
# import io
# import codecs
# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
# sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

print('text')
>>>>>>> ce52660ebf6982dc3228333af3147a0295adf1a7
# 크롬 드라이버 생성
driver = webdriver.Chrome()
driver.implicitly_wait(3)

# 들어가는거
# keyword = input('무엇을 검색할까요? ')
keyword = '플랩풋볼'
driver.get('https://www.instagram.com/')
time.sleep(3)

# 로그인
# id = input('id? ')
# ps = input('password? ')
id = ''
ps = ''

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
	driver.switch_to.window(driver.window_handles[-1])
	driver.implicitly_wait(3)
	url = driver.current_url
	f_code = url[-12:-1]
	# print(f_code)
	code = f_code

	# 첫 게시글 이름
	print('==GET NAME')
	names = driver.find_elements_by_css_selector('div.o-MQd a.sqdOP')
	# print(name)
	for n in names:
		name = n.text
		# print(name)

	# 게시글 내 본문
	print('==GET CONTENET')
	cont = driver.find_elements_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > div.EtaWk > ul div.C4VMK > span')
	# print(cont[0].text)
	content = cont[0].text

	# 해시태그
	print('==GET TAG')
	hashs = driver.find_elements_by_css_selector('div.C4VMK > span > a')
	hash_lst = []
	# print(hashs.text)
	try:
		for hash in hashs:
			# 정규화
			hash = re.sub('[^0-9a-zA-Zㄱ-ㅣ가-힣!?]', "", hash.text)
			hash_lst.append(hash)
		# print(hash_lst)

		for tag in hash_lst:
			print('==GET TAG')
			hashtag = tag
			# print(code + ' ' + hashtag)

	except:
		hash_lst.append('no_hash')
		# print(hash_lst)

	# 첫 게시글 날짜
	html = driver.page_source
	soup = BeautifulSoup(html, 'html.parser')
	print('==GET DATE')
	try:
		date = soup.select('time._1o9PC.Nzb55')
		for d in date:
			dt = d['datetime'][:10]
			# print(dt)
	except:
		dt = 'no_date'
		# print(dt)


	# 첫 게시글 sql로 저장
	print(code, name, content, hash_lst, dt)


	# 다음 버튼
	next_lst = driver.find_elements_by_css_selector('div._2dDPU.CkGkG > div.EfHg9 a')

	page = 2

	while len(next_lst) > 0:

		# 다음 버튼 누르기
		for next in next_lst:

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
				name_lst = driver.find_elements_by_css_selector('div.o-MQd a.sqdOP')
				for n in name_lst:
					name = n.text
					print(name)

			except:
				name = 'no_name'
				print(name)

			# 두번째 게시글부터 본문
			print('==GET CONTENET')
			try:
				cont = driver.find_elements_by_css_selector('ul div.C4VMK > span')
				print(cont[0].text)
				content = cont[0].text
			except:
				print('no_content')
				content = 'no_content'

			# 두번째 게시글부터 해시태그
			hash_lst = []
			try:
				hashs = driver.find_elements_by_css_selector('div.C4VMK > span > a')
				for hash in hashs:
					hash = re.sub('[^0-9a-zA-Zㄱ-ㅣ가-힣!?]', "", hash.text)
					hash_lst.append(hash)
				print(hash_lst)
				for tag in hash_lst:
					print('==GET TAG')
					hashtag = tag
					print(code + ' ' + hashtag)

			except:
				print('no_hash')
				hash_lst.append('no_hash')
			
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
				dt = 'no_date'
				print(dt)

			# if today == dt:
			# 	print('GO TO APP')


			page += 1

	else:
		print('페이지 오류입니다')

	store_post(code, name, content, hash_lst, dt)








<<<<<<< HEAD
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
=======
# for cont in cont_lst:
# 	print(cont.text)
>>>>>>> ce52660ebf6982dc3228333af3147a0295adf1a7
