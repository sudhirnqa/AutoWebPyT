from selenium.common import NoAlertPresentException, NoSuchWindowException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from Pages.base_element import BaseElement
from Utilities.common_utils import custom_logger, allure_attach_screenshot


class BasePage(object):
    """Base class for all page objects."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

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

    def wait_for_element_to_get_disappeared_from_page(self, element):
        log = custom_logger()
        self.wait.until(ec.invisibility_of_element(element))
        log.info(f"Element disappeared: {element}")

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

    def close_other_tabs_and_switch_to_parent_tab(self):
        log = custom_logger()
        try:
            window_count = self.get_windows_count()
            windows = self.driver.window_handles
            if window_count > 1:
                for window in windows[1:]:
                    self.driver.switch_to.window(window)
                    self.driver.close()
                    log.info(f"Switched to tab: {window} and closing it")
                self.driver.switch_to.window(windows[0])
                log.info(f"Switched to tab: {windows[0]}")
            else:
                self.driver.switch_to.window(windows[0])
                log.info(f"No new tab opened...")
        except NoSuchWindowException as e:
            log.error(f"Exception on switching to parent tab: {e}")
        except Exception as e:
            log.error(f"Exception on switching to parent tab: {e}")

    def get_windows_count(self):
        log = custom_logger()
        try:
            self.wait.until(ec.new_window_is_opened(self.driver.current_window_handle))
        except (NoSuchWindowException, Exception) as e:
            log.error(f"No new window opened {e}")
        finally:
            windows = self.driver.window_handles
            log.info(f"Windows count: {len(windows)}")
        return len(windows)
