"""product details page locators"""

from selenium.webdriver.common.by import By

product_details = (By.XPATH, "//div[@class='product-details']")
product_name = (By.XPATH, f"{product_details[1]}//h2")
product_category = (By.XPATH, f"{product_details[1]}//p[contains(text(),'Category')]")
product_price = (By.XPATH, f"{product_details[1]}//span//span")
product_availability = (
    By.XPATH,
    f"{product_details[1]}//b[contains(text(),'Availability')]//parent::p",
)
product_condition = (
    By.XPATH,
    f"{product_details[1]}//b[contains(text(),'Condition')]//parent::p",
)
product_brand = (
    By.XPATH,
    f"{product_details[1]}//b[contains(text(),'Brand')]//parent::p",
)
quantity_field = (By.ID, "quantity")
add_to_cart_btn = (By.XPATH, "//button[@type='button']")
view_cart_link = (By.XPATH, "//a//u[text()='View Cart']")
review_name_field = (By.ID, "name")
review_email_field = (By.ID, "email")
review_message_textarea = (By.NAME, "review")
submit_review_btn = (By.ID, "button-review")
review_success_message = (By.XPATH, "//div[@class = 'alert-success alert']//span")
