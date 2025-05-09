from Locators import signup_page_locators, navbar_footer_locators
from Pages.base_element import BaseElement
from Pages.base_page import BasePage
from Pages.home_page import HomePage
from Utilities.common_utils import custom_logger


class SignupPage(BasePage):

    @property
    def mr_radio_btn(self):
        return BaseElement(self.driver, signup_page_locators.mr_radio_btn)

    def click_mr_radio_btn(self):
        self.mr_radio_btn.click()

    @property
    def signup_name(self):
        return BaseElement(self.driver, signup_page_locators.signup_name_field)

    def get_signup_name(self):
        return self.signup_name.attribute("value")

    @property
    def sighup_email(self):
        return BaseElement(self.driver, signup_page_locators.signup_email_field)

    def get_signup_email(self):
        return self.sighup_email.attribute("value")

    @property
    def signup_password(self):
        return BaseElement(self.driver, signup_page_locators.signup_password_field)

    def enter_signup_password(self, password):
        self.signup_password.enter_text(password)

    @property
    def day_of_birth_dropdown(self):
        return BaseElement(self.driver, signup_page_locators.day_of_birth_dropdown)

    def select_day_of_birth(self, select_by_type, value):
        self.day_of_birth_dropdown.select_dropdown(select_by_type, value)

    @property
    def month_of_birth_dropdown(self):
        return BaseElement(self.driver, signup_page_locators.month_of_birth_dropdown)

    def select_month_of_birth(self, select_by_type, value):
        self.month_of_birth_dropdown.select_dropdown(select_by_type, value)

    @property
    def year_of_birth_dropdown(self):
        return BaseElement(self.driver, signup_page_locators.year_of_birth_dropdown)

    def select_year_of_birth(self, select_by_type, value):
        self.year_of_birth_dropdown.select_dropdown(select_by_type, value)

    @property
    def newsletter_checkbox(self):
        return BaseElement(self.driver, signup_page_locators.newsletter_checkbox)

    def click_newsletter_checkbox(self):
        self.newsletter_checkbox.click()

    @property
    def special_offers_checkbox(self):
        return BaseElement(self.driver, signup_page_locators.special_offers_checkbox)

    def click_special_offers_checkbox(self):
        self.special_offers_checkbox.click()

    @property
    def first_name(self):
        return BaseElement(self.driver, signup_page_locators.first_name_field)

    def enter_first_name(self, first_name):
        self.first_name.enter_text(first_name)

    @property
    def last_name(self):
        return BaseElement(self.driver, signup_page_locators.last_name_field)

    def enter_last_name(self, last_name):
        self.last_name.enter_text(last_name)

    @property
    def company_name(self):
        return BaseElement(self.driver, signup_page_locators.company_name_field)

    def enter_company_name(self, company_name):
        self.company_name.enter_text(company_name)

    @property
    def address_1(self):
        return BaseElement(self.driver, signup_page_locators.address_1_field)

    def enter_address_1(self, address_1):
        self.address_1.enter_text(address_1)

    @property
    def address_2(self):
        return BaseElement(self.driver, signup_page_locators.address_2_field)

    def enter_address_2(self, address_2):
        self.address_2.enter_text(address_2)

    @property
    def country_dropdown(self):
        return BaseElement(self.driver, signup_page_locators.country_dropdown)

    def select_country_dropdown(self, select_by_type, value):
        self.country_dropdown.select_dropdown(select_by_type, value)

    @property
    def state(self):
        return BaseElement(self.driver, signup_page_locators.state_field)

    def enter_state(self, state):
        self.state.enter_text(state)

    @property
    def city(self):
        return BaseElement(self.driver, signup_page_locators.city_field)

    def enter_city(self, city):
        self.city.enter_text(city)

    @property
    def zipcode(self):
        return BaseElement(self.driver, signup_page_locators.zipcode_field)

    def enter_zipcode(self, zipcode):
        self.zipcode.enter_text(zipcode)

    @property
    def mobile_number(self):
        return BaseElement(self.driver, signup_page_locators.mobile_number_field)

    def enter_mobile_number(self, mobile_number):
        self.mobile_number.enter_text(mobile_number)

    @property
    def create_account_btn(self):
        return BaseElement(self.driver, signup_page_locators.create_account_btn)

    def click_create_account_btn(self):
        self.create_account_btn.click()

    @property
    def account_created_header(self):
        return BaseElement(self.driver, signup_page_locators.account_created_header)

    def get_account_created_header_text(self):
        return self.account_created_header.text

    @property
    def continue_btn(self):
        return BaseElement(self.driver, signup_page_locators.continue_btn)

    def click_continue_btn(self):
        self.continue_btn.click()
        home_page = HomePage(self.driver)
        home_page.wait_for_page_to_load(navbar_footer_locators.account_owner)
        return home_page

    @property
    def account_created_message(self):
        return BaseElement(self.driver, signup_page_locators.account_created_message)

    def get_account_created_message_text(self):
        return self.account_created_message.text

    def fill_signup_form_and_click_continue_btn(self, test_data):
        log = custom_logger()
        if isinstance(test_data, dict):
            log.info("Filling out the signup form with provided test data.")
            self.click_mr_radio_btn()
            self.enter_signup_password(test_data["password"])
            self.select_day_of_birth("text", str(test_data["date_of_birth"].day))
            self.select_month_of_birth("index", str(test_data["date_of_birth"].month))
            self.select_year_of_birth("value", str(test_data["date_of_birth"].year))
            self.click_newsletter_checkbox()
            self.click_special_offers_checkbox()
            self.enter_first_name(test_data["first_name"])
            self.enter_last_name(test_data["last_name"])
            self.enter_company_name(test_data["company"])
            self.enter_address_1(test_data["address_1"])
            self.enter_address_2(test_data["address_2"])
            self.select_country_dropdown(select_by_type="text", value="India")
            self.enter_state(test_data["state"])
            self.enter_city(test_data["city"])
            self.enter_zipcode(test_data["zipcode"])
            self.enter_mobile_number(test_data["phone_number"])
            self.click_create_account_btn()
            if not self.account_created_header.is_element_displayed():
                log.error("Account creation failed. Please check the provided data.")
                raise Exception(
                    "Account creation failed. Please check the provided data."
                )
        else:
            log.error("Invalid test data format. Please provide a dictionary.")
            raise TypeError("test_data should be a dictionary")
