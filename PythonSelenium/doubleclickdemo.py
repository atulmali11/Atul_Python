from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By



driver=webdriver.Chrome(executable_path="D:\\Python_Atul\\chromedriver\\chromedriver.exe")
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
driver.maximize_window()
action=ActionChains(driver)
action.context_click(driver.find_element(by=By.ID,value="double-click")).perform()
action.double_click(driver.find_element(by=By.ID,value="double-click")).perform()
alerts=driver.switch_to.alert

assert "You double clicked me!!!, You got to be kidding me"== alerts.text
alerts.accept()

