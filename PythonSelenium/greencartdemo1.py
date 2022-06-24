import time

from selenium import webdriver
from selenium.webdriver.common.by import By


lst=[]
lst1=[]
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
    lst.append(button.find_element(by=By.XPATH,value="parent::div/parent::div/h4").text)
    button.click()
print(lst)


driver.find_element(by=By.CSS_SELECTOR,value="img[alt='Cart']").click()
driver.find_element(by=By.XPATH,value="//button[text()='PROCEED TO CHECKOUT']").click()

original_amount=driver.find_element(by=By.CSS_SELECTOR,value=".discountAmt").text
driver.find_element(by=By.CSS_SELECTOR,value="input.promocode").send_keys("rahulshettyacademy")
driver.find_element(by=By.CSS_SELECTOR,value=".promoBtn").click()
promocode=driver.find_element(by=By.CSS_SELECTOR,value=".promoInfo").text
print(promocode)
discounted_amount= driver.find_element(by=By.CSS_SELECTOR,value=".discountAmt").text
names=driver.find_elements(by=By.CSS_SELECTOR,value="p.product-name")
for veg in names:
    lst1.append(veg.text)
print(lst1)
assert lst==lst1
assert float(discounted_amount)<int(original_amount)

amounts= driver.find_elements(by=By.XPATH, value="//tr/td[5]/p")
sum=0
for amount in amounts:
    sum=sum+int(amount.text)
print(sum)

totamt= int(driver.find_element(by=By.CSS_SELECTOR,value=".totAmt").text)

print(totamt)

assert sum==totamt


#//*[@id="productCartTables"]/tbody/tr[2]/td[4]/p