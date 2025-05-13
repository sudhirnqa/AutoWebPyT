from Locators import payment_page_locators
from Pages.base_element import BaseElement
from Pages.base_page import BasePage


class PaymentPage(BasePage):
    @property
    def name_on_card_field(self):
        return BaseElement(self.driver, payment_page_locators.name_on_card_field)

    def enter_name_on_card_field(self, name):
        self.name_on_card_field.enter_text(name)

    @property
    def card_number_field(self):
        return BaseElement(self.driver, payment_page_locators.card_number_field)

    def enter_card_number_field(self, card_number):
        self.card_number_field.enter_text(card_number)

    @property
    def card_cvc_field(self):
        return BaseElement(self.driver, payment_page_locators.card_cvc_field)

    def enter_card_cvc_field(self, cvc):
        self.card_cvc_field.enter_text(cvc)

    @property
    def expiry_month_field(self):
        return BaseElement(self.driver, payment_page_locators.expiry_month_field)

    def enter_expiry_month_field(self, mm):
        self.expiry_month_field.enter_text(mm)

    @property
    def expiry_year_field(self):
        return BaseElement(self.driver, payment_page_locators.expiry_year_field)

    def enter_expiry_year_field(self, yyyy):
        self.expiry_year_field.enter_text(yyyy)

    @property
    def pay_and_confirm_order_btn(self):
        return BaseElement(self.driver, payment_page_locators.pay_and_confirm_order_btn)

    def click_pay_and_confirm_order_btn(self):
        self.pay_and_confirm_order_btn.click()

    def fill_payment_form_and_click_pay_and_confirm_order_btn(
        self, name, card_number, cvc, mm, yyyy
    ):
        self.enter_name_on_card_field(name)
        self.enter_card_number_field(card_number)
        self.enter_card_cvc_field(cvc)
        self.enter_expiry_month_field(mm)
        self.enter_expiry_year_field(yyyy)
        self.click_pay_and_confirm_order_btn()
