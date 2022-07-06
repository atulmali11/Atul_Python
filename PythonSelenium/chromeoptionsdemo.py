from selenium import webdriver
from selenium.webdriver.chrome.service import Service


options_obj=webdriver.ChromeOptions()
options_obj.add_argument("Headless")
options_obj.add_argument("--Start-Maximized")
options_obj.add_argument("--ignore-certificates-error")
service_obj=Service("D:\\Python_Atul\\chromedriver\\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj,options=options_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice")
driver.close()
