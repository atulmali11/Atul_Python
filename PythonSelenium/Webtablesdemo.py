import time

import webdriver_manager.drivers.chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
autosortedlst=[]
service_obj=Service("D:\\Python_Atul\\chromedriver\\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(by=By.XPATH, value="//a[text()='Top Deals']").click()
time.sleep(2)
childwindow=driver.window_handles[1]
driver.switch_to.window(childwindow)
driver.find_element(by=By.XPATH,value="//span[text()='Veg/fruit name']").click()

vegnames=driver.find_elements(by=By.XPATH, value="//tr/td[1]")

for vname in vegnames:
    autosortedlst.append(vname.text)
print(autosortedlst)

originallst=autosortedlst

sortlst=autosortedlst.sort()

assert originallst==autosortedlst
