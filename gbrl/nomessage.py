from selenium import webdriver
import time

driver = webdriver.Chrome("C:/Users/SAMSUNG/Downloads/chromedriver_win32/chromedriver.exe")

driver.get("https://www.plabfootball.com/admin/")
driver.implicitly_wait(3)

driver.find_element_by_xpath('//*[@id="id_username"]').send_keys('jinhocheol@naver.com')
driver.find_element_by_xpath('//*[@id="id_password"]').send_keys('ab5701100!')

time.sleep(1)

driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()

driver.find_element_by_xpath('//*[@id="content-main"]/div[12]/table/tbody/tr[5]/th/a').click()

driver.find_element_by_xpath('//*[@id="searchbar"]')

driver.find_element_by_xpath('//*[@id="searchbar"]').click()
driver.find_element_by_xpath('//*[@id="searchbar"]').send_keys('010-9064-4482')
#or 이거 안되면 이거 쳐봐라 # 안되면 이거 해라 
driver.find_element_by_xpath('//*[@id="changelist-search"]/div/input[2]').click()

driver.find_element_by_xpath('//*[@id="result_list"]/tbody/tr/th/a').click()

driver.find_element_by_xpath('//*[@id="id_memo"]').send_keys('수신 거부')

driver.find_element_by_xpath('//*[@id="id_is_subscribe"]').click()

#driver.find_element_by_xpath('//*[@id="profilesetting_form"]/div/div/input[1]').click()

#시트 높낮이 체크 - 스크롤 - 하나씩 적용 
#다시 돌아가서, 번호 2가지 방식으로 치고. 수신 거부 쓰고 - 저장 버튼 
#없으면 어떻게 할 건지? 없다면 없다고 써야한다. if not 구문으로 
#if 로 추가해야함, - 형태 or 00000000 형태 
#완료하면 체크해라 