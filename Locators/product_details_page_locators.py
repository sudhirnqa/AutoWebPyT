from selenium.webdriver.common.by import By

product_details = (By.XPATH, "//div[@class='product-details']")
product_name = (By.XPATH, f"{product_details[1]}//h2")
product_category = (By.XPATH, f"{product_details[1]}//p[contains(text(),'Category')]")
product_price = (By.XPATH, f"{product_details[1]}//span//span")
product_availability = (By.XPATH, f"{product_details[1]}//b[contains(text(),'Availability')]//parent::p")
product_condition = (By.XPATH, f"{product_details[1]}//b[contains(text(),'Condition')]//parent::p")
product_brand = (By.XPATH, f"{product_details[1]}//b[contains(text(),'Brand')]//parent::p")
