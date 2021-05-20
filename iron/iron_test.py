import re
p = re.compile('#([0-9a-zA-Z가-힣]*)')

texts = '#플랩풋볼 #플랩 #해시태그 안녕'
hashtags = p.findall(texts)
print(hashtags)
