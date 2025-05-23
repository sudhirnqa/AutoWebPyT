from pytest import fixture, mark

from Helpers.common_file_helpers import load_data_from_json
from Locators import navbar_footer_locators
from Pages.navbar_footer import NavbarFooter


@mark.usefixtures("setup_teardown_class")
class TestCart:
    """Test class for cart functionality."""

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
        nav_footer.wait_for_page_to_load(navbar_footer_locators.subscribe_email_field)
        products_page = nav_footer.click_products_link()
        yield products_page, nav_footer
        self.driver.delete_all_cookies()

    def test_add_product_in_cart(self, setup_teardown_test):
        products_page = setup_teardown_test[0]
        products_page.click_add_to_cart_and_continue_shopping("Blue Top")
        products_page.click_add_to_cart_and_continue_shopping("Blue Top")
        products_page.click_add_to_cart_and_continue_shopping("Men Tshirt")
        cart_page = products_page.click_add_to_cart_and_view_cart("Men Tshirt")
        expected_cart_table_headers = load_data_from_json(
            ".//Testdata//cart_data.json"
        )["table_headers"]
        expected_cart_table_rows = load_data_from_json(".//Testdata//cart_data.json")[
            "table_rows"
        ]
        actual_cart_table_headers = cart_page.get_cart_table_headers()

        self.soft_assert.assert_list_equals(
            actual_cart_table_headers, expected_cart_table_headers
        )

        items_count = cart_page.get_count_of_unique_items_in_cart()
        self.soft_assert.assert_equals(2, items_count)
        actual_cart_table_rows = cart_page.get_cart_table_row_data()

        self.soft_assert.assert_list_equals(
            actual_cart_table_rows, expected_cart_table_rows
        )

        self.soft_assert.finalize()

    def test_remove_product_in_cart(self, setup_teardown_test):
        products_page = setup_teardown_test[0]
        products_page.click_add_to_cart_and_continue_shopping("Blue Top")
        cart_page = products_page.click_add_to_cart_and_view_cart("Men Tshirt")
        count_of_rows = cart_page.get_count_of_unique_items_in_cart()
        self.soft_assert.assert_equals(count_of_rows, 2)

        expected_table_rows_before_delete = load_data_from_json(
            ".//Testdata//cart_data.json"
        )["expected_table_rows_before_delete"]
        actual_table_rows_before_delete = cart_page.get_cart_table_row_data()
        self.soft_assert.assert_list_equals(
            actual_table_rows_before_delete, expected_table_rows_before_delete
        )

        expected_table_rows_after_delete = load_data_from_json(
            ".//Testdata//cart_data.json"
        )["expected_table_rows_after_delete"]
        cart_page.click_cart_item_delete_field_by_product_name("Blue Top")
        actual_table_rows_after_delete = cart_page.get_cart_table_row_data()
        self.soft_assert.assert_list_equals(
            actual_table_rows_after_delete, expected_table_rows_after_delete
        )

        cart_page.click_cart_item_delete_field_by_product_name("Men Tshirt")

        actual_table_rows_after_delete = cart_page.get_cart_table_row_data()
        self.soft_assert.assert_list_equals(actual_table_rows_after_delete, [])

        cart_message = cart_page.get_cart_empty_message()
        self.soft_assert.assert_string_equals(cart_message, "Cart is empty!")

        self.soft_assert.finalize()

    def test_product_quantity_in_cart(self, setup_teardown_test):
        products_page = setup_teardown_test[0]
        product = {"Item": "Blue Top", "Quantity": "5"}
        product_details_page = products_page.click_view_product(product["Item"])
        cart_page = product_details_page.enter_quantity_and_click_add_to_cart(
            product["Quantity"]
        )
        product_row = cart_page.get_cart_table_row_data()[0]

        self.soft_assert.assert_dict_contains(product_row, product)
        self.soft_assert.finalize()

    def test_search_products_and_verify_cart_after_login(self, setup_teardown_test):
        product_page, nav_footer = setup_teardown_test
        product_to_search = self.product_to_search_list[0]
        product_page.search_product(product_to_search["search_term"])

        actual_search_results = product_page.get_product_names()
        self.soft_assert.assert_dict_equals(
            actual_search_results, product_to_search["search_results"]
        )

        for search_result in product_to_search["search_results"]:
            product_page.click_add_to_cart_and_continue_shopping(search_result)
        cart_page = nav_footer.click_cart_link()

        actual_results = [
            list(row_dict.values())[0]
            for row_dict in cart_page.get_cart_table_row_data()
        ]
        self.soft_assert.assert_list_contains(
            actual_results,
            product_to_search["search_results"],
        )

        login_page = nav_footer.click_login_signup_link()
        valid_login_data = load_data_from_json(".\\Testdata\\login_data.json")[
            "valid_login"
        ][0]
        login_page.fill_login_form_and_click_login_btn(
            valid_login_data["username"], valid_login_data["password"]
        )
        cart_page = nav_footer.click_cart_link()
        actual_results = [
            list(row_dict.values())[0]
            for row_dict in cart_page.get_cart_table_row_data()
        ]

        self.soft_assert.assert_list_contains(
            actual_results,
            product_to_search["search_results"],
        )

        self.soft_assert.finalize()
