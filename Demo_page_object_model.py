# Elements with their locators in the sauce demo web page
username_input = driver.find_element(By.ID, 'user-name')
password_input = driver.find_element(By.ID, 'password')
login_btn = driver.find_element(By.ID, 'login-button')
# Element only available when a login attempt fails
error_message = driver.find_element(By.XPATH, "//div[@class='error-message-container error']")
# Elements available in the home page of the web
cart_icon = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
product_filter = driver.find_element(By.CLASS_NAME, 'product_sort_container')
hamburger = driver.find_element(By.ID, 'react-burger-menu-btn')
logout_btn = driver.find_element(By.ID, 'logout_sidebar_link')
add_cart_btn = driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
# Elements available in the cart menu
remove_cart_btn = driver.find_element(By.ID, 'remove-sauce-labs-backpack')
removed_item = driver.find_element(By.CLASS_NAME, 'removed_cart_item')
