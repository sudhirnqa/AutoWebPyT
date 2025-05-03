from selenium.common import NoAlertPresentException

from Pages.base_element import BaseElement
from Utilities.common_utils import custom_logger, allure_attach_screenshot


class BasePage(object):
    """Base class for all page objects."""

    def __init__(self, driver):
        self.driver = driver

    def go_to(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    @property
    def get_title(self):
        return self.driver.title

    def refresh_page(self):
        self.driver.refresh()

    def wait_for_page_to_load(self, locator):
        """Wait for a specific element to be present on the page."""
        log = custom_logger()
        element = BaseElement(self.driver, locator)
        log.info(f"Page loaded and found the element with the locator: {locator}")
        return element

    def accept_alert(self):
        log = custom_logger()
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
            log.info(f"Alert accepted: {alert.text}")
        except NoAlertPresentException as e:
            print(f"Alert not found: {e}")
            log.error(f"Alert not found: {e}")
            allure_attach_screenshot(self.driver)
        except Exception as e:
            print(f"Unexpected error accepting alert: {e}")
            log.error(f"Unexpected error accepting alert: {e}")
            allure_attach_screenshot(self.driver)

    def dismiss_alert(self):
        log = custom_logger()
        try:
            alert = self.driver.switch_to.alert
            alert.dismiss()
            log.info(f"Alert dismissed: {alert.text}")
        except NoAlertPresentException as e:
            print(f"Alert not found: {e}")
            log.error(f"Alert not found: {e}")
            allure_attach_screenshot(self.driver)
        except Exception as e:
            print(f"Unexpected error dismissing alert: {e}")
            log.error(f"Unexpected error dismissing alert: {e}")
            allure_attach_screenshot(self.driver)

    def get_alert_text(self):
        log = custom_logger()
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            log.info(f"Alert text: {alert_text}")
            return alert_text
        except NoAlertPresentException as e:
            print(f"Alert not found: {e}")
            log.error(f"Alert not found: {e}")
            allure_attach_screenshot(self.driver)
            return None
        except Exception as e:
            print(f"Unexpected error getting alert text: {e}")
            log.error(f"Unexpected error getting alert text: {e}")
            allure_attach_screenshot(self.driver)
            return None

    def enter_text_in_alert(self, text):
        log = custom_logger()
        try:
            alert = self.driver.switch_to.alert
            alert.send_keys(text)
            log.info(f"Text entered in alert: {text}")
        except NoAlertPresentException as e:
            print(f"Alert not found: {e}")
            log.error(f"Alert not found: {e}")
            allure_attach_screenshot(self.driver)
        except Exception as e:
            print(f"Unexpected error entering text in alert: {e}")
            log.error(f"Unexpected error entering text in alert: {e}")
            allure_attach_screenshot(self.driver)