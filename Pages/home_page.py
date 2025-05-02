from Locators import home_page_locators, login_page_locators
from Pages.base_element import BaseElement
from Pages.base_page import BasePage


class HomePage(BasePage):

    @property
    def account_owner_name(self):
        return BaseElement(self.driver, home_page_locators.account_owner)

    def get_account_owner_name(self):
        return self.account_owner_name.text

    @property
    def delete_account_link(self):
        return BaseElement(self.driver, home_page_locators.delete_account_link)

    def click_delete_account_link(self):
        self.delete_account_link.click()
        self.wait_for_page_to_load(home_page_locators.account_deleted_header)

    @property
    def sign_out_link(self):
        return BaseElement(self.driver, home_page_locators.sign_out_link)

    def click_sign_out_link(self):
        self.sign_out_link.click()
        self.wait_for_page_to_load(login_page_locators.login_form_header)

    def is_log_out_displayed(self):
        return self.sign_out_link.is_element_displayed()

    @property
    def account_deleted_header(self):
        return BaseElement(self.driver, home_page_locators.account_deleted_header)

    def get_account_deleted_header_text(self):
        return self.account_deleted_header.text

    @property
    def continue_btn_on_delete_account(self):
        return BaseElement(self.driver, home_page_locators.continue_btn)

    def click_continue_btn_on_delete_account(self):
        self.continue_btn_on_delete_account.click()
        self.wait_for_page_to_load(login_page_locators.logo_img)
