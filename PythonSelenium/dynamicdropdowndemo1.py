import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\\Python_Atul\\chromedriver\\chromedriver.exe")

driver.get("https://www.goibibo.com/flights/")

driver.maximize_window()
time.sleep(2)

driver.find_element(by=By.CLASS_NAME,value="sc-iIPllB ezZWci fswWidgetPlaceholder").click()

