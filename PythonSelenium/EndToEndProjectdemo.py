from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj=Service("D:\\Python_Atul\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)


driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
wait=WebDriverWait(driver,15)
"""
driver.find_element(by=By.XPATH,value="//input[@minlength='2']").send_keys("ATUL")
driver.find_element(by=By.XPATH, value="//input[@name='email']").send_keys("abc@gmail.com")
driver.find_element(by=By.ID,value="exampleInputPassword1").send_keys('12345')
driver.find_element(by=By.ID,value="exampleCheck1").click()
dropdown=Select(driver.find_element(by=By.XPATH,value="//select[@class='form-control']"))
dropdown.select_by_visible_text("Male")
driver.find_element(by=By.XPATH,value="//input[@id='inlineRadio1']").click()
"""

driver.find_element(by=By.XPATH,value="//a[text()='Shop']").click()

carttitle=driver.find_elements(by=By.XPATH,value="//div[@class='card h-100']")

for cart in carttitle:
    cartname=cart.find_element(by=By.XPATH, value="div/h4/a").text
    print(cartname)
    if cartname == "Blackberry":
        cart.find_element(by=By.XPATH, value="div/button").click()

driver.find_element(by=By.CSS_SELECTOR,value="a[class*='btn-primary']").click()
#driver.implicitly_wait(5)
driver.find_element(by=By.CSS_SELECTOR,value="button[class='btn btn-success']").click()

driver.find_element(by=By.CSS_SELECTOR, value="input[id='country']").send_keys("IND")

driver.implicitly_wait(10)
driver.find_element(by=By.XPATH,value="//a[text()='India']")

driver.find_element(by=By.LINK_TEXT,value="India").click()

driver.find_element(by=By.XPATH,value="//div[@class='checkbox checkbox-primary']").click()

driver.find_element(by=By.XPATH, value="//input[@type='submit']").click()

alertmsg=driver.find_element(by=By.XPATH,value="//div[@class='alert alert-success alert-dismissible']").text

print(alertmsg)
assert "Success! Thank you!" in alertmsg


driver.close()

