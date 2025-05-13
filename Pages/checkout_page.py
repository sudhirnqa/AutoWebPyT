from Locators import checkout_page_locators, payment_page_locators
from Pages.base_element import BaseElement
from Pages.base_page import BasePage
from Pages.payment_page import PaymentPage


class CheckoutPage(BasePage):
    @property
    def delivery_address_header(self):
        return BaseElement(self.driver, checkout_page_locators.delivery_address_header)

    def get_delivery_address_header(self):
        return self.delivery_address_header.text

    @property
    def billing_address_header(self):
        return BaseElement(self.driver, checkout_page_locators.billing_address_header)

    def get_billing_address_header(self):
        return self.billing_address_header.text

    @property
    def place_order_btn(self):
        return BaseElement(self.driver, checkout_page_locators.place_order_btn)

    def click_place_order_btn(self):
        self.place_order_btn.click()

    @property
    def review_your_order_header(self):
        return BaseElement(self.driver, checkout_page_locators.review_your_order_header)

    def get_review_your_order_header(self):
        self.review_your_order_header.text()

    @property
    def checkout_table_headers(self):
        return BaseElement(self.driver, checkout_page_locators.checkout_table_headers)

    def get_checkout_table_headers(self):
        return self.checkout_table_headers.elements_text()[:-1]

    @property
    def checkout_table_rows(self):
        return BaseElement(self.driver, checkout_page_locators.checkout_table_rows)

    def get_checkout_table_rows(self):
        return self.checkout_table_rows.elements_text()

    def get_count_of_unique_items_in_checkout_table(self):
        return len(self.get_checkout_table_rows())

    def get_checkout_table_row_data(self):
        headers = self.get_checkout_table_headers()
        row_lines = self.get_checkout_table_rows()
        rows = []
        total_amount = 0
        for row_line in row_lines:
            row_data = row_line.split("\n")
            if len(row_data) == len(headers):
                row = dict()
                for index, header in enumerate(headers):
                    if header == "Price":
                        row[header] = int(row_data[index].lstrip("Rs. "))
                    elif header == "Quantity":
                        row[header] = int(row_data[index])
                    elif header == "Total":
                        row[header] = int(row_data[index].lstrip("Rs. "))
                    else:
                        row[header] = row_data[index]
                rows.append(row)
            elif len(row_data) == 2:
                total_amount = int(row_data[1].lstrip("Rs. "))
        return rows, total_amount

    @property
    def delivery_address_details(self):
        return BaseElement(self.driver, checkout_page_locators.delivery_address_details)

    def get_delivery_address_details(self):
        return self.delivery_address_details.elements_text()[1:]

    @property
    def billing_address_details(self):
        return BaseElement(self.driver, checkout_page_locators.billing_address_details)

    def get_billing_address_details(self):
        return self.billing_address_details.elements_text()[1:]

    @property
    def comment_textarea(self):
        return BaseElement(self.driver, checkout_page_locators.comment_textarea)

    def enter_comment_textarea(self, comment):
        self.comment_textarea.enter_text(comment)

    def enter_comment_and_click_place_order_btn(self, comment):
        self.enter_comment_textarea(comment)
        self.click_place_order_btn()
        payment_page = PaymentPage(self.driver)
        payment_page.wait_for_page_to_load(payment_page_locators.payment_header)
        return payment_page
