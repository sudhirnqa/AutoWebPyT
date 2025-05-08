from Locators import home_page_locators, navbar_footer_locators
from Pages.base_element import BaseElement
from Pages.base_page import BasePage


class HomePage(BasePage):

    @property
    def account_deleted_header(self):
        return BaseElement(self.driver, home_page_locators.account_deleted_header)

    def get_account_deleted_header_text(self):
        return self.account_deleted_header.text

    @property
    def account_deleted_message(self):
        return BaseElement(self.driver, home_page_locators.account_deleted_message)

    def get_account_deleted_message_text(self):
        return self.account_deleted_message.text

    @property
    def continue_btn_on_delete_account(self):
        return BaseElement(self.driver, home_page_locators.continue_btn)

    def click_continue_btn_on_delete_account(self):
        self.continue_btn_on_delete_account.click()
        self.wait_for_page_to_load(navbar_footer_locators.logo_img)
