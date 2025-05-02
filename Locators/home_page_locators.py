"""Locators for the home page."""
from selenium.webdriver.common.by import By

account_owner = (By.XPATH, "//a[contains(text(),'Logged in as')]//b")
delete_account_link = (By.XPATH, "//a[contains(text(),'Delete Account')]")
sign_out_link = (By.XPATH, "//a[contains(text(),'Logout')]")
account_deleted_header = (By.XPATH, "//h2//b[text()='Account Deleted!']")
continue_btn = (By.XPATH, "//a[text()='Continue']")
