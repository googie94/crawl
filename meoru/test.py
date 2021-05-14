# from urllib.request import urlopen, Request
# from bs4 import BeautifulSoup as bs

# # 사용자 인증서 필요
# import  os, ssl
# if  ( not  os.environ.get ( 'PYTHONHTTPSVERIFY', '') and getattr (ssl, '_create_unverified_context', None)) : 
# 	ssl._create_default_https_context =  ssl._create_unverified_context

# # 한글 키워드 인코드(귀멸의 칼날)
# keyword = '%EA%B7%80%EB%A9%B8%EC%9D%98%20%EC%B9%BC%EB%82%A0'
# keyword.encode('utf-8')
# url = 'https://namu.wiki/w/'+keyword

# # 나무위키에서는 유저 정보가 없으면 막고 있는 것 같음. 유저 정보를 헤더에 담아 요청을 보냄
# req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})


# # 위에 내용은 신경쓰지 않아도 됩니다. 이번주 하기로 한 것에만 집중하면 됩니다.
# html = urlopen(req)
# bs = bs(html.read(), 'html.parser')
# print(bs)


print('hello world')