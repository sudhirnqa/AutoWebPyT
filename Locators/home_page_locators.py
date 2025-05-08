"""home page locators"""
from selenium.webdriver.common.by import By

account_deleted_header = (By.XPATH, "//h2//b[text()='Account Deleted!']")
account_deleted_message = (By.XPATH, "//h2[@data-qa]//following-sibling::p")
continue_btn = (By.XPATH, "//a[text()='Continue']")
