"""test cases page locators"""
from selenium.webdriver.common.by import By

test_case_header = (By.XPATH, "//h2//b[text()='Test Cases']")
test_case_label = (By.XPATH, "//h5")
test_cases_links_to_toggle = (By.XPATH,
                              "//div[starts-with(@id,'collapse')]//ancestor::div[@class='panel-group']//a[@data-toggle]")
