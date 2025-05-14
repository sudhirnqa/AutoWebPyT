from pytest import fixture, mark

from Helpers.common_file_helpers import load_data_from_json
from Locators import navbar_footer_locators, cart_page_locators, payment_page_locators
from Pages.home_page import HomePage
from Pages.navbar_footer import NavbarFooter
from Utilities.common_utils import data_faker


@mark.usefixtures("setup_teardown_class")
class TestOrders:
    """Test class for order functionality."""

    @fixture(autouse=True)
    def setup_teardown_test(self):
        nav_footer = NavbarFooter(self.driver)
        nav_footer.wait_for_page_to_load(navbar_footer_locators.logo_img)
        test_data = data_faker()
        yield nav_footer, test_data
        self.driver.delete_all_cookies()

    def test_place_order_register_while_checkout(self, setup_teardown_test):
        nav_footer, test_data = setup_teardown_test

        cart_page = self.add_products_to_and_navigate_to_cart(nav_footer)
        cart_page.click_proceed_to_checkout_link()

        login_page = cart_page.click_register_login_link()

        signup_page = login_page.fill_signup_form_and_click_signup_btn(
            test_data["name"], test_data["email"]
        )
        signup_page.fill_signup_form_and_click_continue_btn(test_data)
        signup_page.click_continue_btn()

        nav_footer.click_cart_link()
        self.navigate_to_and_validate_the_checkout_page_then_place_the_order_and_delete_the_test_account(
            nav_footer, cart_page, test_data
        )

    def test_place_order_register_before_checkout(self, setup_teardown_test):
        nav_footer, test_data = setup_teardown_test

        login_page = nav_footer.click_login_signup_link()

        signup_page = login_page.fill_signup_form_and_click_signup_btn(
            test_data["name"], test_data["email"]
        )
        signup_page.fill_signup_form_and_click_continue_btn(test_data)
        signup_page.click_continue_btn()

        cart_page = self.add_products_to_and_navigate_to_cart(nav_footer)

        self.navigate_to_and_validate_the_checkout_page_then_place_the_order_and_delete_the_test_account(
            nav_footer, cart_page, test_data
        )

    def test_place_order_login_before_checkout(self, setup_teardown_test):
        nav_footer, test_data = setup_teardown_test

        login_page = nav_footer.click_login_signup_link()
        valid_login_data = load_data_from_json(".\\Testdata\\login_data.json")[
            "valid_login"
        ][0]
        login_page.fill_login_form_and_click_login_btn(
            valid_login_data["username"], valid_login_data["password"]
        )

        cart_page = self.add_products_to_and_navigate_to_cart(nav_footer)
        checkout_page = cart_page.click_proceed_to_checkout_link()

        expected_details = [
            ". firstname lastname",
            "CC",
            "Address1",
            "Addres2",
            "Bengaluru Karnataka 560001",
            "India",
            "+919876543210",
        ]
        self.validate_checkout_page_details_and_place_the_order(
            checkout_page, expected_details, test_data
        )

        nav_footer.click_sign_out_link()
        self.soft_assert.finalize()

    def add_products_to_and_navigate_to_cart(self, nav_footer):
        products_page = nav_footer.click_products_link()
        products_page.click_add_to_cart_and_continue_shopping("Blue Top")
        products_page.click_add_to_cart_and_continue_shopping("Blue Top")
        products_page.click_add_to_cart_and_continue_shopping("Men Tshirt")
        products_page.click_add_to_cart_and_continue_shopping("Men Tshirt")
        cart_page = nav_footer.click_cart_link()
        cart_page.wait_for_page_to_load(cart_page_locators.cart_page_header)
        return cart_page

    def navigate_to_and_validate_the_checkout_page_then_place_the_order_and_delete_the_test_account(
        self, nav_footer, cart_page, test_data
    ):
        checkout_page = cart_page.click_proceed_to_checkout_link()
        expected_details = [
            f"Mr. {test_data['first_name']} {test_data['last_name']}",
            test_data["company"],
            test_data["address_1"].split("\n")[0],
            test_data["address_2"].split("\n")[0],
            f"{test_data['address_2'].split('\n')[1]}{test_data['city']} {test_data['address_1'].split('\n')[1]}{test_data['state']} {test_data['zipcode']}",
            "India",
            test_data["phone_number"],
        ]

        self.validate_checkout_page_details_and_place_the_order(
            checkout_page, expected_details, test_data
        )
        nav_footer.click_delete_account_link()
        home_page = HomePage(self.driver)
        account_delete_confirmation = home_page.get_account_deleted_message_text()
        self.soft_assert.assert_string_equals(
            "Your account has been permanently deleted!", account_delete_confirmation
        )
        self.soft_assert.finalize()

    def validate_checkout_page_details_and_place_the_order(
        self, checkout_page, expected_details, test_data
    ):
        actual_billing_details = checkout_page.get_billing_address_details()
        self.soft_assert.assert_list_equals(actual_billing_details, expected_details)
        actual_delivery_details = checkout_page.get_delivery_address_details()
        self.soft_assert.assert_list_equals(actual_delivery_details, expected_details)

        products, actual_total_price = checkout_page.get_checkout_table_row_data()
        total_price = 0
        for product in products:
            self.soft_assert.assert_equals(
                product["Price"] * product["Quantity"], product["Total"]
            )
            total_price += product["Total"]

        self.soft_assert.assert_equals(actual_total_price, total_price)

        payment_page = checkout_page.enter_comment_and_click_place_order_btn(
            comment=test_data["text"]
        )
        payment_page.fill_payment_form_and_click_pay_and_confirm_order_btn(
            f"{test_data['first_name']} {test_data['last_name']}",
            test_data["credit_card_number"],
            "123",
            "12",
            "2025",
        )
        payment_page.wait_for_page_to_load(
            payment_page_locators.order_confirmation_header
        )
