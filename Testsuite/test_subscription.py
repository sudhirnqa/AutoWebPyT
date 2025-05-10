from pytest import fixture, mark

from Locators import navbar_footer_locators
from Pages.navbar_footer import NavbarFooter
from Utilities.common_utils import data_faker


@mark.usefixtures("setup_teardown_class")
class TestProducts:
    """Test class for subscription functionality."""

    @fixture(autouse=True)
    def setup_teardown_test(self):
        nav_footer = NavbarFooter(self.driver)
        nav_footer.wait_for_page_to_load(navbar_footer_locators.subscribe_email_field)
        test_data = data_faker()
        yield nav_footer, test_data
        self.driver.delete_all_cookies()

    def test_subscription_on_home_page(self, setup_teardown_test):
        nav_footer, test_data = setup_teardown_test
        nav_footer.click_home_page_link()
        self.validate_the_subscription_success_message(nav_footer, test_data)

    def test_subscription_on_cart_page(self, setup_teardown_test):
        nav_footer, test_data = setup_teardown_test
        nav_footer.click_cart_link()
        self.validate_the_subscription_success_message(nav_footer, test_data)

    def validate_the_subscription_success_message(self, nav_footer, test_data):
        success_msg = nav_footer.fill_subscription_email_and_click_subscription_btn(
            test_data["email"]
        )
        self.soft_assert.assert_is_instance(
            success_msg,
            str,
            message=f"Expected success message type to be string, but got {type(success_msg)}",
        )
        self.soft_assert.assert_string_equals(
            success_msg,
            "You have been successfully subscribed!",
            message=f"Expected success message should be 'You have been successfully subscribed!', but got{success_msg}",
        )
        success_msg_displayed = nav_footer.is_subscribe_success_message_disappeared()
        self.soft_assert.assert_true(
            success_msg_displayed,
            message="Success message displayed, but it should not be displayed",
        )
        self.soft_assert.finalize()
