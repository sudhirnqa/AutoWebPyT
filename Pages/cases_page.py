from Locators import case_page_locators
from Pages.base_element import BaseElement
from Pages.base_page import BasePage


class TestCasesPage(BasePage):

    @property
    def test_case_label(self):
        return BaseElement(self.driver, case_page_locators.test_case_label)

    def get_test_case_label_text(self):
        return self.test_case_label.text

    @property
    def test_cases_links_to_toggle(self):
        return BaseElement(self.driver, case_page_locators.test_cases_links_to_toggle)

    def get_test_cases_links_text(self):
        return self.test_cases_links_to_toggle.elements_text()
