from Locators import (
    products_page_locators,
    product_details_page_locators,
    cart_page_locators,
)
from Pages.base_element import BaseElement
from Pages.base_page import BasePage
from Pages.cart_page import CartPage
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
        return BaseElement(
            self.driver, products_page_locators.product_add_to_cart_buttons
        )

    @property
    def view_products(self):
        return BaseElement(self.driver, products_page_locators.view_products)

    @property
    def search_product_field(self):
        return BaseElement(self.driver, products_page_locators.search_product_field)

    @property
    def search_btn(self):
        return BaseElement(self.driver, products_page_locators.search_btn)

    @property
    def continue_shopping_btn(self):
        return BaseElement(self.driver, products_page_locators.continue_shopping_btn)

    @property
    def view_cart_link(self):
        return BaseElement(self.driver, products_page_locators.view_cart_link)

    def click_continue_shopping_btn(self):
        self.continue_shopping_btn.click()

    def click_view_cart_link(self):
        self.view_cart_link.click()
        cart_page = CartPage(self.driver)
        cart_page.wait_for_page_to_load(cart_page_locators.cart_page_header)
        return cart_page

    def enter_search_product_name(self, product_name):
        self.search_product_field.enter_text(product_name)

    def click_search_btn(self):
        self.search_btn.click()

    def search_product(self, product_name):
        self.enter_search_product_name(product_name)
        self.click_search_btn()

    def get_product_names(self):
        return self.product_names.elements_text()

    def get_index_of_product(self, target_product):
        return self.product_names.get_index_of_element_by_text(target_product)

    def click_view_product(self, product_name):
        product_index = self.get_index_of_product(product_name)
        self.view_products.click_element_by_index(product_index)
        product_details_page = ProductDetailsPage(self.driver)
        product_details_page.wait_for_page_to_load(
            product_details_page_locators.product_details
        )
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

    def click_add_to_cart_and_continue_shopping(self, product_name):
        product_index = self.get_index_of_product(product_name)
        self.product_add_to_cart_buttons.click_element_by_index(product_index)
        self.click_continue_shopping_btn()

    def click_add_to_cart_and_view_cart(self, product_name):
        product_index = self.get_index_of_product(product_name)
        self.product_add_to_cart_buttons.click_element_by_index(product_index)
        cart_page = self.click_view_cart_link()
        return cart_page

    @property
    def category_women(self):
        return BaseElement(self.driver, products_page_locators.category_women)

    def click_category_women(self):
        self.category_women.click()

    @property
    def category_women_dress(self):
        return BaseElement(self.driver, products_page_locators.category_women_dress)

    def click_category_women_dress(self):
        self.category_women_dress.click()

    @property
    def category_men(self):
        return BaseElement(self.driver, products_page_locators.category_men)

    def click_category_men(self):
        self.category_men.click()

    @property
    def category_men_jeans(self):
        return BaseElement(self.driver, products_page_locators.category_men_jeans)

    def click_category_men_jeans(self):
        self.category_men_jeans.click()

    @property
    def category_kids(self):
        return BaseElement(self.driver, products_page_locators.category_kids)

    def click_category_kids(self):
        self.category_kids.click()

    @property
    def category_kids_dress(self):
        return BaseElement(self.driver, products_page_locators.category_kids_dress)

    def click_category_kids_dress(self):
        self.category_kids_dress.click()

    @property
    def products_page_header(self):
        return BaseElement(self.driver, products_page_locators.products_page_header)

    def get_products_page_header(self):
        return self.products_page_header.text

    @property
    def category_women_tops(self):
        return BaseElement(self.driver, products_page_locators.category_women_tops)

    def click_category_women_tops(self):
        self.category_women_tops.click()

    @property
    def category_women_saree(self):
        return BaseElement(self.driver, products_page_locators.category_women_saree)

    def click_category_women_saree(self):
        self.category_women_saree.click()

    @property
    def category_men_tshirts(self):
        return BaseElement(self.driver, products_page_locators.category_men_tshirts)

    def click_category_men_tshirts(self):
        self.category_men_tshirts.click()

    @property
    def category_kids_topsshirts(self):
        return BaseElement(self.driver, products_page_locators.category_kids_topsshirts)

    def click_category_kids_topsshirts(self):
        self.category_kids_topsshirts.click()

    @property
    def polo_brand(self):
        return BaseElement(self.driver, products_page_locators.polo_brand)

    def click_polo_brand(self):
        self.polo_brand.click()

    @property
    def hm_brand(self):
        return BaseElement(self.driver, products_page_locators.hm_brand)

    def click_hm_brand(self):
        self.hm_brand.click()

    @property
    def madame_brand(self):
        return BaseElement(self.driver, products_page_locators.madame_brand)

    def click_madame_brand(self):
        self.madame_brand.click()

    @property
    def mast_harbour_brand(self):
        return BaseElement(self.driver, products_page_locators.mast_harbour_brand)

    def click_mast_harbour_brand(self):
        self.mast_harbour_brand.click()

    @property
    def baby_hug_brand(self):
        return BaseElement(self.driver, products_page_locators.baby_hug_brand)

    def click_baby_hug_brand(self):
        self.baby_hug_brand.click()

    @property
    def allen_solly_junior_brand(self):
        return BaseElement(self.driver, products_page_locators.allen_solly_junior_brand)

    def click_allen_solly_junior_brand(self):
        self.allen_solly_junior_brand.click()

    @property
    def kookie_kids_brand(self):
        return BaseElement(self.driver, products_page_locators.kookie_kids_brand)

    def click_kookie_kids_brand(self):
        self.kookie_kids_brand.click()

    @property
    def biba_brand(self):
        return BaseElement(self.driver, products_page_locators.biba_brand)

    def click_biba_brand(self):
        self.biba_brand.click()

    @property
    def polo_brand_stock(self):
        return BaseElement(self.driver, products_page_locators.polo_brand_stock)

    def get_polo_brand_stock(self):
        return int(self.polo_brand_stock.text.replace("(", "").replace(")", ""))

    @property
    def hm_brand_stock(self):
        return BaseElement(self.driver, products_page_locators.hm_brand_stock)

    def get_hm_brand_stock(self):
        return int(self.hm_brand_stock.text.replace("(", "").replace(")", ""))

    @property
    def madame_brand_stock(self):
        return BaseElement(self.driver, products_page_locators.madame_brand_stock)

    def get_madame_brand_stock(self):
        return int(self.madame_brand_stock.text.replace("(", "").replace(")", ""))

    @property
    def mast_harbour_brand_stock(self):
        return BaseElement(self.driver, products_page_locators.mast_harbour_brand_stock)

    def get_mast_harbour_brand_stock(self):
        return int(self.mast_harbour_brand_stock.text.replace("(", "").replace(")", ""))

    @property
    def baby_hug_brand_stock(self):
        return BaseElement(self.driver, products_page_locators.baby_hug_brand_stock)

    def get_baby_hug_brand_stock(self):
        return int(self.baby_hug_brand_stock.text.replace("(", "").replace(")", ""))

    @property
    def allen_solly_junior_brand_stock(self):
        return BaseElement(
            self.driver, products_page_locators.allen_solly_junior_brand_stock
        )

    def get_allen_solly_junior_brand_stock(self):
        return int(
            self.allen_solly_junior_brand_stock.text.replace("(", "").replace(")", "")
        )

    @property
    def kookie_kids_brand_stock(self):
        return BaseElement(self.driver, products_page_locators.kookie_kids_brand_stock)

    def get_kookie_kids_brand_stock(self):
        return int(self.kookie_kids_brand_stock.text.replace("(", "").replace(")", ""))

    @property
    def biba_brand_stock(self):
        return BaseElement(self.driver, products_page_locators.biba_brand_stock)

    def get_biba_brand_stock(self):
        return int(self.biba_brand_stock.text.replace("(", "").replace(")", ""))
