from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
# 

html = urlopen('http://www.pythonscraping.com/pages/page1.html')
# b = html.read()
# print(b)
# print(b.h1)
bs = bs(html.read(), 'html.parser')
print(bs)
print(bs.h1)