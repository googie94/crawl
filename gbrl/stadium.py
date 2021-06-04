import time
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook

wb = Workbook(write_only=True)
ws = wb.create_sheet('풋살장리스트')
ws.append(['풋살장이름', '주소'])

driver = webdriver.Chrome("C:/Users/SAMSUNG/Downloads/chromedriver_win32/chromedriver.exe")
driver.implicitly_wait(3)

# 들어가는거
driver.get('https://iamground.kr/futsal/search')
time.sleep(5)

road = driver.find_element_by_xpath

road('//*[@id="iSearch"]').click()
time.sleep(1)

road('//*[@id="iSearch"]').send_keys('서울')
time.sleep(2)

road('//*[@id="navbarRight"]/div[3]/i').click()
time.sleep(2)

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # scrollHeight까지 스크롤
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break 
    last_height = new_height


for index in range(1,50):
    time.sleep(2)
    print(index)
    print(type(index))
    index = str(index)
    print(type(index))
    # 클릭한다

    stadium_address = road("//*[@id='cardHolder']/div["+index+"]/div[2]/div[1]/div[2]")
    stadium_name = road("//*[@id='cardHolder']/div["+index+"]/div[1]/div[2]/h4")

    time.sleep(2)

    print(stadium_address.text)
    print(stadium_name.text)

driver.quit()

wb.save('풋살장리스트.xlsx')

# import requests; from urllib.parse import urlparse
# import pandas as pd 

# address ="강원 원주시 단구로 171"
# url = "http://dapi.kakao.com/v2/local/search/address.json?&query=" + address

# result = requests.get(urlparse(url).geturl()), 
# headers={"Authorization":"KakaoAK 320bdd95b5628c5557d1a30a0a84f769"}

# print(result)

# # json_obj = result.json()
# # print(json_obj)

# # list = []
# # for document in json_obj['documents']:
# #     val = [document['road_address']['building_name'], document['address_name'], document['y'], document['x']]
# #     list.append(val)

# # df = pd.DataFrame(list, colums = ['building_name' , 'address_name', 'lat', 'lon'] )
# # df 
