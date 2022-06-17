

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\\Python_Atul\\chromedriver\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()
#select all checkboxes

checkboxes=driver.find_elements(by=By.XPATH,value="//input[@type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
        #selected=checkbox.is_selected()
        if not checkbox.is_selected():
            checkbox.click()
        #print(selected)

        if checkbox.get_attribute("value")=="option2":
            checkbox.click()
# validate all checkbox are selected or not
            #assert checkbox.is_selected()