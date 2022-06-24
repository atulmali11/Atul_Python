from selenium import webdriver
from selenium.webdriver.common.by import By



driver=webdriver.Chrome(executable_path="D:\\Python_Atul\\chromedriver\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com")

driver.maximize_window()

driver.find_element(by=By.XPATH,value="//a[@href='/frames']").click()
driver.find_element(by=By.XPATH,value="//a[@href='/iframe']").click()
driver.switch_to.frame("mce_0_ifr")
driver.find_element(by=By.CSS_SELECTOR,value="#tinymce").clear()
driver.find_element(by=By.CSS_SELECTOR,value="#tinymce").send_keys("Atul Mali")

driver.switch_to.default_content()

print(driver.find_element(by=By.CSS_SELECTOR,value="h3").text)

