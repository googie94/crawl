from urllib.request import urlopen, Request
import requests
# 
from bs4 import BeautifulSoup
from selenium import webdriver
# 
import time
from datetime import datetime, timedelta, timezone
import re
#
from konlpy.tag import Okt
from collections import Counter
# 
# # 사용자 인증서 필요
import  os, ssl
if  ( not  os.environ.get ( 'PYTHONHTTPSVERIFY', '') and getattr (ssl, '_create_unverified_context', None)) : 
	ssl._create_default_https_context =  ssl._create_unverified_context
# 
import json


# save mysql
import pymysql

host = 'sego.c3jqlg47t2v5.ap-northeast-2.rds.amazonaws.com'
user = 'sego_admin'
pw = 'googie0126!'
db = 'sego'
conn = pymysql.connect(host=host, user=user, passwd=pw, db=db, charset='utf8')
cur = conn.cursor()
cur.execute('USE scraping')

def store_post(post_id, category, title, content, created_date, link):
	cur.execute(
		'INSERT INTO naver_post (post_id, category, title, content, created_date, link) VALUES (%s, %s, %s, %s, %s, %s)',
		(post_id, category, title, content, created_date, link)
	)
	cur.connection.commit()

def store_comment(post_id, content, created_date):
	cur.execute(
		'INSERT INTO naver_comment (post_id, content, created_date) VALUES (%s, %s, %s)',
		(post_id, content, created_date)
	)
	cur.connection.commit()

def store_tag(post_id, tag):
	cur.execute(
		'INSERT INTO naver_tag (post_id, tag) VALUES (%s, %s)',
		(post_id, tag)
	)
	cur.connection.commit()


# USER
payload={}
headers = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
  'Referer': 'https://apis.naver.com/'
}
# 
text_list = []
url_list = []
# 키워드 = 플랩풋볼
keyword = '%ED%94%8C%EB%9E%A9%ED%92%8B%EB%B3%BC'
keyword.encode('utf-8')


# req = requests.get(api_url, headers=headers, data=payload)
# a = req.text.find('(')
# txt = req.text[a+1:]
# b = txt.find(')')
# txt = txt[:b]
# req = json.loads(txt)

# 인스타그램 테스트
# api_url = 'https://www.instagram.com/explore/tags/'+keyword+'/?__a=1'
# req = requests.get(api_url, headers=headers, data=payload).json()
# print(req)


def hangul(text):
	hangul = re.compile('[^ ㄱ-ㅣ 가-힣]')
	result = hangul.sub('', text)
	# okt = Okt()
	# global text_list
	# text_list.append(result)
	print(result)

# ========================================
# ========== 네이버 블로그 ==================
# ========================================

def getTotal(index):
	index = str(index)
	url = 'https://s.search.naver.com/p/blog/search.naver?where=m_blog&start='+index+'&nlu_query={"r_category":"23"}&ssl=1&mobile_more=1&dkey=0&query='+keyword+'&nx_search_query='+keyword+'&spq=0&rev=44&_callback=jQuery224024759958364615287_1620305685738'
	html = urlopen(url)
	bs = BeautifulSoup(html, 'html.parser')
	total = bs.text[53:57]
	total = int(total.replace('"', '').replace(',', ''))
	return total

def getBlogUrl(index):
	index = str(index)
	url = 'https://s.search.naver.com/p/blog/search.naver?where=m_blog&start='+index+'&nlu_query={"r_category":"23"}&ssl=1&mobile_more=1&dkey=0&query='+keyword+'&nx_search_query='+keyword+'&spq=0&rev=44&_callback=jQuery224024759958364615287_1620305685738'
	print('=====GET URL=======')
	# print(url)
	html = urlopen(url)
	bs = BeautifulSoup(html, 'html.parser')
	hrefs = bs.findAll('a', href = re.compile('(https://m.blog.naver.com/)[^A-Z]*/'))
	global url_list
	url_list = []
	for href in hrefs:
		if href.attrs['href'].replace('\\"','').replace(' ','') not in url_list:
			url_list.append(href.attrs['href'].replace('\\"','').replace(' ',''))
	return url_list

