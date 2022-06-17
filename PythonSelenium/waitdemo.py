#Impicit wait
#Explicit wait
#using time class-->provide by python
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\\Python_Atul\\chromedriver\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(by=By.CSS_SELECTOR,value="input.search-keyword").send_keys("ber")
time.sleep(3)
count=len(driver.find_elements(by=By.XPATH,value="//div[@class='products']/div"))
#print(len(count))
assert count==3

buttons=driver.find_elements(by=By.XPATH,value="//div[@class='product-action']/button")

for button in buttons:
    button.click()

driver.find_element(by=By.CSS_SELECTOR,value="img[alt='Cart']").click()
driver.find_element(by=By.XPATH,value="//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(by=By.CSS_SELECTOR,value="input.promocode").send_keys("rahulshettyacademy")
driver.find_element(by=By.CSS_SELECTOR,value=".promoBtn").click()
promocode=driver.find_element(by=By.CSS_SELECTOR,value=".promoInfo").text
print(promocode)


