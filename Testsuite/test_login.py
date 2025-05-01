import pytest

from Helpers.common_file_helpers import load_data_from_json
from Pages.login_page import LoginPage
from Utilities.common_utils import custom_logger

invalid_login = load_data_from_json('.\\Testdata\\login_data.json')['invalid_login']
invalid_login_test_data = [tuple(data_dict.values()) for data_dict in invalid_login]


@pytest.mark.parametrize("email, password, response", invalid_login_test_data)
def test_invalid_login(email, password, response, invoke_browser):
    log = custom_logger()
    driver, base_url = invoke_browser
    login_page = LoginPage(driver)
    login_page.go_to(base_url + "login")
    login_page.fill_login_form_and_click_login_btn(email, password)
    error_msg = login_page.get_invalid_login_error_text()
    try:
        assert response == error_msg, f"Expected: {error_msg}, but got: {response}"
        log.info(f"Expected: {error_msg}, but got: {response}")
    except AssertionError as e:
        print(f"AssertionError: {e}")
        log.error(f"AssertionError: {e}")
        log.error(f"Expected: {error_msg}, but got: {response}")
        raise e
