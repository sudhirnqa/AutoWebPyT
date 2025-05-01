from Pages.base_element import BaseElement
from Utilities.common_utils import custom_logger


class BasePage(object):
    """Base class for all page objects."""

    def __init__(self, driver):
        self.driver = driver

    def go_to(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

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
