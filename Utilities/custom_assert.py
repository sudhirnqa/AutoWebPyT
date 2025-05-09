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

    def assert_equal(self, actual, expected, message=""):
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

    def assert_not_equal(self, actual, unexpected, message=""):
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

    def assert_raises(self, expected_exception, func, *args, **kwargs):
        """
        Asserts that a specific exception is raised when calling a function.

        Args:
            expected_exception (Exception): The type of exception expected.
            func (callable): The function to call.
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