def getBlogPost(url):
	print('POST START')
	category = 'blog'
	# print('===============주소===============')
	print(url)
	post_id = url.split('/')[4]
	# 
	html = urlopen(url)
	bs = BeautifulSoup(html, 'html.parser')
	# print(bs)
	# 최근 블로그
	try:
		# DATE
		date = bs.find('p', {'class': 'blog_date'}).text
		if '시간' in date:
			time = date.replace('시간 전', '')
			time = int(time)
			time = -time
			now = datetime.now()
			date = now + timedelta(hours=time)
			date = str(date)
			date = date[:16]
		elif '분' in date:
			time = date.replace('시간 전', '')
			time = int(time)
			time = -time
			now = datetime.now()
			date = now + timedelta(minutes=time)
			date = str(date)
			date = date[:16]
		else:
			dates = date.split('.')
			date_arr = []
			for date in dates:
				date_arr.append(date.replace(' ','').replace('\n\t', ''))
			date = str(date_arr[0]+'-'+date_arr[1]+'-'+date_arr[2]+' '+date_arr[3])
			# print('before', date)
		date = datetime.strptime(date,'%Y-%m-%d %H:%M')
		# CONTENT
		try:
			title = bs.find('div', {'class': 'se-module se-module-text se-title-text'}).text
			contents = bs.findAll('div', {'class': 'se-module se-module-text'})
			# print('===============제목===============')
			# print(date)
			# print(title)
			# print('===============내용===============')
			arr = []
			for content in contents:
				arr.append(content.get_text())
			content = ''.join(arr)
			store_post(post_id, category, title, content, date, url)

		except:
			title = bs.find('h3').text
			content = bs.find('p', {'class': 'se_textarea'}).text
			# print('===============제목===============')
			# print(date)
			# print(title)
			# print('===============내용===============')
			# print(content)
			store_post(post_id, category, title, content, date, url)

	# 아니라면
	except:
		date = bs.find('p', {'class': 'se_date'}).text
		dates = date.split('.')
		date_arr = []
		for date in dates:
			date_arr.append(date.replace(' ','').replace('\n\t', ''))
		date = str(date_arr[0]+'-'+date_arr[1]+'-'+date_arr[2]+' '+date_arr[3])
		# print('before', date)
		date = datetime.strptime(date,'%Y-%m-%d %H:%M')
		title = bs.find('h3').text
		content = bs.find('div', {'id': 'viewTypeSelector'}).text
		# print('===============제목===============')
		# print(date)
		# print(title)
		# print('===============내용===============')
		# print(content)
		store_post(post_id, category, title, content, date, url)

	# 
	# print('===============태그===============')
	try:
		tags = bs.findAll('span', {'class': 'ell'})
		for tag in tags:
			if "#" in tag.text[0]:
				tag = tag.text
				tag = tag.replace('#','')
				print(post_id, tag)
				store_tag(post_id, tag)
	except:
		print('NONE TAG')
	# SENT COMMENT
	user_name = url.split('/')[3]
	getBlogComment(user_name, post_id)

def getBlogComment(user_name, post_id):
	print('COMMENT START')
	print('SECCESS', user_name, post_id)
	url = 'https://blog.naver.com/PostList.nhn?blogId='+user_name
	html = urlopen(url)
	bs = BeautifulSoup(html.read(), 'html.parser')
	scripts = bs.findAll("script")
	for script in scripts:
		if "blogNo" in script.text:
			text = script.text
			var = text.split("var")
			for v in var:
				if "blogNo" in v:
					blog_no = v.split("'")[1]
	api_url = 'https://apis.naver.com/commentBox/cbox/web_naver_list_jsonp.json?ticket=blog&templateId=default&pool=cbox9&lang=ko&objectId='
	content_no = post_id
	object_id = blog_no + '_201_' + content_no
	api_url = api_url + object_id + '&groupId=' + blog_no
	res = requests.get(api_url, headers=headers)
	res = res.text
	res = res[10:]
	a = res.find(');')
	res = res[:a]
	res = json.loads(res)
	print('===============댓글===============')
	try:
		comment_count = res['result']['count']['total']
		# print('댓글 수 : ', comment_count)
	except:
		print('DONT COMMENT')
	# 
	try:
		comments = res['result']['commentList']
		for comment in comments:
			if comment['contents'] == "": 
				print('숨김')
			else:
				content = comment['contents'].replace('<br>','')
				dates = comment['modTime'].replace('T', ' ')
				date = dates[:16]
				print(date)
				created_date = datetime.strptime(date,'%Y-%m-%d %H:%M')
				print(created_date)
				# print(post_id, content, created_date)
				store_comment(post_id, content, created_date)
	except:
		pass
	print('POST END')

