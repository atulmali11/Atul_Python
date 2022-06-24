from selenium import webdriver
from selenium.webdriver.common.by import By



driver=webdriver.Chrome(executable_path="D:\\Python_Atul\\chromedriver\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.find_element(by=By.LINK_TEXT,value="Click Here").click()
childwindow = driver.window_handles[1]
driver.switch_to.window(childwindow)
print(driver.find_element(by=By.TAG_NAME,value="h3").text)
driver.close()
driver.switch_to.window((driver.window_handles[0]))
assert "Opening a new window" == driver.find_element(by=By.TAG_NAME,value="h3").text

