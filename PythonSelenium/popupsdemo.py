from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\\Python_Atul\\chromedriver\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
validatetext="ATUL"
driver.find_element(by=By.CSS_SELECTOR,value='#name').send_keys(validatetext)
driver.find_element(by=By.CSS_SELECTOR,value="#alertbtn").click()


alert=driver.switch_to.alert
alerttext=alert.text
assert validatetext in alerttext
alert.accept()
