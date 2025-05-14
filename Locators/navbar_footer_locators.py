"""navbar and footer locators"""

from selenium.webdriver.common.by import By

account_owner = (By.XPATH, "//a[contains(text(),'Logged in as')]//b")
delete_account_link = (By.XPATH, "//a[contains(text(),'Delete Account')]")
sign_out_link = (By.XPATH, "//a[contains(text(),'Logout')]")
logo_img = (By.XPATH, "//img[contains(@alt,'Website for automation practice')]")
test_cases_link = (By.XPATH, "//a[contains(text(),'Test Cases')]")
products_link = (By.XPATH, "//a[contains(text(),'Products')]")
subscribe_email_field = (By.ID, "susbscribe_email")
subscribe_btn = (By.ID, "subscribe")
subscribe_success_message = (By.XPATH, "//div[@class='alert-success alert']")
home_link = (By.XPATH, "//a[contains(text(),'Home')]")
cart_link = (By.XPATH, "//a[contains(text(),'Cart')]")
login_signup_link = (By.XPATH, "//a[contains(text(),'Signup / Login')]")
