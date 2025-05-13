from selenium.webdriver.common.by import By

checkout_page_header = (By.XPATH, "//li[text()='Checkout']")
delivery_address_header = (By.XPATH, "//h3[text()='Your delivery address']")
billing_address_header = (By.XPATH, "//h3[text()='Your billing address']")
comment_textarea = (By.XPATH, "//textarea")
place_order_btn = (By.XPATH, "//a[text()='Place Order']")
review_your_order_header = (By.XPATH, "//h2[text()='Review Your Order']")
checkout_table_headers = (By.XPATH, "//thead//td")
checkout_table_rows = (By.XPATH, "//tbody//tr")
delivery_address_details = (By.XPATH, "//ul[@id='address_delivery']//li")
billing_address_details = (By.XPATH, "//ul[@id='address_invoice']//li")
