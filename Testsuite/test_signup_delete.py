from pytest import fixture, mark

from Helpers.common_file_helpers import load_data_from_json
from Pages.login_page import LoginPage
from Utilities.common_utils import get_fake_demographics


@mark.usefixtures("setup_teardown_class")
class TestSignup:

    @fixture(autouse=True)
    def setup_teardown_test(self):
        login_page = LoginPage(self.driver)
        login_page.go_to(self.base_url + "signup")
        yield login_page
        self.driver.delete_all_cookies()

    # Test data for invalid signup testcases
    invalid_signup = load_data_from_json(".\\Testdata\\signup_data.json")["invalid_signup"]
    invalid_signup_test_data = [tuple(data_dict.values()) for data_dict in invalid_signup]

    @mark.parametrize("name, email, response", invalid_signup_test_data)
    def test_invalid_user_signup(self, name, email, response, setup_teardown_test):
        login_page = setup_teardown_test
        login_page.fill_signup_form_and_click_signup_btn(name, email)
        error_msg = login_page.get_invalid_signup_error_text()
        self.soft_assert.assert_equal(error_msg, response, "Invalid signup error - message mismatch.")
        self.soft_assert.finalize()

    def test_valid_user_signup(self, setup_teardown_test):
        test_data = get_fake_demographics()
        login_page = setup_teardown_test
        signup_page = login_page.fill_signup_form_and_click_signup_btn(test_data["name"], test_data["email"])

        home_page_title = signup_page.get_title()
        self.soft_assert.assert_equal(home_page_title, "Automation Exercise - Signup",
                                      f"Expected title 'Automation Exercise - Signup', but got '{home_page_title}'")

        self.soft_assert.assert_equal(signup_page.get_signup_name(), test_data["name"],
                                      f"Expected name '{test_data['name']}', but got '{signup_page.get_signup_name()}'")

        self.soft_assert.assert_equal(signup_page.get_signup_email(), test_data["email"],
                                      f"Expected email '{test_data['email']}', but got '{signup_page.get_signup_email()}'")

        signup_page.fill_signup_form_and_click_continue_btn(test_data)

        self.soft_assert.assert_equal(signup_page.get_account_created_header_text(),
                                      "ACCOUNT CREATED!", "Account created header mismatch.")
        self.soft_assert.assert_equal(signup_page.get_account_created_message_text(),
                                      "Congratulations! Your new account has been successfully created!",
                                      "Account created message mismatch.")
        home_page = signup_page.click_continue_btn()
        self.soft_assert.assert_equal(home_page.get_title(), "Automation Exercise",
                                      "Expected title 'Automation Exercise', but got '{home_page.get_title()}'")
        self.soft_assert.finalize()

    def test_delete_user_account(self, setup_teardown_test):
        test_data = get_fake_demographics()
        login_page = setup_teardown_test
        signup_page = login_page.fill_signup_form_and_click_signup_btn(test_data["name"], test_data["email"])
        signup_page.fill_signup_form_and_click_continue_btn(test_data)
        home_page = signup_page.click_continue_btn()
        home_page.click_delete_account_link()
        self.soft_assert.assert_equal(home_page.get_account_deleted_header_text(), "ACCOUNT DELETED!",
                                      "Account deleted header mismatch.")
        self.soft_assert.assert_in("permanently deleted!", home_page.get_account_deleted_message_text(),
                                   "Account deleted message mismatch.")
        home_page.click_continue_btn_on_delete_account()
        self.soft_assert.assert_equal(home_page.get_title(), "Automation Exercise",
                                      "Expected title 'Automation Exercise', but got '{home_page.get_title()}'")
        self.soft_assert.finalize()
