from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
# 
html = urlopen('https://www.youtube.com/results?search_query=%ED%94%8C%EB%9E%A9%ED%92%8B%EB%B3%BC&sp=CAISBAgFEAE%253D')
#bs = html.read()
bs = bs(html, 'html.parser')
print(bs.prettify())