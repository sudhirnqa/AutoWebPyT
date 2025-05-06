from Locators import products_page_locators, product_details_page_locators
from Pages.base_element import BaseElement
from Pages.base_page import BasePage
from Pages.product_details_page import ProductDetailsPage


class ProductsPage(BasePage):

    @property
    def product_cards(self):
        return BaseElement(self.driver, products_page_locators.product_cards)

    @property
    def product_names(self):
        return BaseElement(self.driver, products_page_locators.product_names)

    @property
    def product_prices(self):
        return BaseElement(self.driver, products_page_locators.product_prices)

    @property
    def product_add_to_cart_buttons(self):
        return BaseElement(self.driver, products_page_locators.product_add_to_cart_buttons)

    @property
    def view_products(self):
        return BaseElement(self.driver, products_page_locators.view_products)

    def get_product_names(self):
        return self.product_names.elements_text()

    def get_index_of_product(self, target_product):
        return self.product_names.get_index_of_element_by_text(target_product)

    def click_view_product(self, product_name):
        product_index = self.get_index_of_product(product_name)
        self.view_products.click_element_by_index(product_index)
        windows_count = self.get_windows_count()
        if windows_count > 1:
            self.close_other_tabs_and_switch_to_parent_tab()
            self.view_products.click_element_by_index(product_index)
        product_details_page = ProductDetailsPage(self.driver)
        product_details_page.wait_for_page_to_load(product_details_page_locators.product_details)
        return product_details_page

    def get_product_prices(self):
        return self.product_prices.elements_text()

    def get_products_as_dict(self):
        products = dict()
        product_names = self.get_product_names()
        product_prices = self.get_product_prices()
        if len(product_names) == len(product_prices):
            for i in range(len(product_names)):
                products[product_names[i].strip()] = product_prices[i].strip()
        return products
