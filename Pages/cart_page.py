from Locators import cart_page_locators, login_page_locators, checkout_page_locators
from Pages.base_element import BaseElement
from Pages.base_page import BasePage
from Pages.checkout_page import CheckoutPage
from Pages.login_page import LoginPage


class CartPage(BasePage):
    @property
    def cart_table_headers(self):
        return BaseElement(self.driver, cart_page_locators.cart_table_headers)

    def get_cart_table_headers(self):
        return self.cart_table_headers.elements_text()[:-1]

    @property
    def cart_table_rows(self):
        return BaseElement(self.driver, cart_page_locators.cart_table_rows)

    def get_cart_table_rows(self):
        return self.cart_table_rows.elements_text()

    def get_count_of_unique_items_in_cart(self):
        return len(self.cart_table_rows.elements_text())

    def get_cart_table_row_data(self):
        headers = self.get_cart_table_headers()
        row_lines = self.get_cart_table_rows()
        rows = []
        for row_line in row_lines:
            row = row_line.split("\n")
            row_data = dict()
            if len(row) != len(headers):
                raise ValueError("The number of headers and rows are not equal.")
            else:
                for index, header in enumerate(headers):
                    row_data[header] = row[index]
                rows.append(row_data)
        return rows

    def click_proceed_to_checkout_link(self):
        self.proceed_to_checkout_link.click()
        if not self.register_login_link.is_element_displayed():
            checkout_page = CheckoutPage(self.driver)
            checkout_page.wait_for_page_to_load(
                checkout_page_locators.checkout_page_header
            )
            return checkout_page
        return None

    @property
    def proceed_to_checkout_link(self):
        return BaseElement(self.driver, cart_page_locators.proceed_to_checkout_link)

    @property
    def continue_on_cart_link(self):
        return BaseElement(self.driver, cart_page_locators.continue_on_cart_link)

    def click_continue_on_cart_link(self):
        self.continue_on_cart_link.click()

    @property
    def register_login_link(self):
        return BaseElement(self.driver, cart_page_locators.register_login_link)

    def click_register_login_link(self):
        self.register_login_link.click()
        login_page = LoginPage(self.driver)
        login_page.wait_for_page_to_load(login_page_locators.signup_form_header)
        return login_page
