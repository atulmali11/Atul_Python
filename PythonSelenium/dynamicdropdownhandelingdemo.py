import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.drivers.edge import EdgeChromiumDriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
#driver=webdriver.Chrome(executable_path="D:\\Python_Atul\\chromedriver\\chromedriver.exe")
driver.get("https://www.google.com")
driver.maximize_window()
driver.find_element(by=By.CSS_SELECTOR,value="input[name='q']").send_keys("Selenium")
#list1=[]
time.sleep(3)
list1=driver.find_elements(by=By.CSS_SELECTOR, value="li[class='sbct']")
print(len(list1))
time.sleep(3)
#driver.find_element(by=By.XPATH,value="//*[normalize-space()='selenium download']").click()

for element in list1:
    if(element.text=='selenium download'):
        element.click()
        break

driver.quit()