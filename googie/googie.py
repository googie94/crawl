from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
# 
import  os, ssl 

if  ( not  os.environ.get ( 'PYTHONHTTPSVERIFY', '') and getattr (ssl, '_create_unverified_context', None)) : 
	ssl._create_default_https_context =  ssl._create_unverified_context

keyword = '%EA%B7%80%EB%A9%B8%EC%9D%98%20%EC%B9%BC%EB%82%A0'
keyword.encode('utf-8')
url = 'https://namu.wiki/w/'+keyword
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

html = urlopen(req)
bs = bs(html.read(), 'html.parser')
print(bs)