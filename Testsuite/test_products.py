from pytest import fixture, mark

from Helpers.common_file_helpers import load_data_from_json
from Pages.login_page import LoginPage


@mark.usefixtures("setup_teardown_class")
class TestProducts:
    """Test class for login functionality."""

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
