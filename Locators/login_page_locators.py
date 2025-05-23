"""login page locators"""

from selenium.webdriver.common.by import By

signup_form_header = (By.XPATH, "//div[@class='signup-form']//h2")
signup_form_name = (By.XPATH, "//input[@data-qa='signup-name']")
signup_form_email = (By.XPATH, "//input[@data-qa='signup-email']")
signup_btn = (By.XPATH, "//button[@data-qa='signup-button']")
login_form_header = (By.XPATH, "//div[@class='login-form']//h2")
login_form_email = (By.XPATH, "//input[@data-qa='login-email']")
login_form_password = (By.XPATH, "//input[@data-qa='login-password']")
login_btn = (By.XPATH, "//button[@data-qa='login-button']")
invalid_login_error = (By.XPATH, "//p[text()='Your email or password is incorrect!']")
invalid_signup_error = (By.XPATH, "//p[text()='Email Address already exist!']")
