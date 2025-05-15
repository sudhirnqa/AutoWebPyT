import pytest
from pytest import fixture, mark

from Helpers.common_file_helpers import load_data_from_json
from Pages.navbar_footer import NavbarFooter


@mark.usefixtures("setup_teardown_class")
class TestProducts:
    """Test class for products."""

    # Parameterize testdata
    product_to_search_list = load_data_from_json("./Testdata/products_data.json")[
        "product_to_search"
    ]
    product_to_search = [
        tuple(product_dict.values()) for product_dict in product_to_search_list
    ]

    @fixture(autouse=True)
    def setup_teardown_test(self):
        nav_footer = NavbarFooter(self.driver)
        product_page = nav_footer.click_products_link()
        yield product_page
        self.driver.delete_all_cookies()

    def test_product_listing(self, setup_teardown_test):
        product_page = setup_teardown_test
        actual_products = product_page.get_products_as_dict()
        expected_products = load_data_from_json(".//Testdata//products_data.json")[
            "all_products"
        ]
        self.soft_assert.assert_dict_equals(actual_products, expected_products)
        self.soft_assert.finalize()

    def test_the_desired_values_displayed_on_products_details_page(
        self, setup_teardown_test
    ):
        product = load_data_from_json("./Testdata/products_data.json")["product"]
        product_page = setup_teardown_test
        product_details_page = product_page.click_view_product(product["name"])
        product_detail = product_details_page.get_product_details()
        self.soft_assert.assert_dict_equals(product_detail, product)
        self.soft_assert.finalize()

    @mark.parametrize("search_term, search_results", product_to_search)
    def test_product_search_results(
        self, search_term, search_results, setup_teardown_test
    ):
        product_page = setup_teardown_test
        product_page.search_product(search_term)
        actual_search_results = product_page.get_product_names()
        self.soft_assert.assert_dict_equals(actual_search_results, search_results)
        self.soft_assert.finalize()

    @mark.parametrize(
        "category, sub_category, expected_product_page_header, expected_products",
        load_data_from_json(".//Testdata//products_data.json")["product_categories"],
    )
    def test_product_by_its_category(
        self,
        category,
        sub_category,
        expected_product_page_header,
        expected_products,
        setup_teardown_test,
    ):
        product_page = setup_teardown_test
        product_header = product_page.get_products_page_header()

        self.soft_assert.assert_string_contains(product_header, "ALL PRODUCTS")

        if category not in ["Women", "Men", "Kids"]:
            pytest.fail("Data Error: Invalid category")

        if category == "Women":
            product_page.click_category_women()
            if sub_category == "Dress":
                product_page.click_category_women_dress()
            elif sub_category == "Tops":
                product_page.click_category_women_tops()
            elif sub_category == "Saree":
                product_page.click_category_women_saree()
        elif category == "Men":
            product_page.click_category_men()
            if sub_category == "Jeans":
                product_page.click_category_men_jeans()
            elif sub_category == "Tshirts":
                product_page.click_category_men_tshirts()
        elif category == "Kids":
            product_page.click_category_kids()
            if sub_category == "Dress":
                product_page.click_category_kids_dress()
            elif sub_category == "TopsShirts ":
                product_page.click_category_kids_topsshirts()

        product_header = product_page.get_products_page_header()
        self.soft_assert.assert_string_equals(
            product_header, expected_product_page_header
        )

        products = product_page.get_products_as_dict()
        self.soft_assert.assert_dict_equals(products, expected_products)

        self.soft_assert.finalize()

    @mark.parametrize(
        "brand, expected_product_page_header, expected_products",
        load_data_from_json(".//Testdata//products_data.json")["product_brands"],
    )
    def test_product_by_its_brand(
        self,
        brand,
        expected_product_page_header,
        expected_products,
        setup_teardown_test,
    ):
        product_page = setup_teardown_test
        product_header = product_page.get_products_page_header()

        self.soft_assert.assert_string_contains(product_header, "ALL PRODUCTS")

        if brand not in [
            "Polo",
            "H&M",
            "Madame",
            "Mast & Harbour",
            "Babyhug",
            "Allen Solly Junior",
            "Kookie Kids",
            "Biba",
        ]:
            pytest.fail("Data Error: Invalid category")

        if brand == "Polo":
            product_page.click_polo_brand()
            stock = product_page.get_polo_brand_stock()
        elif brand == "H&M":
            product_page.click_hm_brand()
            stock = product_page.get_hm_brand_stock()
        elif brand == "Madame":
            product_page.click_madame_brand()
            stock = product_page.get_madame_brand_stock()
        elif brand == "Mast & Harbour":
            product_page.click_mast_harbour_brand()
            stock = product_page.get_mast_harbour_brand_stock()
        elif brand == "Babyhug":
            product_page.click_baby_hug_brand()
            stock = product_page.get_baby_hug_brand_stock()
        elif brand == "Allen Solly Junior":
            product_page.click_allen_solly_junior_brand()
            stock = product_page.get_allen_solly_junior_brand_stock()
        elif brand == "Kookie Kids":
            product_page.click_kookie_kids_brand()
            stock = product_page.get_kookie_kids_brand_stock()
        elif brand == "Biba":
            product_page.click_biba_brand()
            stock = product_page.get_biba_brand_stock()

        product_header = product_page.get_products_page_header()
        self.soft_assert.assert_string_equals(
            product_header, expected_product_page_header
        )

        products = product_page.get_products_as_dict()
        self.soft_assert.assert_dict_equals(products, expected_products)

        actual_stock = len(products)
        self.soft_assert.assert_equals(actual_stock, stock)

        self.soft_assert.finalize()
