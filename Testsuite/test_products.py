from pytest import fixture, mark

from Helpers.common_file_helpers import load_data_from_json
from Pages.login_page import LoginPage


@mark.usefixtures("setup_teardown_class")
class TestProducts:
    """Test class for login functionality."""

    # Parameterize testdata
    product_to_search_list = load_data_from_json("./Testdata/products_data.json")["product_to_search"]
    product_to_search = [tuple(product_dict.values()) for product_dict in product_to_search_list]

    @fixture(autouse=True)
    def setup_teardown_test(self):
        login_page = LoginPage(self.driver)
        product_page = login_page.click_products_link()
        yield product_page
        self.driver.delete_all_cookies()

    def test_product_listing(self, setup_teardown_test):
        product_page = setup_teardown_test
        actual_products = product_page.get_products_as_dict()
        expected_products = load_data_from_json("./Testdata/products_data.json")["all_products"]
        self.soft_assert.assert_equal(actual_products, expected_products)
        self.soft_assert.finalize()

    def test_the_desired_values_displayed_on_products_details_page(self, setup_teardown_test):
        product = load_data_from_json("./Testdata/products_data.json")["product"]
        product_page = setup_teardown_test
        product_details_page = product_page.click_view_product(product["name"])
        product_detail = product_details_page.get_product_details()
        self.soft_assert.assert_equal(product_detail, product)
        self.soft_assert.finalize()

    @mark.parametrize("search_term, search_result", product_to_search)
    def test_product_search_results(self, search_term, search_result, setup_teardown_test):
        product_page = setup_teardown_test
        product_page.search_product(search_term)
        actual_search_result = product_page.get_product_names()
        self.soft_assert.assert_equal(actual_search_result, search_result)
        self.soft_assert.finalize()
