from pytest import fixture, mark

from Pages.login_page import LoginPage
from Utilities.common_utils import data_faker


@mark.usefixtures("setup_teardown_class")
class TestListOfCases:
    """Test class for login functionality."""

    @fixture(autouse=True)
    def setup_teardown_test(self):
        login_page = LoginPage(self.driver)
        test_cases_page = login_page.click_test_cases_link()
        yield test_cases_page
        self.driver.delete_all_cookies()

    def test_the_list_of_test_cases_visible(self, setup_teardown_test):
        test_cases_page = setup_teardown_test
        list_header = test_cases_page.get_test_case_label_text()

        self.soft_assert.assert_equal(list_header,
                                      "Below is the list of test Cases for you to practice the Automation. "
                                      "Click on the scenario for detailed Test Steps:Automation software",
                                      f"Expected testcases label is: "
                                      f"'Below is the list of test Cases for you to practice the Automation. "
                                      f"Click on the scenario for detailed Test Steps:Automation software', "
                                      f"but got: '{list_header}'")

        count_of_cases = len(test_cases_page.get_test_cases_links_text())
        self.soft_assert.assert_equal(count_of_cases, 26,
                                      f"Expected count of cases: '26', but got: '{count_of_cases}'")

        self.soft_assert.finalize()
