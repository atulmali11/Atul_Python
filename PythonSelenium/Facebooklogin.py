from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#driver initialization
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

username='username'
password='password'
service_obj=Service("D:\\Python_Atul\\chromedriver_win32\\chromedriver.exe")
driver= webdriver.Chrome(service=service_obj)
wait=WebDriverWait(driver,10)
#Facebook url
driver.get("https://www.facebook.com/")
driver.maximize_window()
#Login to facebook
wait.until(expected_conditions.visibility_of(driver.find_element(by=By.CSS_SELECTOR, value="#email"))).send_keys(username)
wait.until(expected_conditions.visibility_of(driver.find_element(by=By.CSS_SELECTOR, value="#pass"))).send_keys(password)
driver.find_element(by=By.XPATH,value="//button[@name='login']").click()
#click on post section
wait.until(expected_conditions.visibility_of(driver.find_element(by=By.XPATH,value="//span[contains(text(),'on your mind,')]"))).click()
try:
    wait.until(expected_conditions.visibility_of(driver.find_element(by=By.XPATH,value="//div[contains(@aria-label,'on your mind,')]/p"))).send_keys("Hello")
except:
    for x in range(1,11):

        try:
            wait.until(expected_conditions.visibility_of(driver.find_element(by=By.XPATH, value="//div[contains(@aria-label,'on your mind,')]/p"))).send_keys("Hello")
            break
        except:
            print("Try one more time")
wait.until(expected_conditions.visibility_of(driver.find_element(by=By.XPATH,value="//span[text()='Post']"))).click()




