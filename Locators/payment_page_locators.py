from selenium.webdriver.common.by import By

payment_header = (By.XPATH, "//h2[text()='Payment']")
name_on_card_field = (By.NAME, "name_on_card")
card_number_field = (By.NAME, "card_number")
card_cvc_field = (By.NAME, "cvc")
expiry_month_field = (By.NAME, "expiry_month")
expiry_year_field = (By.NAME, "expiry_year")
pay_and_confirm_order_btn = (By.ID, "submit")
order_confirmation_header = (By.XPATH, "//h2//b[text()='Order Placed!']")
continue_btn = (By.XPATH, "//a[text()='Continue']")
download_invoice_btn = (By.XPATH, "//a[text()='Download Invoice']")
