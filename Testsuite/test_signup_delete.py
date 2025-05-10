from pytest import fixture, mark

from Helpers.common_file_helpers import load_data_from_json
from Pages.login_page import LoginPage
from Pages.navbar_footer import NavbarFooter
from Utilities.common_utils import data_faker


@mark.usefixtures("setup_teardown_class")
class TestSignup:
    # Parameterize Testdata
    # Test data for invalid signup testcases
    invalid_signup = load_data_from_json(".\\Testdata\\signup_data.json")[
        "invalid_signup"
    ]
    invalid_signup_test_data = [
        tuple(data_dict.values()) for data_dict in invalid_signup
    ]

    @fixture(autouse=True)
    def setup_teardown_test(self):
        login_page = LoginPage(self.driver)
        login_page.go_to(self.base_url + "signup")
        test_data = data_faker()
        yield login_page, test_data
        self.driver.delete_all_cookies()

    @mark.parametrize("name, email, response", invalid_signup_test_data)
    def test_invalid_user_signup(self, name, email, response, setup_teardown_test):
        login_page = setup_teardown_test[0]
        login_page.fill_signup_form_and_click_signup_btn(name, email)
        error_msg = login_page.get_invalid_signup_error_text()
        self.soft_assert.assert_string_equals(
            error_msg, response, "Invalid signup error - message mismatch."
        )
        self.soft_assert.finalize()

    def test_valid_user_signup(self, setup_teardown_test):
        login_page, test_data = setup_teardown_test
        signup_page = login_page.fill_signup_form_and_click_signup_btn(
            test_data["name"], test_data["email"]
        )

        sihnup_page_title = signup_page.get_title
        self.soft_assert.assert_string_equals(
            sihnup_page_title,
            "Automation Exercise - Signup",
            f"Expected title 'Automation Exercise - Signup', but got '{sihnup_page_title}'",
        )

        self.soft_assert.assert_string_equals(
            signup_page.get_signup_name(),
            test_data["name"],
            f"Expected name '{test_data['name']}', but got '{signup_page.get_signup_name()}'",
        )

        self.soft_assert.assert_string_equals(
            signup_page.get_signup_email(),
            test_data["email"],
            f"Expected email '{test_data['email']}', but got '{signup_page.get_signup_email()}'",
        )

        signup_page.fill_signup_form_and_click_continue_btn(test_data)

        self.soft_assert.assert_string_equals(
            signup_page.get_account_created_header_text(),
            "ACCOUNT CREATED!",
            "Account created header mismatch.",
        )
        self.soft_assert.assert_string_equals(
            signup_page.get_account_created_message_text(),
            "Congratulations! Your new account has been successfully created!",
            "Account created message mismatch.",
        )
        home_page = signup_page.click_continue_btn()
        self.soft_assert.assert_string_equals(
            home_page.get_title,
            "Automation Exercise",
            f"Expected title 'Automation Exercise', but got '{home_page.get_title}'",
        )
        self.soft_assert.finalize()

    def test_delete_user_account(self, setup_teardown_test):
        login_page, test_data = setup_teardown_test
        signup_page = login_page.fill_signup_form_and_click_signup_btn(
            test_data["name"], test_data["email"]
        )
        signup_page.fill_signup_form_and_click_continue_btn(test_data)
        home_page = signup_page.click_continue_btn()
        nav_footer = NavbarFooter(self.driver)
        nav_footer.click_delete_account_link()
        self.soft_assert.assert_string_equals(
            home_page.get_account_deleted_header_text(),
            "ACCOUNT DELETED!",
            "Account deleted header mismatch.",
        )
        self.soft_assert.assert_string_contains(
            home_page.get_account_deleted_message_text(),
            "permanently deleted!",
            "Account deleted message mismatch.",
        )
        home_page.click_continue_btn_on_delete_account()
        self.soft_assert.assert_string_equals(
            home_page.get_title,
            "Automation Exercise",
            f"Expected title 'Automation Exercise', but got '{home_page.get_title}'",
        )
        self.soft_assert.finalize()
