from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\\Python_Atul\\chromedriver\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")


radiobuttons=driver.find_elements(by=By.XPATH,value="//input[@name='radioButton']")

radiobuttons[1].click()
assert radiobuttons[1].is_selected()

driver.quit()