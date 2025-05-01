
from selenium.webdriver.common.by import By

from Locators import Login_page_locators
from Pages.base_element import BaseElement
from Pages.base_page import BasePage


class LoginPage(BasePage):

    @property
    def signup_form_header(self):
        return BaseElement(self.driver, Login_page_locators.signup_form_header)

    def get_signup_form_header_text(self):
        return self.signup_form_header.text

    @property
    def signup_form_name(self):
        return BaseElement(self.driver, Login_page_locators.signup_form_name)

    def enter_signup_name(self, name):
        self.signup_form_name.enter_text(name)

    @property
    def signup_form_email(self):
        return BaseElement(self.driver, Login_page_locators.signup_form_email)

    def enter_signup_email(self, email):
        self.signup_form_email.enter_text(email)

    @property
    def signup_btn(self):
        return BaseElement(self.driver, Login_page_locators.signup_btn)

    def click_signup_btn(self):
        self.signup_btn.click()

    @property
    def login_email_field(self):
        return BaseElement(self.driver, Login_page_locators.login_form_email)

    def enter_login_email(self, email):
        self.login_email_field.enter_text(email)

    @property
    def login_in_password_field(self):
        return BaseElement(self.driver, Login_page_locators.login_form_password)

    def enter_login_password(self, password):
        self.login_in_password_field.enter_text(password)

    @property
    def login_btn(self):
        return BaseElement(self.driver, Login_page_locators.login_btn)

    def click_login_btn(self):
        self.login_btn.click()

    @property
    def login_form_header(self):
        return BaseElement(self.driver, Login_page_locators.login_form_header)

    def get_login_form_header_text(self):
        return self.login_form_header.text

    def is_login_form_header_displayed(self):
        return self.login_form_header.is_element_displayed()

    @property
    def invalid_login_error(self):
        return BaseElement(self.driver, Login_page_locators.invalid_login_error)

    def get_invalid_login_error_text(self):
        return self.invalid_login_error.text

    def fill_login_form_and_click_login_btn(self, email, password):
        self.enter_login_email(email)
        self.enter_login_password(password)
        self.login_btn.click()

    def fill_signup_form_and_click_signup_btn(self, name, email):
        self.enter_signup_name(name)
        self.enter_signup_email(email)
        self.signup_btn.click()