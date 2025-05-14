"""product page locators"""

from selenium.webdriver.common.by import By

products_page_header = (
    By.XPATH,
    "//div[@class='features_items']//h2[@class='title text-center']",
)
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
category_women = (By.XPATH, "//a[contains(@href,'#Women')]")
category_women_dress = (By.XPATH, "//div[@id='Women']//a[contains(text(),'Dress')]")
category_women_tops = (By.XPATH, "//div[@id='Women']//a[contains(text(),'Tops')]")
category_women_saree = (By.XPATH, "//div[@id='Women']//a[contains(text(),'Saree')]")
category_men = (By.XPATH, "//a[contains(@href,'#Men')]")
category_men_jeans = (By.XPATH, "//div[@id='Men']//a[contains(text(),'Jeans')]")
category_men_tshirts = (By.XPATH, "//div[@id='Men']//a[contains(text(),'Tshirts')]")
category_kids = (By.XPATH, "//a[contains(@href,'#Kid')]")
category_kids_dress = (By.XPATH, "//div[@id='Kids']//a[contains(text(),'Dress')]")
category_kids_topsshirts = (
    By.XPATH,
    "//div[@id='Kids']//a[contains(text(),'Tops & Shirts')]",
)
