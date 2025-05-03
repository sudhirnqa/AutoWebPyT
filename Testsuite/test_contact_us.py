from pytest import fixture, mark

from Pages.contactus_page import ContactusPage
from Utilities.common_utils import data_faker


@mark.usefixtures("setup_teardown_class")
class TestContactUS:
    """Test class for login functionality."""

    @fixture(autouse=True)
    def setup_teardown_test(self):
        contactus_page = ContactusPage(self.driver)
        contactus_page.go_to(self.base_url + "contact_us")
        contactus_page.wait_for_contactus_page_to_load()
        test_data = data_faker()
        yield contactus_page, test_data
        self.driver.delete_all_cookies()

    def test_the_contact_us_form_submit_success_message(self, setup_teardown_test):
        contactus_page, test_data = setup_teardown_test
        page_header = contactus_page.get_contactus_page_header_text()
        form_header = contactus_page.get_contactus_form_header()
        self.soft_assert.assert_equal(page_header, "CONTACT US",
                                      f"Expected page header is: 'Contact Us', but got: '{page_header}'")
        self.soft_assert.assert_equal(form_header, "GET IN TOUCH",
                                      f"Expected form header is: 'Get In Touch', but got: '{form_header}'")

        contactus_page.fill_contactus_form_and_click_submit(test_data,
                                                            file_to_upload='.\\Testdata\\dummy_file_to_upload')
        alert_text = contactus_page.get_alert_text()
        self.soft_assert.assert_equal(alert_text, "Press OK to proceed!",
                                      f"Expected success message is: 'Press OK to proceed!', but got: '{alert_text}'")
        contactus_page.accept_alert()
        success_msg = contactus_page.get_contactus_success_message_text()
        self.soft_assert.assert_equal(success_msg, "Success! Your details have been submitted successfully.",
                                      f"Expected success message is: 'Success! Your details have been submitted successfully.', but got: '{success_msg}'")

        self.soft_assert.finalize()
