# how to invoke the browser
from selenium import webdriver

#driver=webdriver.Chrome(executable_path="D:\Python_Atul\chromedriver\chromedriver.exe")

#driver=webdriver.Firefox(executable_path='D:\Python_Atul\geckodriver\geckodriver.exe')

driver=webdriver.Ie(executable_path="D:\Python_Atul\IEDriverServer\IEDriverServer.exe")

driver.get("https://rahulshettyacademy.com/")


print("Chrome browser succesfully opened and landed on specific page")

print(driver.title)

print(driver.current_url)



driver.get("https://rahulshettyacademy.com/practice-project")

driver.back()
driver.refresh()
driver.maximize_window()
driver.minimize_window()
#driver.close()
