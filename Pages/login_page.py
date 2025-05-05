from Locators import login_page_locators, home_page_locators, signup_page_locators, case_page_locators
from Pages.base_element import BaseElement
from Pages.base_page import BasePage
from Pages.cases_page import TestCasesPage
from Pages.home_page import HomePage
from Pages.signup_page import SignupPage


class LoginPage(BasePage):

    @property
    def signup_form_header(self):
        return BaseElement(self.driver, login_page_locators.signup_form_header)

    def get_signup_form_header_text(self):
        return self.signup_form_header.text

    @property
    def signup_form_name(self):
        return BaseElement(self.driver, login_page_locators.signup_form_name)

    def enter_signup_name(self, name):
        self.signup_form_name.enter_text(name)

    @property
    def signup_form_email(self):
        return BaseElement(self.driver, login_page_locators.signup_form_email)

    def enter_signup_email(self, email):
        self.signup_form_email.enter_text(email)

    @property
    def signup_btn(self):
        return BaseElement(self.driver, login_page_locators.signup_btn)

    def click_signup_btn(self):
        self.signup_btn.click()

    @property
    def login_email_field(self):
        return BaseElement(self.driver, login_page_locators.login_form_email)

    def enter_login_email(self, email):
        self.login_email_field.enter_text(email)

    @property
    def login_in_password_field(self):
        return BaseElement(self.driver, login_page_locators.login_form_password)

    def enter_login_password(self, password):
        self.login_in_password_field.enter_text(password)

    @property
    def login_btn(self):
        return BaseElement(self.driver, login_page_locators.login_btn)

    def click_login_btn(self):
        self.login_btn.click()

    @property
    def login_form_header(self):
        return BaseElement(self.driver, login_page_locators.login_form_header)

    def get_login_form_header_text(self):
        return self.login_form_header.text

    def is_login_form_header_displayed(self):
        return self.login_form_header.is_element_displayed()

    @property
    def invalid_login_error(self):
        return BaseElement(self.driver, login_page_locators.invalid_login_error)

    def get_invalid_login_error_text(self):
        return self.invalid_login_error.text

    @property
    def invalid_signup_error(self):
        return BaseElement(self.driver, login_page_locators.invalid_signup_error)

    def get_invalid_signup_error_text(self):
        return self.invalid_signup_error.text

    def fill_login_form_and_click_login_btn(self, email, password):
        self.enter_login_email(email)
        self.enter_login_password(password)
        self.click_login_btn()
        if not self.invalid_login_error.is_element_displayed():
            home_page = HomePage(self.driver)
            home_page.wait_for_page_to_load(home_page_locators.account_owner)
            return home_page
        return None

    def fill_signup_form_and_click_signup_btn(self, name, email):
        self.enter_signup_name(name)
        self.enter_signup_email(email)
        self.signup_btn.click()
        if not self.invalid_signup_error.is_element_displayed():
            signup_page = SignupPage(self.driver)
            signup_page.wait_for_page_to_load(signup_page_locators.signup_page_header)
            return signup_page
        return None

    @property
    def test_cases_link(self):
        return BaseElement(self.driver, login_page_locators.test_cases_link)

    def click_test_cases_link(self):
        self.test_cases_link.click()
        test_cases_page = TestCasesPage(self.driver)
        test_cases_page.wait_for_page_to_load(case_page_locators.test_case_header)
        return test_cases_page
