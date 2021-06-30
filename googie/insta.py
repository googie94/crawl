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
cur.execute('USE sego')

def store_post(category, post_id, author, content, created_date, url):
	cur.execute(
		'INSERT INTO post_instagram (category, post_id, author, content, created_date, url) VALUES (%s, %s, %s, %s, %s, %s)',
		(category, post_id, author, content, created_date, url)
	)
	cur.connection.commit()

def store_tag(post_id, tag):
	cur.execute(
		'INSERT INTO post_instagram_tag (post_id, tag) VALUES (%s, %s)',
		(post_id, tag)
	)
	cur.connection.commit()
# def store_comment(post_id, content, created_date):
# 	cur.execute(
# 		'INSERT INTO naver_comment (post_id, content, created_date) VALUES (%s, %s, %s)',
# 		(post_id, content, created_date)
# 	)
# 	cur.connection.commit()

# def store_tag(post_id, tag):
# 	cur.execute(
# 		'INSERT INTO naver_tag (post_id, tag) VALUES (%s, %s)',
# 		(post_id, tag)
# 	)
# 	cur.connection.commit()

today = datetime.today().strftime('%Y%m%d')
yesterday = datetime.today() - timedelta(days=1)
yesterday = yesterday.strftime('%Y-%m-%d')

# USER
payload={}
headers = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}
# PARAMETERS
keyword = '%ED%94%8C%EB%9E%A9%ED%92%8B%EB%B3%BC'
keyword.encode('utf-8')
is_next = True
end_cursor = ''

def getPostList():
	global is_next
	global end_cursor
	api_url = 'https://www.instagram.com/graphql/query/?query_hash=298b92c8d7cad703f7565aa892ede943&variables={"tag_name":"'+keyword+'","first":50,"after":"'+end_cursor+'"}'
	print(api_url)
	res = requests.get(api_url, headers=headers, data=payload).json()
	res = res['data']['hashtag']
	# 
	is_next = res['edge_hashtag_to_media']['page_info']['has_next_page']
	end_cursor = res['edge_hashtag_to_media']['page_info']['end_cursor']
	# 
	posts = res['edge_hashtag_to_media']['edges']
	print('POSTS LENGTH', len(posts))
	time.sleep(10)
	try:
		category = 'instagram'
		for index, post in enumerate(posts):
			print('================= POST '+ str(index+1) +' =================')
			print('==GET CODE')
			post_id = post['node']['shortcode']
			print(post_id)
			print('== GET CONTENT')
			content = post['node']['edge_media_to_caption']['edges'][0]['node']['text']
			print(content)
			print('==GET DATE')
			date = datetime.fromtimestamp(post['node']['taken_at_timestamp'])
			created_date = date.strftime('%Y-%m-%d %H:%M:%S')
			print(created_date)
			print('==GET LIKE')
			author = post['node']['owner']['id']
			print(author)
			# print('==GET LIKE')
			# like_count = post['node']['edge_liked_by']['count']
			# print(like_count)
			tags = re.findall(r"#(\w+)", content)
			print(tags)
			url = 'https://www.instagram.com/p/'+post_id+'/'
			#
			# print('YESTERDAY', yesterday)
			# if created_date > yesterday:
			# 	print('CONFIRM')
			# else:
			# 	print('NONONO')
			# 	is_next=False
			# print(category, post_id, author, content, created_date, url)
			store_post(category, post_id, author, content, created_date, url)
			for tag in tags:
				print('==GET TAG')
				print(post_id, tag)
				store_tag(post_id, tag)
			# print('GET THUMBNAIL','https://www.instagram.com/p/'+post['node']['shortcode']+'/media/?size=l')
			# print('IS VIDEO',post['node']['is_video'])
	except:
		pass
	time.sleep(25)


for i in range(100):
	print('======================= INDEX', i+1, '=======================')
	if is_next == True:
		getPostList()
	else:
		break;

# def getInstaPost():
	
# 간략 포스트
# https://api.instagram.com/oembed/?url=http://instagram.com/p/B25TmunFTUK/
# 포스트
# https://www.instagram.com/graphql/query/?query_hash=298b92c8d7cad703f7565aa892ede943&variables={%22tag_name%22:%22%ED%94%8C%EB%9E%A9%ED%92%8B%EB%B3%BC%22,%22first%22:6,%22after%22:%22QVFCbzVFdmY1eWdxOGx6czFDMzBfQnFWVmJXZUdUZHFlZ2NRMWRrR29vb0o2anpBdlVaNlZaM1dqZENvcEFhVG9VTElDdnVkSzhsYW9Xb0FBTG1rREMtWQ==%22}
# 댓글 (상위 20개)
# https://www.instagram.com/graphql/query/?query_hash=33ba35852cb50da46f5b5e889df7d159&variables={%22shortcode%22:%22CPVA3cXLOPY%22,%22first%22:20}
# 동영상 및 이미지
# https://www.instagram.com/p/CBf0Ez_FeXR/?__a=1
# https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-15/e35/s640x640/174191033_293248945850264_4706822520582962514_n.jpg?tp=1&_nc_ht=scontent-arn2-2.cdninstagram.com&_nc_cat=1&_nc_ohc=lUMp5EnMMW8AX__E42K&edm=ABfd0MgBAAAA&ccb=7-4&oh=c755580e7a5f0c8e3d4170122390efbc&oe=60AE0543&_nc_sid=7bff83
# https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-15/e35/s1080x1080/190518389_1911147585709942_1958578390236297346_n.jpg?tp=1&_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_cat=110&_nc_ohc=rR0MpFZziG0AX8XC8eX&edm=AA0rjkIBAAAA&ccb=7-4&oh=55f9a18d6f2382fd3b019df11e867ee5&oe=60BC575E&_nc_sid=d997c6
# https://scontent-mxp1-1.cdninstagram.com/vp/cce7a73f8904eea57575a69244b4997b/5DFF22C4/t51.2885-15/sh0.08/e35/s640x640/67472591_2116886595084247_1444361079130496531_n.jpg?_nc_ht=scontent-mxp1-1.cdninstagram.com&_nc_cat=107
