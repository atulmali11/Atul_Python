from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\Python_Atul\chromedriver\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.maximize_window()

print(driver.title)

#driver.find_element_by_name("name").send_keys("ATUL")===>by_id

driver.find_element_by_css_selector("input[name='name']").send_keys("ABC")

