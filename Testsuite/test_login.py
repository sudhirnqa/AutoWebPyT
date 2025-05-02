import pytest

from Helpers.common_file_helpers import load_data_from_json
from Pages.login_page import LoginPage
from Utilities.custom_assert import CustomAssert

invalid_login = load_data_from_json('.\\Testdata\\login_data.json')['invalid_login']
invalid_login_test_data = [tuple(data_dict.values()) for data_dict in invalid_login]


class TestLogin:
    @pytest.mark.parametrize("email, password, response", invalid_login_test_data)
    def test_invalid_login(self, email, password, response, invoke_browser):
        driver, base_url = invoke_browser
        soft_assert = CustomAssert(driver)
        login_page = LoginPage(driver)
        login_page.go_to(base_url + "login")
        login_page.fill_login_form_and_click_login_btn(email, password)
        error_msg = login_page.get_invalid_login_error_text()
        soft_assert.assert_equal(error_msg, response, "Invalid login error message mismatch.")
        soft_assert.finalize()