# ========================================
# ========== 네이버 카페 ===================
# ========================================
# comment_list = []
# # 
# def getTotal(index):
# 	url = 'https://s.search.naver.com/p/cafe/search.naver?abuse=0&ac=0&aq=0&date_from=&date_option=0&date_to=&m=1&nlu_query={"r_category":"23"}&nqx_context=&nx_and_query=&nx_search_hlquery=&nx_search_query=&nx_sub_query=&prdtype=0&prmore=1&qdt=1&query='+keyword+'&qvt=1&rev=44&spq=0&st=rel&stnm=rel&where=m_article&start={}&display=15&is_person=0&_callback=jQuery22407496630039182579_1620346928758'.format(index)
# 	html = urlopen(url)
# 	bs = BeautifulSoup(html, 'html.parser')
# 	total = bs.text[53:57]
# 	total = int(total.replace('"', '').replace(',', ''))
# 	return total

# def getBlogUrl(index):
# 	url = 'https://s.search.naver.com/p/cafe/search.naver?abuse=0&ac=0&aq=0&date_from=&date_option=0&date_to=&m=1&nlu_query={"r_category":"23"}&nqx_context=&nx_and_query=&nx_search_hlquery=&nx_search_query=&nx_sub_query=&prdtype=0&prmore=1&qdt=1&query='+keyword+'&qvt=1&rev=44&spq=0&st=rel&stnm=rel&where=m_article&start={}&display=15&is_person=0&_callback=jQuery22407496630039182579_1620346928758'.format(index)
# 	print('=======================')
# 	print(index)
# 	print(url)
# 	html = urlopen(url)
# 	bs = BeautifulSoup(html, 'html.parser')
# 	hrefs = bs.findAll('a', href = re.compile('(https://m.cafe.naver.com/)[^A-Z]*/'))
# 	global url_list
# 	url_list = []
# 	for href in hrefs:
# 		if href.attrs['href'].replace('\\"','').replace(' ','') not in url_list:
# 			url_list.append(href.attrs['href'].replace('\\"','').replace(' ',''))
# 	return url_list

