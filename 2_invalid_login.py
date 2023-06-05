from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("drivers/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
driver.implicitly_wait(20)

# 2 - Invalid login // In this test, we perform a login with invalid credentials
# then we ensure a warning is present in the page
username_input = driver.find_element(By.ID, 'user-name')
password_input = driver.find_element(By.ID, 'password')
login_btn = driver.find_element(By.ID, 'login-button')
username_input.send_keys('asd')
password_input.send_keys('asd')
login_btn.click()
error_message = driver.find_element(By.XPATH, "//div[@class='error-message-container error']")
error_message.is_displayed()
