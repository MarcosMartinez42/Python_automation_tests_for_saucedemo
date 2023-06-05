from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("drivers/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
driver.implicitly_wait(20)

# 3 - Logout // In this test we perform a logout from the account
username_input = driver.find_element(By.ID, 'user-name')
password_input = driver.find_element(By.ID, 'password')
login_btn = driver.find_element(By.ID, 'login-button')
username_input.send_keys('standard_user')
password_input.send_keys('secret_sauce')
login_btn.click()
hamburger = driver.find_element(By.ID, 'react-burger-menu-btn')
hamburger.click()
logout_btn = driver.find_element(By.ID, 'logout_sidebar_link')
logout_btn.click()
new_login_btn = driver.find_element(By.XPATH, "//input[@id='login-button']")
new_login_btn.is_displayed()
