from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
# 
print('한글')
html = urlopen('https://www.bbc.com/sport/football/56957720')
# b = html.read()
# print(b)
# print(b.h1)
bs = bs(html.read(), 'html.parser')
print(bs.h4.text)


#urllib = url라이브러리 
# bs = BeautifulSoup
#html을 받고 그것에 접근할 수있게 하는 함수