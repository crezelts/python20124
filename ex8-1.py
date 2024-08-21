from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.get("https://www.naver.com")
driver.implicitly_wait(0.5)
query_text=f"부산행 개봉일"
search_box=driver.find_element(by=By.CSS_SELECTOR,value="#query")
search_box.send_keys(query_text)
driver.implicitly_wait(0.5)
search_button=driver.find_element(by=By.ID,value="search-btn")
search_button.click()
driver.implicitly_wait(0.5)
date_div=driver.find_element(by=By.CSS_SELECTOR,value="#main_pack > div.sc_new.cs_common_module.case_empasis.color_6._au_movie_content_wrap > div.cm_content_wrap > div.cm_content_area._cm_content_area_info > div > div.detail_info > dl > div:nth-child(1) ")
print("20206 김민서")
print(date_div.text)

time.sleep(10) 