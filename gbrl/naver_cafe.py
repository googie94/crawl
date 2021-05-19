from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip

def clipboard_input(user_xpath, user_input):
        temp_user_input = pyperclip.paste()  # 사용자 클립보드를 따로 저장

        pyperclip.copy(user_input)
        driver.find_element_by_xpath(user_xpath).click()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

        pyperclip.copy(temp_user_input)  # 사용자 클립보드에 저장 된 내용을 다시 가져 옴
        time.sleep(1)

driver = webdriver.Chrome("C:/Users/SAMSUNG/Downloads/chromedriver_win32/chromedriver.exe")
driver.implicitly_wait(3)

# 접속할 url
url = "https://cafe.naver.com/re4mo/1513599"

# 접속 시도
driver.get(url)

login = {
    "id" : "tigerz0114",
    "pw" : "wlsghcjf!1"
}

clipboard_input('//*[@id="id"]', login.get("id"))
clipboard_input('//*[@id="pw"]', login.get("pw"))
driver.find_element_by_xpath('//*[@id="log.login"]').click()

# 코드잇 네이버 블로그 접속
time.sleep(1)

driver.find_element_by_css_selector('input.#query').click()

driver.find_element_by_css_selector().send_keys('플랩풋볼')

driver.find_element_by_css_selector('ico_search_submit').click()


# 'mainFrame'으로 이동
driver.switch_to.frame('cafe_main')

# 블로그 글 내용 출력
print(driver.find_element_by_css_selector('div.se-main-container').text)

driver.quit()

#현 상황 요약 , 네이버 블로그 iframe 제목, 기사 돌파 성공 -> 카페 시도 => 
#캡챠 갑툭튀 => 디버깅 크롬 뭐시기로 돌파중 ...

#driver.switch_to.default_content() #처음 상태로 되돌아옴

#git add --all
#git status 
#git commit -am ""
#git push origin master 