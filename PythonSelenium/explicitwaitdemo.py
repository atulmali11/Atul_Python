#Impicit wait
#Explicit wait
#using time class-->provide by python
import time
from logging import exception

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome(executable_path="D:\\Python_Atul\\chromedriver\\chromedriver.exe")
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
wait=WebDriverWait(driver,4)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,'.promocode')))
driver.find_element(by=By.CSS_SELECTOR,value="input.promocode").send_keys("rahulshettyacademy")
driver.find_element(by=By.CSS_SELECTOR,value=".promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//span[text()='Code applied ..!']")))
promocode=driver.find_element(by=By.CSS_SELECTOR,value=".promoInfo").text

print(promocode)


