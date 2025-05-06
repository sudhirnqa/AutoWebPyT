from selenium.common import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException, \
    ElementNotVisibleException, InvalidSelectorException, StaleElementReferenceException, NoSuchAttributeException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

from Utilities.common_utils import custom_logger, allure_attach_screenshot


class BaseElement(object):

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)
        self.element = None
        self.find_element()
        self.elements = None
        self.find_elements()

    def find_element(self):
        log = custom_logger()
        try:
            self.element = self.wait.until(ec.presence_of_element_located(self.locator))
            log.info(f"Element found: {self.locator}")
        except (ElementClickInterceptedException, ElementNotInteractableException, ElementNotVisibleException,
                InvalidSelectorException, StaleElementReferenceException,) as e:
            print(f"Error finding element: {self.locator} - {e}")
            log.error(f"Error finding element: {self.locator} - {e}")
            allure_attach_screenshot(self.driver)
        except Exception as e:
            print(f"Unexpected error finding element: {self.locator} - {e}")
            log.error(f"Unexpected error finding element: {self.locator} - {e}")
            allure_attach_screenshot(self.driver)

    def find_elements(self):
        log = custom_logger()
        try:
            self.elements = self.wait.until(ec.presence_of_all_elements_located(self.locator))
            log.info(f"Elements found: {self.locator}")
        except StaleElementReferenceException as e:
            print(f"Error finding element: {self.locator} - {e}")
            log.error(f"Error finding element: {self.locator} - {e}")
            allure_attach_screenshot(self.driver)
        except Exception as e:
            print(f"Unexpected error finding element: {self.locator} - {e}")
            log.error(f"Unexpected error finding element: {self.locator} - {e}")
            allure_attach_screenshot(self.driver)

    def click(self):
        log = custom_logger()
        try:
            self.scroll_to_element()
            self.wait.until(ec.element_to_be_clickable(self.locator)).click()
            log.info(f"Element clicked: {self.locator}")
        except (ElementClickInterceptedException, ElementNotInteractableException, ElementNotVisibleException,
                InvalidSelectorException, StaleElementReferenceException,) as e:
            print(f"Error clicking element: {self.locator} - {e}")
            log.error(f"Error clicking element: {self.locator} - {e}")
            allure_attach_screenshot(self.driver)
        except Exception as e:
            print(f"Unexpected error clicking element: {self.locator} - {e}")
            log.error(f"Unexpected error clicking element: {self.locator} - {e}")
            allure_attach_screenshot(self.driver)

    def enter_text(self, text):
        log = custom_logger()
        try:
            self.scroll_to_element()
            self.element.send_keys(text)
            log.info(f"Text entered: '{text}' in {self.locator}")
        except (ElementClickInterceptedException, ElementNotInteractableException, ElementNotVisibleException,
                InvalidSelectorException, StaleElementReferenceException,) as e:
            print(f"Error entering text in element: {self.locator} - {e}")
            log.error(f"Error entering text in element: {self.locator} - {e}")
            allure_attach_screenshot(self.driver)
        except Exception as e:
            print(f"Unexpected error entering text in element: {self.locator} - {e}")
            log.error(f"Unexpected error entering text in element: {self.locator} - {e}")
            allure_attach_screenshot(self.driver)

    def attribute(self, attribute_name):
        log = custom_logger()
        try:
            attribute_value = self.element.get_attribute(attribute_name)
            log.info(f"Attribute '{attribute_name}' value: {attribute_value} from element: {self.locator}")
            return attribute_value
        except NoSuchAttributeException as e:
            print(f"Error getting attribute '{attribute_name}' from element: {self.locator} - {e}")
            log.error(f"Error getting attribute '{attribute_name}' from element: {self.locator} - {e}")
            allure_attach_screenshot(self.driver)
            return None
        except Exception as e:
            print(f"Unexpected error getting attribute '{attribute_name}' from element: {self.locator} - {e}")
            log.error(f"Unexpected error getting attribute '{attribute_name}' from element: {self.locator} - {e}")
            allure_attach_screenshot(self.driver)
            return None

    @property
    def text(self):
        log = custom_logger()
        text_value = self.element.text
        if text_value:
            log.info(f"Text found: '{text_value}' from element: {self.locator}")
        else:
            log.error(f"No text found in element: {self.locator}")
        return text_value

    def elements_text(self):
        log = custom_logger()
        text_list = []
        if len(self.elements) > 0:
            text_list = [element.text for element in self.elements]
            log.info(f"Text found on elements: '{text_list}' from element: {self.locator}")
        else:
            log.error(f"No elements found: {self.locator}")
        return text_list

    def click_element_by_text(self, target_text):
        log = custom_logger()
        if len(self.elements) > 0:
            for element in self.elements:
                if element.text == target_text:
                    self.action.move_to_element(element).click().perform()
                    log.info(
                        f"Text on element found and clicking on it: '{element.text}' from elements: {self.locator}")
                    break
        else:
            log.error(f"No elements found: {self.locator}")

    def get_index_of_element_by_text(self, target_text):
        log = custom_logger()
        if len(self.elements) > 0:
            for i, element in enumerate(self.elements):
                if element.text == target_text:
                    log.info(
                        f"Text on element found {element.text} and returning the index: '{i}' from elements: {self.locator}")
                    return i
        else:
            log.error(f"No elements found: {self.locator}")
            return None

    def get_element_text_by_index(self, index):
        log = custom_logger()
        if len(self.elements) > 0:
            for i, element in enumerate(self.elements):
                if i == index:
                    log.info(
                        f"Returning text on index {i} is {element.text} from elements: {self.locator}")
                    return element.text
        else:
            log.error(f"No elements found: {self.locator}")
            return None

    def click_element_by_index(self, index):
        log = custom_logger()
        if len(self.elements) > 0:
            for i, element in enumerate(self.elements):
                if i == index:
                    self.action.move_to_element(element).click().perform()
                    log.info(
                        f"Clicking the index {i} on elements: {self.locator}")
                    break
        else:
            log.error(f"No elements found: {self.locator}")

    def is_element_displayed(self):
        log = custom_logger()
        try:
            is_displayed = self.element.is_displayed()
            log.info(f"Element is displayed: {self.locator}")
        except NoSuchElementException as e:
            print(f"Element not found: {self.locator} - {e}")
            log.error(f"Element not found: {self.locator} - {e}")
            allure_attach_screenshot(self.driver)
            return False
        except Exception as e:
            print(f"Unexpected error checking if element is displayed: {self.locator} - {e}")
            log.error(f"Unexpected error checking if element is displayed: {self.locator} - {e}")
            return False

        return is_displayed

    def select_dropdown(self, select_by_type, value):
        log = custom_logger()
        try:
            self.scroll_to_element()
            select = Select(self.element)
            log.info(f"Dropdown Select on : {self.locator}")
            select_by_type = select_by_type.lower()
            if select_by_type == "index":
                select.select_by_index(value)
            elif select_by_type == "value":
                select.select_by_value(value)
            elif select_by_type == "text":
                select.select_by_visible_text(value)
            log.info(f"Dropdown Selected by {select_by_type} on : {value}")
        except (ElementClickInterceptedException, ElementNotInteractableException, ElementNotVisibleException,
                InvalidSelectorException, StaleElementReferenceException,) as e:
            print(f"Error selecting dropdown: {self.locator} - {e}")
            log.error(f"Error selecting dropdown: {self.locator} - {e}")
            allure_attach_screenshot(self.driver)
        except Exception as e:
            print(f"Unexpected error selecting dropdown: {self.locator} - {e}")
            log.error(f"Unexpected error selecting dropdown: {self.locator} - {e}")
            allure_attach_screenshot(self.driver)

    def get_dropdown_options(self):
        log = custom_logger()
        try:
            select = Select(self.element)
            options = [option.text for option in select.options]
            log.info(f"Dropdown options: {options} from element: {self.locator}")
            return options
        except (ElementClickInterceptedException, ElementNotInteractableException, ElementNotVisibleException,
                InvalidSelectorException, StaleElementReferenceException,) as e:
            print(f"Error getting dropdown options: {self.locator} - {e}")
            log.error(f"Error getting dropdown options: {self.locator} - {e}")
            allure_attach_screenshot(self.driver)
            return None
        except Exception as e:
            print(f"Unexpected error getting dropdown options: {self.locator} - {e}")
            log.error(f"Unexpected error getting dropdown options: {self.locator} - {e}")
            allure_attach_screenshot(self.driver)
            return None

    def is_element_selected(self):
        log = custom_logger()
        try:
            is_selected = self.element.is_selected()
            log.info(f"Element is selected: {self.locator}")
        except NoSuchElementException as e:
            print(f"Element not found: {self.locator} - {e}")
            log.error(f"Element not found: {self.locator} - {e}")
            allure_attach_screenshot(self.driver)
            return False
        except Exception as e:
            print(f"Unexpected error checking if element is selected: {self.locator} - {e}")
            log.error(f"Unexpected error checking if element is selected: {self.locator} - {e}")
            allure_attach_screenshot(self.driver)
            return False
        return is_selected

    def is_element_enabled(self):
        log = custom_logger()
        try:
            is_enabled = self.element.is_enabled()
            log.info(f"Element is enabled: {self.locator}")
        except NoSuchElementException as e:
            print(f"Element not found: {self.locator} - {e}")
            log.error(f"Element not found: {self.locator} - {e}")
            allure_attach_screenshot(self.driver)
            return False
        except Exception as e:
            print(f"Unexpected error checking if element is enabled: {self.locator} - {e}")
            log.error(f"Unexpected error checking if element is enabled: {self.locator} - {e}")
            allure_attach_screenshot(self.driver)
            return False
        return is_enabled

    def mouse_hover_on_element(self):
        log = custom_logger()
        try:
            self.action.move_to_element(self.element).perform()
            log.info(f"Mouse hovered on element: {self.locator}")
        except (ElementNotInteractableException, ElementNotVisibleException, StaleElementReferenceException,) as e:
            print(f"Error hovering on element: {self.locator} - {e}")
            log.error(f"Error hovering on element: {self.locator} - {e}")
            allure_attach_screenshot(self.driver)
        except Exception as e:
            print(f"Unexpected error hovering on element: {self.locator} - {e}")
            log.error(f"Unexpected error hovering on element: {self.locator} - {e}")
            allure_attach_screenshot(self.driver)

    def double_click_on_element(self):
        log = custom_logger()
        try:
            self.action.double_click(self.element).perform()
            log.info(f"Double clicked on element: {self.locator}")
        except (ElementNotInteractableException, ElementNotVisibleException,
                StaleElementReferenceException, ElementClickInterceptedException) as e:
            print(f"Error double clicking on element: {self.locator} - {e}")
            log.error(f"Error double clicking on element: {self.locator} - {e}")
            allure_attach_screenshot(self.driver)
        except Exception as e:
            print(f"Unexpected error double clicking on element: {self.locator} - {e}")
            log.error(f"Unexpected error double clicking on element: {self.locator} - {e}")
            allure_attach_screenshot(self.driver)

    def right_click_on_element(self):
        log = custom_logger()
        try:
            self.action.context_click(self.element).perform()
            log.info(f"Right clicked on element: {self.locator}")
        except (ElementNotInteractableException, ElementNotVisibleException,
                ElementClickInterceptedException, StaleElementReferenceException) as e:
            print(f"Error right clicking on element: {self.locator} - {e}")
            log.error(f"Error right clicking on element: {self.locator} - {e}")
            allure_attach_screenshot(self.driver)
        except Exception as e:
            print(f"Unexpected error right clicking on element: {self.locator} - {e}")
            log.error(f"Unexpected error right clicking on element: {self.locator} - {e}")
            allure_attach_screenshot(self.driver)

    def drag_an_element_and_drop_on_another_element(self, target_element):
        log = custom_logger()
        try:
            self.action.drag_and_drop(self.element, target_element).perform()
            log.info(f"Dragged element: {self.locator} and dropped on element: {target_element}")
        except (ElementNotInteractableException, ElementNotVisibleException,
                ElementClickInterceptedException, StaleElementReferenceException) as e:
            print(f"Error dragging and dropping element: {self.locator} - {e}")
            log.error(f"Error dragging and dropping element: {self.locator} - {e}")
            allure_attach_screenshot(self.driver)
        except Exception as e:
            print(f"Unexpected error dragging and dropping element: {self.locator} - {e}")
            log.error(f"Unexpected error dragging and dropping element: {self.locator} - {e}")
            allure_attach_screenshot(self.driver)

    def scroll_to_element(self):
        log = custom_logger()
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", self.element)
            log.info(f"Scrolled to element: {self.locator}")
        except (ElementNotInteractableException, ElementNotVisibleException,
                StaleElementReferenceException) as e:
            print(f"Error scrolling to element: {self.locator} - {e}")
            log.error(f"Error scrolling to element: {self.locator} - {e}")
            allure_attach_screenshot(self.driver)
        except Exception as e:
            print(f"Unexpected error scrolling to element: {self.locator} - {e}")
            log.error(f"Unexpected error scrolling to element: {self.locator} - {e}")
            allure_attach_screenshot(self.driver)

    def clear_element_text(self):
        log = custom_logger()
        try:
            self.element.clear()
            log.info(f"Cleared text in element: {self.locator}")
        except (ElementClickInterceptedException, ElementNotInteractableException, ElementNotVisibleException,
                InvalidSelectorException, StaleElementReferenceException,) as e:
            print(f"Error clearing text in element: {self.locator} - {e}")
            log.error(f"Error clearing text in element: {self.locator} - {e}")
            allure_attach_screenshot(self.driver)
        except Exception as e:
            print(f"Unexpected error clearing text in element: {self.locator} - {e}")
            log.error(f"Unexpected error clearing text in element: {self.locator} - {e}")
            allure_attach_screenshot(self.driver)
