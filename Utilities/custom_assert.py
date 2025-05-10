import traceback

from Utilities.common_utils import allure_attach_screenshot, custom_logger


class CustomAssert:
    """
    A class to perform soft assertions in tests.

    Collects multiple assertion failures within a test method
    and raises a single AssertionError at the end if any occurred.
    """

    def __init__(self, driver):
        """Initializes the CustomAssert instance with an empty list for failures."""
        self.failures = []
        self.driver = driver

    def _add_failure(self, message):
        """
        Adds a failure message to the list, including traceback information.

        Args:
            message (str): The description of the assertion failure.
        """
        # Capture the traceback leading to the assertion call, but exclude
        # the internal frames of CustomAssert itself.
        stack = traceback.extract_stack()
        # Typically, the last frame is _add_failure, the one before it is the
        # specific assertion method (e.g., assert_equal), and the one before
        # that is the test method calling the assertion.
        relevant_frame = stack[-3]
        failure_info = (
            f"Failure in file '{relevant_frame.filename}', line {relevant_frame.lineno}, "
            f"in '{relevant_frame.name}':\n  {message}"
        )
        self.failures.append(failure_info)
        # Take a screenshot of the driver to attach to the report
        allure_attach_screenshot(self.driver)

    # --- Assertion Methods ---

    def assert_equals(self, actual, expected, message=""):
        """
        Asserts that two values are equal.

        Args:
            actual: The actual value obtained.
            expected: The expected value.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if actual != expected:
            error_msg = (
                f"Assertion Failed: Expected '{expected}' (type: {type(expected)}), "
                f"but got '{actual}' (type: {type(actual)})."
            )
            if message:
                error_msg += f" Additional Info: {message}"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Assertion Passed: '{actual}' == '{expected}'.")

    def assert_not_equals(self, actual, unexpected, message=""):
        """
        Asserts that two values are not equal.

        Args:
            actual: The actual value obtained.
            unexpected: The value that actual should not be equal to.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if actual == unexpected:
            error_msg = f"Assertion Failed: Expected value not to be '{unexpected}', but it was."
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Value is not equal to '{unexpected}', as expected: '{actual}'.")

    def assert_true(self, condition, message=""):
        """
        Asserts that a condition is True.

        Args:
            condition: The condition to evaluate.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if not condition:
            error_msg = (
                f"Assertion Failed: Expected condition to be True, but it was False."
            )
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Condition is True, as expected: '{condition}'.")

    def assert_false(self, condition, message=""):
        """
        Asserts that a condition is False.

        Args:
            condition: The condition to evaluate.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if condition:
            error_msg = (
                f"Assertion Failed: Expected condition to be False, but it was True."
            )
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Condition is False, as expected: '{condition}'.")

    def assert_is_none(self, obj, message=""):
        """
        Asserts that an object is None.

        Args:
            obj: The object to check.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if obj is not None:
            error_msg = (
                f"Assertion Failed: Expected object to be None, but it was '{obj}'."
            )
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Object is None, as expected: '{obj}'.")

    def assert_is_not_none(self, obj, message=""):
        """
        Asserts that an object is not None.

        Args:
            obj: The object to check.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if obj is None:
            error_msg = f"Assertion Failed: Expected object not to be None, but it was."
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Object is not None, as expected: '{obj}'.")

    def assert_in(self, member, container, message=""):
        """
        Asserts that a member is present in a container.

        Args:
            member: The item to check for.
            container: The container (e.g., list, tuple, dict, string) to check within.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if member not in container:
            error_msg = f"Assertion Failed: Expected '{member}' to be in '{container}', but it was not."
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"'{member}' is in '{container}', as expected.")

    def assert_not_in(self, member, container, message=""):
        """
        Asserts that a member is not present in a container.

        Args:
            member: The item to check for.
            container: The container (e.g., list, tuple, dict, string) to check within.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if member in container:
            error_msg = f"Assertion Failed: Expected '{member}' not to be in '{container}', but it was."
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"'{member}' is not in '{container}', as expected.")

    def assert_dict_equals(self, actual, expected, message=""):
        """
        Asserts that two dictionaries are equal.

        Args:
            actual (dict): The actual dictionary obtained.
            expected (dict): The expected dictionary.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if actual != expected:
            error_msg = (
                f"Assertion Failed: Expected dictionary '{expected}', "
                f"but got '{actual}'."
            )
            if message:
                error_msg += f" Additional Info: {message}"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Assertion Passed: Dictionaries are equal.")

    def assert_dict_not_equals(self, actual, unexpected, message=""):
        """
        Asserts that two dictionaries are not equal.

        Args:
            actual (dict): The actual dictionary obtained.
            unexpected (dict): The dictionary that actual should not be equal to.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if actual == unexpected:
            error_msg = (
                f"Assertion Failed: Expected dictionary not to be '{unexpected}', "
                f"but it was."
            )
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Dictionaries are not equal, as expected.")

    def assert_list_equals(self, actual, expected, message=""):
        """
        Asserts that two lists are equal.

        Args:
            actual (list): The actual list obtained.
            expected (list): The expected list.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if actual != expected:
            error_msg = (
                f"Assertion Failed: Expected list '{expected}', " f"but got '{actual}'."
            )
            if message:
                error_msg += f" Additional Info: {message}"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Assertion Passed: Lists are equal.")

    def assert_list_not_equals(self, actual, unexpected, message=""):
        """
        Asserts that two lists are not equal.

        Args:
            actual (list): The actual list obtained.
            unexpected (list): The list that actual should not be equal to.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if actual == unexpected:
            error_msg = (
                f"Assertion Failed: Expected list not to be '{unexpected}', "
                f"but it was."
            )
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Lists are not equal, as expected.")

    def assert_list_contains(self, actual, expected, message=""):
        """
        Asserts that a list contains a specific item.

        Args:
            actual (list): The actual list obtained.
            expected: The item expected to be in the list.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if expected not in actual:
            error_msg = (
                f"Assertion Failed: Expected list '{actual}' to contain '{expected}', "
                f"but it did not."
            )
            if message:
                error_msg += f" Additional Info: {message}"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Assertion Passed: List contains '{expected}'.")

    def assert_list_not_contains(self, actual, unexpected, message=""):
        """
        Asserts that a list does not contain a specific item.

        Args:
            actual (list): The actual list obtained.
            unexpected: The item expected not to be in the list.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if unexpected in actual:
            error_msg = (
                f"Assertion Failed: Expected list '{actual}' not to contain '{unexpected}', "
                f"but it did."
            )
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Assertion Passed: List does not contain '{unexpected}'.")

    def assert_list_empty(self, actual, message=""):
        """
        Asserts that a list is empty.

        Args:
            actual (list): The actual list obtained.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if actual:
            error_msg = f"Assertion Failed: Expected list to be empty, but it contained '{actual}'."
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Assertion Passed: List is empty.")

    def assert_list_not_empty(self, actual, message=""):
        """
        Asserts that a list is not empty.

        Args:
            actual (list): The actual list obtained.
            Message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if not actual:
            error_msg = f"Assertion Failed: Expected list not to be empty, but it was."
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Assertion Passed: List is not empty.")

    def assert_string_contains(self, actual, expected, message=""):
        """
        Asserts that a string contains a specific substring.

        Args:
            actual (str): The actual string obtained.
            expected (str): The substring expected to be in the string.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if expected not in actual:
            error_msg = (
                f"Assertion Failed: Expected string '{actual}' to contain '{expected}', "
                f"but it did not."
            )
            if message:
                error_msg += f" Additional Info: {message}"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Assertion Passed: String contains '{expected}'.")

    def assert_string_not_contains(self, actual, unexpected, message=""):
        """
        Asserts that a string does not contain a specific substring.

        Args:
            actual (str): The actual string obtained.
            unexpected (str): The substring expected not to be in the string.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if unexpected in actual:
            error_msg = (
                f"Assertion Failed: Expected string '{actual}' not to contain '{unexpected}', "
                f"but it did."
            )
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Assertion Passed: String does not contain '{unexpected}'.")

    def assert_string_empty(self, actual, message=""):
        """
        Asserts that a string is empty.

        Args:
            actual (str): The actual string obtained.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if actual:
            error_msg = (
                f"Assertion Failed: Expected string to be empty, but it was '{actual}'."
            )
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Assertion Passed: String is empty.")

    def assert_string_not_empty(self, actual, message=""):
        """
        Asserts that a string is not empty.

        Args:
            actual (str): The actual string obtained.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if not actual:
            error_msg = (
                f"Assertion Failed: Expected string not to be empty, but it was."
            )
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Assertion Passed: String is not empty.")

    def assert_string_equals_ignore_case(self, actual, expected, message=""):
        """
        Asserts that two strings are equal, ignoring case.

        Args:
            actual (str): The actual string obtained.
            expected (str): The expected string.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if actual.lower() != expected.lower():
            error_msg = (
                f"Assertion Failed: Expected '{expected}' (case-insensitive), "
                f"but got '{actual}'."
            )
            if message:
                error_msg += f" Additional Info: {message}"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(
                f"Assertion Passed: '{actual}' == '{expected}' (case-insensitive)."
            )

    def assert_string_not_equals_ignore_case(self, actual, unexpected, message=""):
        """
        Asserts that two strings are not equal, ignoring case.

        Args:
            actual (str): The actual string obtained.
            unexpected (str): The string that actual should not be equal to.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if actual.lower() == unexpected.lower():
            error_msg = (
                f"Assertion Failed: Expected value not to be '{unexpected}' (case-insensitive), "
                f"but it was."
            )
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(
                f"Value is not equal to '{unexpected}' (case-insensitive), as expected."
            )

    def assert_is_instance(self, obj, expected_type, message=""):
        """
        Asserts that an object is an instance of a specific type.

        Args:
            obj: The object to check.
            expected_type: The expected type or class.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if not isinstance(obj, expected_type):
            error_msg = (
                f"Assertion Failed: Expected object of type '{expected_type.__name__}', "
                f"but got '{type(obj).__name__}'."
            )
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(
                f"Object is an instance of '{expected_type.__name__}', as expected."
            )

    def assert_is_not_instance(self, obj, expected_type, message=""):
        """
        Asserts that an object is not an instance of a specific type.

        Args:
            obj: The object to check.
            expected_type: The expected type or class.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if isinstance(obj, expected_type):
            error_msg = (
                f"Assertion Failed: Expected object not to be an instance of '{expected_type.__name__}', "
                f"but it was."
            )
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(
                f"Object is not an instance of '{expected_type.__name__}', as expected."
            )

    def assert_string_equals(self, actual, expected, message=""):
        """
        Asserts that two strings are equal.

        Args:
            actual (str): The actual string obtained.
            expected (str): The expected string.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if actual != expected:
            error_msg = (
                f"Assertion Failed: Expected '{expected}' (case-insensitive), "
                f"but got '{actual}'."
            )
            if message:
                error_msg += f" Additional Info: {message}"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(
                f"Assertion Passed: '{actual}' == '{expected}' (case-insensitive)."
            )

    def assert_string_not_equals(self, actual, unexpected, message=""):
        """
        Asserts that two strings are not equal.

        Args:
            actual (str): The actual string obtained.
            unexpected (str): The string that actual should not be equal to.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if actual == unexpected:
            error_msg = (
                f"Assertion Failed: Expected value not to be '{unexpected}' (case-insensitive), "
                f"but it was."
            )
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(
                f"Value is not equal to '{unexpected}' (case-insensitive), as expected."
            )

    def assert_string_blank(self, actual, message=""):
        """
        Asserts that a string is blank (empty or whitespace).

        Args:
            actual (str): The actual string obtained.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if actual and actual.strip():
            error_msg = (
                f"Assertion Failed: Expected string to be blank, but it was '{actual}'."
            )
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Assertion Passed: String is blank.")

    def assert_string_not_blank(self, actual, message=""):
        """
        Asserts that a string is not blank (contains non-whitespace characters).

        Args:
            actual (str): The actual string obtained.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if not actual or not actual.strip():
            error_msg = (
                f"Assertion Failed: Expected string not to be blank, but it was."
            )
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Assertion Passed: String is not blank.")

    def assert_string_numeric(self, actual, message=""):
        """
        Asserts that a string is numeric (contains only digits).

        Args:
            actual (str): The actual string obtained.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if not actual.isnumeric():
            error_msg = f"Assertion Failed: Expected string to be numeric, but it was '{actual}'."
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Assertion Passed: String is numeric.")

    def assert_string_not_numeric(self, actual, message=""):
        """
        Asserts that a string is not numeric (contains non-digit characters).

        Args:
            actual (str): The actual string obtained.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if actual.isnumeric():
            error_msg = f"Assertion Failed: Expected string not to be numeric, but it was '{actual}'."
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Assertion Passed: String is not numeric.")

    def assert_string_alphabetic(self, actual, message=""):
        """
        Asserts that a string is alphabetic (contains only letters).

        Args:
            actual (str): The actual string obtained.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if not actual.isalpha():
            error_msg = f"Assertion Failed: Expected string to be alphabetic, but it was '{actual}'."
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Assertion Passed: String is alphabetic.")

    def assert_string_not_alphabetic(self, actual, message=""):
        """
        Asserts that a string is not alphabetic (contains non-letter characters).

        Args:
            actual (str): The actual string obtained.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if actual.isalpha():
            error_msg = f"Assertion Failed: Expected string not to be alphabetic, but it was '{actual}'."
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Assertion Passed: String is not alphabetic.")

    def assert_string_alphanumeric(self, actual, message=""):
        """
        Asserts that a string is alphanumeric (contains letters and/or digits).

        Args:
            actual (str): The actual string obtained.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if not actual.isalnum():
            error_msg = f"Assertion Failed: Expected string to be alphanumeric, but it was '{actual}'."
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Assertion Passed: String is alphanumeric.")

    def assert_string_not_alphanumeric(self, actual, message=""):
        """
        Asserts that a string is not alphanumeric (contains non-letter and/or non-digit characters).

        Args:
            actual (str): The actual string obtained.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if actual.isalnum():
            error_msg = f"Assertion Failed: Expected string not to be alphanumeric, but it was '{actual}'."
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Assertion Passed: String is not alphanumeric.")

    def assert_string_contains_special_characters(self, actual, message=""):
        """
        Asserts that a string contains special characters.

        Args:
            actual (str): The actual string obtained.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if not any(not char.isalnum() and not char.isspace() for char in actual):
            error_msg = f"Assertion Failed: Expected string to contain special characters, but it did not."
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Assertion Passed: String contains special characters.")

    def assert_string_not_contains_special_characters(self, actual, message=""):
        """
        Asserts that a string does not contain special characters.

        Args:
            actual (str): The actual string obtained.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if any(not char.isalnum() and not char.isspace() for char in actual):
            error_msg = f"Assertion Failed: Expected string not to contain special characters, but it did."
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Assertion Passed: String does not contain special characters.")

    def assert_string_email(self, actual, message=""):
        """
        Asserts that a string is a valid email address.

        Args:
            actual (str): The actual string obtained.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if "@" not in actual or "." not in actual.split("@")[-1]:
            error_msg = f"Assertion Failed: Expected string to be a valid email address, but it was '{actual}'."
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Assertion Passed: String is a valid email address.")

    def assert_string_not_email(self, actual, message=""):
        """
        Asserts that a string is not a valid email address.

        Args:
            actual (str): The actual string obtained.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if "@" in actual and "." in actual.split("@")[-1]:
            error_msg = f"Assertion Failed: Expected string not to be a valid email address, but it was '{actual}'."
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Assertion Passed: String is not a valid email address.")

    def assert_tuple_equals(self, actual, expected, message=""):
        """
        Asserts that two tuples are equal.

        Args:
            actual (tuple): The actual tuple obtained.
            expected (tuple): The expected tuple.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if actual != expected:
            error_msg = (
                f"Assertion Failed: Expected tuple '{expected}', "
                f"but got '{actual}'."
            )
            if message:
                error_msg += f" Additional Info: {message}"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Assertion Passed: Tuples are equal.")

    def assert_tuple_not_equals(self, actual, unexpected, message=""):
        """
        Asserts that two tuples are not equal.

        Args:
            actual (tuple): The actual tuple obtained.
            unexpected (tuple): The tuple that actual should not be equal to.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if actual == unexpected:
            error_msg = (
                f"Assertion Failed: Expected tuple not to be '{unexpected}', "
                f"but it was."
            )
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Tuples are not equal, as expected.")

    def assert_tuple_contains(self, actual, expected, message=""):
        """
        Asserts that a tuple contains a specific item.

        Args:
            actual (tuple): The actual tuple obtained.
            expected: The item expected to be in the tuple.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if expected not in actual:
            error_msg = (
                f"Assertion Failed: Expected tuple '{actual}' to contain '{expected}', "
                f"but it did not."
            )
            if message:
                error_msg += f" Additional Info: {message}"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Assertion Passed: Tuple contains '{expected}'.")

    def assert_tuple_not_contains(self, actual, unexpected, message=""):
        """
        Asserts that a tuple does not contain a specific item.

        Args:
            actual (tuple): The actual tuple obtained.
            unexpected: The item expected not to be in the tuple.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if unexpected in actual:
            error_msg = (
                f"Assertion Failed: Expected tuple '{actual}' not to contain '{unexpected}', "
                f"but it did."
            )
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Assertion Passed: Tuple does not contain '{unexpected}'.")

    def assert_tuple_empty(self, actual, message=""):
        """
        Asserts that a tuple is empty.

        Args:
            actual (tuple): The actual tuple obtained.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if actual:
            error_msg = f"Assertion Failed: Expected tuple to be empty, but it contained '{actual}'."
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Assertion Passed: Tuple is empty.")

    def assert_tuple_not_empty(self, actual, message=""):
        """
        Asserts that a tuple is not empty.

        Args:
            actual (tuple): The actual tuple obtained.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if not actual:
            error_msg = f"Assertion Failed: Expected tuple not to be empty, but it was."
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Assertion Passed: Tuple is not empty.")

    def assert_dict_contains(self, actual, expected, message=""):
        """
        Asserts that a dictionary contains a specific key-value pair.

        Args:
            actual (dict): The actual dictionary obtained.
            expected (dict): The expected key-value pair.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if not all(item in actual.items() for item in expected.items()):
            error_msg = (
                f"Assertion Failed: Expected dictionary '{actual}' to contain '{expected}', "
                f"but it did not."
            )
            if message:
                error_msg += f" Additional Info: {message}"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Assertion Passed: Dictionary contains '{expected}'.")

    def assert_dict_not_contains(self, actual, unexpected, message=""):
        """
        Asserts that a dictionary does not contain a specific key-value pair.

        Args:
            actual (dict): The actual dictionary obtained.
            unexpected (dict): The unexpected key-value pair.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if any(
            unexpected_item in actual.items() for unexpected_item in unexpected.items()
        ):
            error_msg = (
                f"Assertion Failed: Expected dictionary '{actual}' not to contain '{unexpected}', "
                f"but it did."
            )
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Assertion Passed: Dictionary does not contain '{unexpected}'.")

    def assert_dict_empty(self, actual, message=""):
        """
        Asserts that a dictionary is empty.

        Args:
            actual (dict): The actual dictionary obtained.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if actual:
            error_msg = f"Assertion Failed: Expected dictionary to be empty, but it contained '{actual}'."
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Assertion Passed: Dictionary is empty.")

    def assert_dict_not_empty(self, actual, message=""):
        """
        Asserts that a dictionary is not empty.

        Args:
            actual (dict): The actual dictionary obtained.
            message (str, optional): A custom message to include on failure. Defaults to "".
        """
        log = custom_logger()
        if not actual:
            error_msg = (
                f"Assertion Failed: Expected dictionary not to be empty, but it was."
            )
            if message:
                error_msg += f" [{message}]"
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            log.info(f"Assertion Passed: Dictionary is not empty.")

    def assert_raises(self, expected_exception, func, *args, **kwargs):
        """
        Asserts that a specific exception is raised when calling a function.

        Args:
            expected_exception (Exception): The type of exception expected.
            Func (callable): The function to call.
            *args: Positional arguments to pass to the function.
            **kwargs: Keyword arguments to pass to the function.
        """
        log = custom_logger()
        try:
            func(*args, **kwargs)
        except expected_exception:
            # Expected exception was raised, assertion passes
            log.info(f"Expected exception '{expected_exception.__name__}' was raised.")
            return
        except Exception as e:
            # A different exception was raised
            error_msg = (
                f"Assertion Failed: Expected exception '{expected_exception.__name__}', "
                f"but got '{type(e).__name__}'."
            )
            log.error(error_msg)
            self._add_failure(error_msg)
        else:
            # No exception was raised
            error_msg = (
                f"Assertion Failed: Expected exception '{expected_exception.__name__}', "
                f"but no exception was raised."
            )
            log.error(error_msg)
            self._add_failure(error_msg)

    # --- Finalization ---

    def finalize(self):
        """
        Checks collected failures and raises a single AssertionError if any exist.

        This method should be called at the end of the test execution.
        """
        log = custom_logger()
        if self.failures:
            # Combine all failure messages
            combined_message = "\n\n".join(self.failures)
            # Add a header indicating the number of failures
            failure_summary = (
                f"{len(self.failures)} assertion(s) failed:\n\n{combined_message}"
            )
            # Clear the failure list in case the instance is reused (though not recommended per test)
            self.failures = []
            # Raise the combined error
            log.error(failure_summary)
            raise AssertionError(failure_summary)
