from pytest import fixture, mark

from Helpers.common_file_helpers import load_data_from_json
from Pages.login_page import LoginPage


@mark.usefixtures("setup_teardown_class")
class TestLogin:
    """Test class for login functionality."""

    @fixture(autouse=True)
    def setup_teardown_test(self):
        login_page = LoginPage(self.driver)
        login_page.go_to(self.base_url + "login")
        yield login_page
        self.driver.delete_all_cookies()

    # Test data for invalid login testcases
    invalid_login = load_data_from_json('.\\Testdata\\login_data.json')['invalid_login']
    invalid_login_test_data = [tuple(data_dict.values()) for data_dict in invalid_login]

    # Test data for valid login testcases
    valid_login = load_data_from_json('.\\Testdata\\login_data.json')['valid_login']
    valid_login_test_data = [tuple(data_dict.values()) for data_dict in valid_login]

    @mark.xfail(reason="This test is expected to fail for one of the invalid login cases.")
    @mark.parametrize("email, password, response", invalid_login_test_data)
    def test_invalid_user_login(self, email, password, response, setup_teardown_test):
        login_page = setup_teardown_test
        login_page.fill_login_form_and_click_login_btn(email, password)
        error_msg = login_page.get_invalid_login_error_text()
        self.soft_assert.assert_equal(error_msg, response, "Invalid login error message mismatch.")
        self.soft_assert.finalize()

    @mark.parametrize("email, password", valid_login_test_data)
    def test_valid_user_login(self, email, password, setup_teardown_test):
        login_page = setup_teardown_test
        home_page = login_page.fill_login_form_and_click_login_btn(email, password)
        home_page_title = home_page.get_title()
        self.soft_assert.assert_equal(home_page_title, "Automation Exercise",
                                      f"Expected title 'Automation Exercise', but got '{home_page_title}'")
        self.soft_assert.finalize()

    @mark.parametrize("email, password", valid_login_test_data)
    def test_user_logout(self, email, password, setup_teardown_test):
        login_page = setup_teardown_test
        home_page = login_page.fill_login_form_and_click_login_btn(email, password)
        home_page.click_sign_out_link()
        login_page_title = login_page.get_title()
        self.soft_assert.assert_equal(login_page_title, "Automation Exercise - Signup / Login",
                                      f"Expected title 'Automation Exercise - Signup / Login', but got '{login_page_title}'")
        current_url = login_page.get_current_url()
        self.soft_assert.assert_in("login", current_url, f"Expected URL contains 'login', but got '{current_url}'")
        self.soft_assert.finalize()
