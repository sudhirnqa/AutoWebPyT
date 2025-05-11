import time

from Locators import (
    navbar_footer_locators,
    case_page_locators,
    products_page_locators,
    home_page_locators,
    login_page_locators,
    cart_page_locators,
)
from Pages.base_element import BaseElement
from Pages.base_page import BasePage
from Pages.cart_page import CartPage
from Pages.cases_page import TestCasesPage
from Pages.products_page import ProductsPage


class NavbarFooter(BasePage):

    @property
    def test_cases_link(self):
        return BaseElement(self.driver, navbar_footer_locators.test_cases_link)

    def click_test_cases_link(self):
        self.test_cases_link.click()
        test_cases_page = TestCasesPage(self.driver)
        test_cases_page.wait_for_page_to_load(case_page_locators.test_case_header)
        return test_cases_page

    @property
    def products_link(self):
        return BaseElement(self.driver, navbar_footer_locators.products_link)

    def click_products_link(self):
        self.products_link.click()
        products_page = ProductsPage(self.driver)
        products_page.wait_for_page_to_load(products_page_locators.products_page_header)
        return products_page

    @property
    def account_owner_name(self):
        return BaseElement(self.driver, navbar_footer_locators.account_owner)

    def get_account_owner_name(self):
        return self.account_owner_name.text

    @property
    def delete_account_link(self):
        return BaseElement(self.driver, navbar_footer_locators.delete_account_link)

    def click_delete_account_link(self):
        self.delete_account_link.click()
        self.wait_for_page_to_load(home_page_locators.account_deleted_header)

    @property
    def sign_out_link(self):
        return BaseElement(self.driver, navbar_footer_locators.sign_out_link)

    def click_sign_out_link(self):
        self.sign_out_link.click()
        self.wait_for_page_to_load(login_page_locators.login_form_header)

    def is_log_out_displayed(self):
        return self.sign_out_link.is_element_displayed()

    @property
    def subscribe_email_field(self):
        return BaseElement(self.driver, navbar_footer_locators.subscribe_email_field)

    @property
    def subscribe_btn(self):
        return BaseElement(self.driver, navbar_footer_locators.subscribe_btn)

    @property
    def subscribe_success_message(self):
        return BaseElement(
            self.driver, navbar_footer_locators.subscribe_success_message
        )

    def enter_subscribe_email_field(self, email):
        self.subscribe_email_field.enter_text(email)

    def click_subscribe_btn(self):
        self.subscribe_btn.click()

    def get_subscribe_success_message(self):
        return self.subscribe_success_message.text

    def is_subscribe_success_message_displayed(self):
        return self.subscribe_success_message.is_element_displayed()

    def is_subscribe_success_message_disappeared(self):
        time.sleep(2)  # toast message should be disappeared exactly after 2 seconds
        return not self.subscribe_success_message.is_element_displayed()

    @property
    def home_link(self):
        return BaseElement(self.driver, navbar_footer_locators.home_link)

    def click_home_page_link(self):
        self.home_link.click()
        self.wait_for_page_to_load(navbar_footer_locators.logo_img)

    @property
    def cart_link(self):
        return BaseElement(self.driver, navbar_footer_locators.cart_link)

    def click_cart_link(self):
        self.cart_link.click()
        cart_page = CartPage(self.driver)
        cart_page.wait_for_page_to_load(cart_page_locators.cart_page_header)
        return cart_page

    def fill_subscription_email_and_click_subscription_btn(self, email):
        self.enter_subscribe_email_field(email)
        self.click_subscribe_btn()
        if self.is_subscribe_success_message_displayed():
            return self.get_subscribe_success_message()
        else:
            # invalid subscription email
            return None
