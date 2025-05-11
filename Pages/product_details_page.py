from Locators import product_details_page_locators, cart_page_locators
from Pages.base_element import BaseElement
from Pages.base_page import BasePage
from Pages.cart_page import CartPage


class ProductDetailsPage(BasePage):
    @property
    def product_name(self):
        return BaseElement(self.driver, product_details_page_locators.product_name)

    @property
    def product_category(self):
        return BaseElement(self.driver, product_details_page_locators.product_category)

    @property
    def product_price(self):
        return BaseElement(self.driver, product_details_page_locators.product_price)

    @property
    def product_availability(self):
        return BaseElement(
            self.driver, product_details_page_locators.product_availability
        )

    @property
    def product_condition(self):
        return BaseElement(self.driver, product_details_page_locators.product_condition)

    @property
    def product_brand(self):
        return BaseElement(self.driver, product_details_page_locators.product_brand)

    def get_product_name(self):
        return self.product_name.text

    def get_product_category(self):
        return self.product_category.text

    def get_product_price(self):
        return self.product_price.text

    def get_product_availability(self):
        return self.product_availability.text

    def get_product_condition(self):
        return self.product_condition.text

    def get_product_brand(self):
        return self.product_brand.text

    def get_product_details(self):
        product_details = {
            "name": self.get_product_name(),
            "price": self.get_product_price(),
            "category": self.get_product_category().split("Category: ")[1],
            "Availability": self.get_product_availability().split("Availability: ")[1],
            "Condition": self.get_product_condition().split("Condition: ")[1],
            "Brand": self.get_product_brand().split("Brand: ")[1],
        }
        return product_details

    @property
    def quantity_field(self):
        return BaseElement(self.driver, product_details_page_locators.quantity_field)

    def clear_quantity_field(self):
        self.quantity_field.clear_element_text()

    def enter_quantity_field(self, quantity):
        self.quantity_field.enter_text(quantity)

    @property
    def add_to_cart_btn(self):
        return BaseElement(self.driver, product_details_page_locators.add_to_cart_btn)

    def click_add_to_cart_btn(self):
        self.add_to_cart_btn.click()

    @property
    def view_cart_link(self):
        return BaseElement(self.driver, product_details_page_locators.view_cart_link)

    def click_view_cart_link(self):
        self.view_cart_link.click()
        cart_page = CartPage(self.driver)
        cart_page.wait_for_page_to_load(cart_page_locators.cart_page_header)
        return cart_page

    def enter_quantity_and_click_add_to_cart(self, quantity):
        self.clear_quantity_field()
        self.enter_quantity_field(quantity)
        self.click_add_to_cart_btn()
        cart_page = self.click_view_cart_link()
        return cart_page
