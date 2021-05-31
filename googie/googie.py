from urllib.request import urlopen, Request
import requests
# 
from bs4 import BeautifulSoup
from selenium import webdriver
# 
import datetime, time
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

def store_post():
	cur.execute(
		'INSERT INTO naver_post (post_id, category, title, content, created_date, like_count) VALUES (%s, %s, %s, %s, %s, %s)',
		(post_id, category, title, content, created_date, like_count)
	)
	cur.connection.commit()

def store_comment(post_id, content):
	cur.execute(
		'INSERT INTO naver_comment (post_id, content) VALUES (%s, %s)',
		(post_id, content)
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


# 블로그 댓글 모델
# api_url = 'https://apis.naver.com/commentBox/cbox/web_naver_list_jsonp.json?ticket=blog&templateId=default_simple&pool=cbox9&_callback=jQuery1124023443552214558605_1621480751221&lang=ko&country=&objectId=59307270_201_222344386382&categoryId=&pageSize=50&indexSize=10&groupId=59307270&listType=OBJECT&pageType=default&page=1&initialize=true&userType=&useAltSort=true&replyPageSize=10&showReply=true&_=1621480751223'
# https://apis.naver.com/commentBox/cbox/web_naver_list_jsonp.json
# ?ticket=blog
# &templateId=default_simple
# &pool=cbox9
# &lang=ko
# &objectId=59307270_201_222344386382
# &groupId=59307270

# https://apis.naver.com/commentBox/cbox/web_naver_list_jsonp.json
# ?ticket=blog
# &templateId=default
# &pool=cbox9
# &lang=ko
# &objectId=68395359_201_222301794649
# &groupId=68395359
# OK = blogNo + _ + 201 + _ + contentNo

# 블로그 넘버 가져오기
# blog_id 필요
# https://m.blog.naver.com/rego/BlogInfo.nhn?blogId=nam4510



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

# ========== 네이버 블로그 ==========

def getTotal(index):
	url = 'https://s.search.naver.com/p/blog/search.naver?where=m_blog&start={}&nlu_query=%7B%22r_category%22%3A%2223%22%7D&ssl=1&mobile_more=1&dkey=0&query='+keyword+'&nx_search_query='+keyword+'&spq=0&rev=44&_callback=jQuery224024759958364615287_1620305685738'.format(index)
	html = urlopen(url)
	bs = BeautifulSoup(html, 'html.parser')
	total = bs.text[53:57]
	total = int(total.replace('"', '').replace(',', ''))
	return total

def getBlogUrl(index):
	url = 'https://s.search.naver.com/p/blog/search.naver?where=m_blog&start={}&nlu_query=%7B%22r_category%22%3A%2223%22%7D&ssl=1&mobile_more=1&dkey=0&query='+keyword+'&nx_search_query='+keyword+'&spq=0&rev=44&_callback=jQuery224024759958364615287_1620305685738'.format(index)
	html = urlopen(url)
	bs = BeautifulSoup(html, 'html.parser')
	hrefs = bs.findAll('a', href = re.compile('(https://m.blog.naver.com/)[^A-Z]*/'))
	global url_list
	for href in hrefs:
		if href.attrs['href'].replace('\\"','').replace(' ','') not in url_list:
			url_list.append(href.attrs['href'].replace('\\"','').replace(' ',''))
	return url_list

def getBlogPost(url):
	print('===============주소===============')
	print(url)
	html = urlopen(url)
	bs = BeautifulSoup(html, 'html.parser')
	# print(bs)
	title = bs.find('div', {'class': 'se-module se-module-text se-title-text'}).text
	print('===============제목===============')
	print(title)
	print('===============내용===============')
	for content in bs.findAll('div', {'class': 'se-module se-module-text'}):
		print(content.get_text())


# 
total = getTotal(1)
index = 1
while index < total:
	getBlogUrl(index)
	for url in url_list:
		getBlogPost(url)
	index += 15

# ========================================
# ========== 네이버 카페 ==========
# comment_list = []
# # 
# def getTotal(index):
# 	url = 'https://s.search.naver.com/p/cafe/search.naver?abuse=0&ac=0&aq=0&date_from=&date_option=0&date_to=&m=1&nlu_query=%7B%22r_category%22%3A%2223%22%7D&nqx_context=&nx_and_query=&nx_search_hlquery=&nx_search_query=&nx_sub_query=&prdtype=0&prmore=1&qdt=1&query='+keyword+'&qvt=1&rev=44&spq=0&st=rel&stnm=rel&where=m_article&start={}&display=15&is_person=0&_callback=jQuery22407496630039182579_1620346928758'.format(index)
# 	html = urlopen(url)
# 	bs = BeautifulSoup(html, 'html.parser')
# 	total = bs.text[53:57]
# 	total = int(total.replace('"', '').replace(',', ''))
# 	return total

# def getBlogUrl(index):
# 	url = 'https://s.search.naver.com/p/cafe/search.naver?abuse=0&ac=0&aq=0&date_from=&date_option=0&date_to=&m=1&nlu_query=%7B%22r_category%22%3A%2223%22%7D&nqx_context=&nx_and_query=&nx_search_hlquery=&nx_search_query=&nx_sub_query=&prdtype=0&prmore=1&qdt=1&query='+keyword+'&qvt=1&rev=44&spq=0&st=rel&stnm=rel&where=m_article&start={}&display=15&is_person=0&_callback=jQuery22407496630039182579_1620346928758'.format(index)
# 	html = urlopen(url)
# 	bs = BeautifulSoup(html, 'html.parser')
# 	hrefs = bs.findAll('a', href = re.compile('(https://m.cafe.naver.com/)[^A-Z]*/'))
# 	global url_list
# 	for href in hrefs:
# 		if href.attrs['href'].replace('\\"','').replace(' ','') not in url_list:
# 			url_list.append(href.attrs['href'].replace('\\"','').replace(' ',''))
# 	return url_list

# def getBlogPost(url):
# 	# print('===============주소===============')
# 	# print(url)
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
# 	print('===============api===============')
# 	print(api_url)
# 	req = requests.get(api_url, headers=headers, data=payload).json()
# 	print('===============날짜===============')
# 	date = req['result']['article']['writeDate']
# 	date = datetime.datetime.fromtimestamp(date)
# 	print(date)
# 	# date = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(date))
# 	# print(date)
# 	print('===============제목===============')
# 	title = req['result']['article']['subject']
# 	apply_regular_expression(title)
# 	content_html = req['result']['article']['contentHtml']
# 	bs = BeautifulSoup(content_html, 'html.parser')
# 	print('===============내용===============')
# 	apply_regular_expression(bs.get_text())
# 	# for content in bs.findAll('div', {'class': 'se-module se-module-text'}):
# 		# apply_regular_expression(content.get_text())
# 	# print('===============댓글===============')
# 	# comment_list = req['result']['comments']['items']
# 	# for comment in comment_list:
# 	# 	apply_regular_expression(comment['content'])


# def apply_regular_expression(text):
# 	hangul = re.compile('[^ ㄱ-ㅣ 가-힣]')
# 	result = hangul.sub('', text)
# 	# okt = Okt()
# 	global text_list
# 	text_list.append(result)
# 	print(result)



# # RUN CODE
# total = getTotal(1)
# index = 1
# while index < total:
# 	print(index)
# 	if index > 50:
# 		break;
# 	# if index == 1:
# 	getBlogUrl(index)
# 	for url in url_list:
# 		getBlogPost(url)
# 		# break;
# 	index += 15

# text_list = "".join(text_list)
# okt = Okt()
# nouns = okt.nouns(text_list)
# counter = Counter(nouns)
# print(counter.most_common(50))

# import platform 
# print(platform.architecture())



















