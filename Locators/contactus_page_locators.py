"""contact us page locators"""
from selenium.webdriver.common.by import By

contactus_page_header = (By.XPATH, "//div[@class='bg']//h2")
contactus_form_header = (By.XPATH, "//div[@class='contact-form']//h2")
contactus_name_field = (By.NAME, "name")
contactus_email_field = (By.NAME, "email")
contactus_subject_field = (By.NAME, "subject")
contactus_message_field = (By.XPATH, "//textarea[@id='message']")
contactus_file_upload = (By.CSS_SELECTOR, "input[name='upload_file']")
contactus_submit_btn = (By.NAME, "submit")
contactus_success_message = (By.CSS_SELECTOR, ".status.alert.alert-success")
