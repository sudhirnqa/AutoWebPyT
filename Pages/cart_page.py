from Locators import cart_page_locators
from Pages.base_element import BaseElement
from Pages.base_page import BasePage


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
