from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\\Python_Atul\\chromedriver\\chromedriver.exe")
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.maximize_window()

print(driver.title)

driver.find_element(by=By.NAME, value='name').send_keys("ATUL")

driver.find_element(by=By.CSS_SELECTOR, value="input[name='email']").send_keys("ABC@gmail.com")

driver.find_element(by=By.ID, value="exampleInputPassword1").send_keys("ASDFG")

driver.find_element(by=By.ID, value="exampleCheck1").click()

driver.find_element(by=By.NAME, value="inlineRadioOptions").click()

driver.find_element(by=By.XPATH, value="//input[@type='submit']").click()

str = driver.find_element(by=By.CLASS_NAME,value='alert-success').text
print(str)