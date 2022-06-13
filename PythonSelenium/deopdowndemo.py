from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path="D:\\Python_Atul\\chromedriver\\chromedriver.exe")

driver.maximize_window();

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(by=By.NAME,value="name").send_keys("Atul")

driver.find_element(by=By.XPATH, value="//input[@name='email']").send_keys("abc@gmail.com")

dropdown=Select(driver.find_element(by=By.CSS_SELECTOR,value="select[id='exampleFormControlSelect1']"))

dropdown.select_by_visible_text('Female')

dropdown.se

dropdown.select_by_index(0)