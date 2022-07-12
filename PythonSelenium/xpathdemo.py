from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj=Service("D:\\Python_Atul\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)

driver.get("https://theautomationzone.blogspot.com/2020/07/xpath-practice.html")
driver.close()

wait=WebDriverWait(driver,5)
wait.until(expected_conditions.presence_of_element_located(driver.find_element(by=By.XPATH,value="//*[@id='id1']")))
print(driver.find_element(by=By.XPATH,value="//*[@id='id1']"))
