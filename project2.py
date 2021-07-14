# 爬取ig關鍵字圖片
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import wget

PATH = "C:/Users/hibyby/Desktop/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.instagram.com/")

username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)
password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
)
login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')

username.clear()
password.clear()
username.send_keys('你的帳號')
password.send_keys('你的密碼')
login.click()

search = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'))
)
keyword = "#dog"
search.send_keys(keyword)
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(1)
search.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "FFVAD"))
)

for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

imgs = driver.find_elements_by_class_name("FFVAD")

path = os.path.join(keyword)
os.mkdir(path)

count = 0
for img in imgs:
    save_as = os.path.join(path, keyword + str(count) + '.jpg')
    # print(img.get_attribute("src"))
    wget.download(img.get_attribute("src"), save_as)
    count += 1


