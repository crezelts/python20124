from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://time.navyism.com/?host=naver.com")
driver.implicitly_wait(0.5)
while True:
    message=driver.find_element(by=By.ID,value="time_area")
    servertime=message.text
    print(servertime)
    if servertime=="2024년 04월 01일 12시 14분 00초":
        break
print("시간초과~")

time.sleep(10)