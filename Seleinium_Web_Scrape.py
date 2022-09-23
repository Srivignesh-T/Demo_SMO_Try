import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url =  "https://www.amazon.in/ref=nav_logo"
path = Service('C:/Users/lenovo/Downloads/chromedriver')
driver = webdriver.Chrome(service=path)
driver.get(url)
driver.implicitly_wait(7)
# a = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[4]/div[2]/div/nav/a[4]')
# a.click()
username = "srivignesh297@gmail.com"
password = "Srivignesh@29"

driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[1]/div[3]/div/a[2]/div/span').click()
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[1]/input[1'
                              ']').send_keys(username)
time.sleep(4)
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div['
                              '2]/span/span/input').click()
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/div/form/div/div[1]/inp'
                              'ut').send_keys(password)
time.sleep(4)
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/div/form/div/div['
                              '2]/span/span/input').click()
driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/inp'
                              'ut').send_keys('mobile phone under 10000')
time.sleep(4)
driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input').click()

Mobile_name = driver.find_elements(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
price = driver.find_elements(By.XPATH, "//span[@class='a-price']")
Mobile_name = [print(x.text) for x in Mobile_name]
price = [print(i.text) for i in price]
# print(Mobile_name, price)
print(len(Mobile_name))
print(len(price))



