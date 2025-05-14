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

    @mark.parametrize("search_term, search_result", product_to_search)
    def test_product_search_results(
        self, search_term, search_result, setup_teardown_test
    ):
        product_page = setup_teardown_test
        product_page.search_product(search_term)
        actual_search_result = product_page.get_product_names()
        self.soft_assert.assert_dict_equals(actual_search_result, search_result)
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
