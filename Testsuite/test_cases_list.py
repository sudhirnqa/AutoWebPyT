from pytest import fixture, mark

from Pages.navbar_footer import NavbarFooter


@mark.usefixtures("setup_teardown_class")
class TestListOfCases:
    """Test class for login functionality."""

    @fixture(autouse=True)
    def setup_teardown_test(self):
        nav_footer = NavbarFooter(self.driver)
        test_cases_page = nav_footer.click_test_cases_link()
        yield test_cases_page
        self.driver.delete_all_cookies()

    def test_the_list_of_test_cases_visible(self, setup_teardown_test):
        test_cases_page = setup_teardown_test
        list_header = test_cases_page.get_test_case_label_text()

        self.soft_assert.assert_string_contains(
            list_header,
            "Below is the list of test Cases for you to practice the Automation.",
            f"Expected testcases label contains: "
            f"'Below is the list of test Cases for you to practice the Automation.'"
            f", but got: '{list_header}'",
        )

        count_of_cases = len(test_cases_page.get_test_cases_links_text())
        self.soft_assert.assert_equals(
            count_of_cases,
            26,
            f"Expected count of cases: '26', but got: '{count_of_cases}'",
        )

        self.soft_assert.finalize()
