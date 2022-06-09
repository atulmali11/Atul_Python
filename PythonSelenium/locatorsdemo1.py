from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\\Python_Atul\\chromedriver\\chromedriver.exe")

driver.get("https://login.salesforce.com/")

driver.maximize_window()

driver.find_element(by=By.CSS_SELECTOR,value='#username').send_keys("Atul")
driver.find_element(by=By.CLASS_NAME, value='input.password').send_keys("MALI")
driver.find_element(by=By.CLASS_NAME, value='input.password').clear()

driver.find_element(by=By.LINK_TEXT,value='Forgot Your Password?').click()

driver.find_element(by=By.XPATH,value="//input[text()='Cancel']").click()