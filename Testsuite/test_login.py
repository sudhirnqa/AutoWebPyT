from pytest import mark

from Helpers.common_file_helpers import load_data_from_json
from Pages.login_page import LoginPage

invalid_login = load_data_from_json('.\\Testdata\\login_data.json')['invalid_login']
invalid_login_test_data = [tuple(data_dict.values()) for data_dict in invalid_login]
valid_login = load_data_from_json('.\\Testdata\\login_data.json')['valid_login']
valid_login_test_data = [tuple(data_dict.values()) for data_dict in valid_login]


@mark.usefixtures("setup_teardown_class")
class TestLogin:
    @mark.parametrize("email, password, response", invalid_login_test_data)
    def test_invalid_login(self, email, password, response, invoke_browser):
        # driver, base_url = invoke_browser
        login_page = LoginPage(self.driver)
        login_page.go_to(self.base_url + "login")
        login_page.fill_login_form_and_click_login_btn(email, password)
        error_msg = login_page.get_invalid_login_error_text()
        self.soft_assert.assert_equal(error_msg, response, "Invalid login error message mismatch.")
        self.soft_assert.finalize()

    @mark.parametrize("email, password", valid_login_test_data)
    def test_valid_login(self, email, password):
        login_page = LoginPage(self.driver)
        login_page.go_to(self.base_url + "login")
        home_page = login_page.fill_login_form_and_click_login_btn(email, password)
        home_page_title = home_page.get_title()
        self.soft_assert.assert_equal(home_page_title, "Automation Exercise",
                                      f"Expected title 'Automation Exercise', but got '{home_page_title}'")
        self.soft_assert.finalize()