# def getBlogPost(url):
# 	category = 'cafe'
# 	# print('===============주소===============')
# 	# print(url)
# 	link = url
# 	url = url[25:]
# 	find_cafe_index = url.find('/')
# 	find_art_index = url.find('?')
# 	find_code_index = url.find('=')
# 	cafe_nm = url[:find_cafe_index]
# 	cafe_id = url[find_cafe_index+1:find_art_index]
# 	cafe_code = url[find_code_index+1:]
# 	cafe_code = cafe_code.replace('=', '%3D')
# 	api_url = 'https://apis.naver.com/cafe-web/cafe-articleapi/v2/cafes/{}/articles/{}?useCafeId=false&art={}&query={}'.format(cafe_nm, cafe_id, cafe_code, keyword)
# 	# 				https://m.cafe.naver.com/ca-fe/web/cafes/re4mo/articles/1373558?useCafeId=false&art=ZXh0ZXJuYWwtc2VydmljZS1uYXZlci1zZWFyY2gtY2FmZS1wcg%3D%3D.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjYWZlVHlwZSI6IkNBRkVfVVJMIiwiY2FmZVVybCI6InJlNG1vIiwiYXJ0aWNsZUlkIjoxMzczNTU4LCJpc3N1ZWRBdCI6MTYyMDM0NzE1Njk1MX0%3D.o7ZbpmIn_4r8qJa8JQeWfcK62kLPmEtfrAaQ8NQrapc%3D&query=%ED%94%8C%EB%9E%A9%ED%92%8B%EB%B3%BC%ED%9B%84%EA%B8%B0
# 	# https://apis.naver.com/cafe-web/cafe-articleapi/v2/cafes/re4mo/articles/1373558?useCafeId=false&art=ZXh0ZXJuYWwtc2VydmljZS1uYXZlci1zZWFyY2gtY2FmZS1wcg%3D%3D.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjYWZlVHlwZSI6IkNBRkVfVVJMIiwiY2FmZVVybCI6InJlNG1vIiwiYXJ0aWNsZUlkIjoxMzczNTU4LCJpc3N1ZWRBdCI6MTYyMDM0NzE1Njk1MX0%3D.o7ZbpmIn_4r8qJa8JQeWfcK62kLPmEtfrAaQ8NQrapc%3D&query=%ED%94%8C%EB%9E%A9%ED%92%8B%EB%B3%BC%ED%9B%84%EA%B8%B0
# 	# https://apis.naver.com/cafe-web/cafe-articleapi/v2/cafes/re4mo/articles/1373558?useCafeId%3Dfalse&art%3DZXh0ZXJuYWwtc2VydmljZS1uYXZlci1zZWFyY2gtY2FmZS1wcg%3D%3D.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjYWZlVHlwZSI6IkNBRkVfVVJMIiwiY2FmZVVybCI6InJlNG1vIiwiYXJ0aWNsZUlkIjoxMzczNTU4LCJpc3N1ZWRBdCI6MTYyMDM1MDc4NjI4M30%3D.p5RYyeselnfi9_xsjTxxt-oI_AE3sPBQ1FzArgi-dzc%3D&query%3D%ED%94%8C%EB%9E%A9%ED%92%8B%EB%B3%BC%ED%9B%84%EA%B8%B0
# 	# print('===============api===============')
# 	# print(api_url)
# 	req = requests.get(api_url, headers=headers, data=payload).json()
# 	print('===============POST===============')
# 	post_id = str(req['result']['article']['id'])
# 	print(post_id)
# 	# print('===============날짜===============')
# 	date = str(req['result']['article']['writeDate'])
# 	date = date[:10]
# 	date = datetime.fromtimestamp(int(date)).strftime('%Y-%m-%d %H:%M:%S')
# 	# print(date)
# 	# print('===============제목===============')
# 	title = req['result']['article']['subject']
# 	# print(title)
# 	content_html = req['result']['article']['contentHtml']
# 	content = BeautifulSoup(content_html, 'html.parser')
# 	# print('===============내용===============')
# 	content = content.get_text()
# 	content = content.strip()
# 	content = content.replace('\n','')
# 	# print(content)
# 	# 
# 	store_post(post_id, category, title, content, date, link)
# 	# 
# 	# print('===============댓글===============')
# 	comment_list = req['result']['comments']['items']
# 	for comment in comment_list:
# 		comment_content = comment['content']
# 		# print(comment_content)
# 		comment_date = str(comment['updateDate'])
# 		comment_date = comment_date[:10]
# 		comment_date = datetime.fromtimestamp(int(comment_date)).strftime('%Y-%m-%d %H:%M:%S')
# 		# print(comment_date)
# 		store_comment(post_id, comment_content, comment_date)


# RUN CODE
total = getTotal(1)
print('======TOTAL===')
print(total)
index = 1
while index < total:
	getBlogUrl(index)
	for url in url_list:
		getBlogPost(url)
	index += 15



# =========================
# =========================
# text_list = "".join(text_list)
# okt = Okt()
# nouns = okt.nouns(text_list)
# counter = Counter(nouns)
# print(counter.most_common(50))

# import platform 
# print(platform.architecture())



















