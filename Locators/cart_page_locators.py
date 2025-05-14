from selenium.webdriver.common.by import By

cart_page_header = (By.XPATH, "//li[text()='Shopping Cart']")
cart_table_headers = (By.XPATH, "//thead//td")
cart_table_rows = (By.XPATH, "//tbody//tr")
table_data = (By.XPATH, "//td")
proceed_to_checkout_link = (By.XPATH, "//a[text()='Proceed To Checkout']")
continue_on_cart_link = (By.XPATH, "//button[text()='Continue On Cart']")
register_login_link = (By.XPATH, "//a//u[text()='Register / Login']")
cart_item_names = (By.XPATH, "//h4//a")
cart_item_delete_fields = (By.XPATH, "//a[@class='cart_quantity_delete']")
cart_empty_message = (By.XPATH, "//span[@id]//b")
