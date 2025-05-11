"""product page locators"""

from selenium.webdriver.common.by import By

products_page_header = (By.XPATH, "//h2[text()='All Products']")
product_cards = (By.XPATH, "//div[@class='productinfo text-center']")
product_names = (By.XPATH, f"{product_cards[1]}//p")
product_prices = (By.XPATH, f"{product_cards[1]}//h2")
product_add_to_cart_buttons = (By.XPATH, f"{product_cards[1]}//a")
view_products = (
    By.XPATH,
    f"{product_cards[1]}//ancestor::div[@class='single-products']"
    f"//following-sibling::div[@class='choose']//a",
)
search_product_field = (By.ID, "search_product")
search_btn = (By.ID, "submit_search")
continue_shopping_btn = (By.XPATH, "//button[text()='Continue Shopping']")
view_cart_link = (By.XPATH, "//a//u[text()='View Cart']")
