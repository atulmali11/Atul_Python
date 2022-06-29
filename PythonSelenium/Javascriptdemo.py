import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


#Scroll down or up


chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("Headless")

service_obj= Service("D:\\Python_Atul\\chromedriver\\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj,options=chrome_option)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scrollBy(0,200)")
time.sleep(5)
driver.execute_script("window.scrollBy(0,-200)")

#Scrrenshot
driver.get_screenshot_as_file("Screenshot.png")


#Headless mode


