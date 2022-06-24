from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By



driver=webdriver.Chrome(executable_path="D:\\Python_Atul\\chromedriver\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
action= ActionChains(driver)
action.move_to_element(driver.find_element(by=By.ID,value="mousehover")).perform()
action.move_to_element(driver.find_element(by=By.LINK_TEXT,value="Top")).click().perform()


