from time import sleep

from Helpers.common_file_helpers import get_absolute_file_path
from Locators import contactus_page_locators
from Pages.base_element import BaseElement
from Pages.base_page import BasePage


class ContactusPage(BasePage):
    def wait_for_contactus_page_to_load(self):
        self.wait_for_page_to_load(contactus_page_locators.contactus_page_header)

    @property
    def contactus_page_header(self):
        return BaseElement(self.driver, contactus_page_locators.contactus_page_header)

    def get_contactus_page_header_text(self):
        return self.contactus_page_header.text

    @property
    def contactus_form_header(self):
        return BaseElement(self.driver, contactus_page_locators.contactus_form_header)

    def get_contactus_form_header(self):
        return self.contactus_form_header.text

    @property
    def contactus_name_field(self):
        return BaseElement(self.driver, contactus_page_locators.contactus_name_field)

    def enter_contactus_name_field(self, text):
        self.contactus_name_field.enter_text(text)

    @property
    def contactus_email_field(self):
        return BaseElement(self.driver, contactus_page_locators.contactus_email_field)

    def enter_contactus_email_field(self, email):
        self.contactus_email_field.enter_text(email)

    @property
    def contactus_subject_field(self):
        return BaseElement(self.driver, contactus_page_locators.contactus_subject_field)

    def enter_contactus_subject_field(self, subject):
        self.contactus_subject_field.enter_text(subject)

    @property
    def contactus_message_field(self):
        return BaseElement(self.driver, contactus_page_locators.contactus_message_field)

    def enter_contactus_message_field(self, text):
        self.contactus_message_field.enter_text(text)

    @property
    def contactus_file_upload(self):
        return BaseElement(self.driver, contactus_page_locators.contactus_file_upload)

    def enter_contactus_file_path_to_upload(self, relative_file_path):
        file = get_absolute_file_path(relative_file_path)
        self.contactus_file_upload.enter_text(file)

    @property
    def contactus_submit_btn(self):
        return BaseElement(self.driver, contactus_page_locators.contactus_submit_btn)

    def click_contactus_submit_btn(self):
        self.contactus_submit_btn.click()

    def get_contactus_page_alert_text(self):
        return self.get_alert_text()

    def accept_contactus_page_alert(self):
        self.accept_alert()

    def dismiss_contactus_page_alert(self):
        self.dismiss_alert()

    def fill_contactus_form_and_click_submit(self, test_data, file_to_upload=None):
        if isinstance(test_data, dict):
            self.enter_contactus_name_field(test_data['name'])
            self.enter_contactus_email_field(test_data['email'])
            self.enter_contactus_subject_field(test_data['text'])
            self.enter_contactus_message_field('\n'.join(test_data['texts']))
            if file_to_upload:
                self.enter_contactus_file_path_to_upload(file_to_upload)
            self.click_contactus_submit_btn()
        else:
            raise ValueError(
                "The test_data argument must be a dictionary with the following keys: name, email, subject, message"
            )

    @property
    def contactus_success_message(self):
        return BaseElement(self.driver, contactus_page_locators.contactus_success_message)

    def get_contactus_success_message_text(self):
        return self.contactus_success_message.text
