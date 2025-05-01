import datetime
import inspect
import logging

import allure
import faker
import random

from time import sleep

from selenium.common import JavascriptException


def allure_attach_screenshot(driver):
    """Attach a screenshot to the Allure report."""
    # Get the name of the test function
    test_name = inspect.stack()[1][3]
    # Attach the screenshot to the Allure report
    now = datetime.datetime.now()
    formated_now = (now.strftime('%Y-%m-%d-%H-%M-%S-%f') +
                    str(int(now.strftime('%f')) * random.randrange(1, 100)))
    test_name = f"{test_name}_{formated_now}"
    allure.attach(
        driver.get_screenshot_as_png(),
        name=test_name,
        attachment_type=allure.attachment_type.PNG
    )


def custom_logger(log_level=logging.DEBUG):
    """Create and configure a custom logger."""
    name = inspect.stack()[1][3]
    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(log_level)
        file_handler = logging.FileHandler("AutomationRun.log", mode='a')
        file_format = logging.Formatter(
            fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%m-%d-%Y %H:%M:%S"
        )
        file_handler.setFormatter(file_format)
        logger.addHandler(file_handler)

    return logger


def get_fake_demographics():
    """Generate fake demographic data."""
    log = custom_logger()
    try:
        fake = faker.Faker()
        demographics = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "phone_number": fake.phone_number(),
            "address_1": fake.street_address(),
            "address_2": fake.secondary_address(),
            "city": fake.city(),
            "state": fake.state(),
            "zip_code": fake.zipcode(),
            "password": fake.password(),
            "date_of_birth": fake.date_of_birth(minimum_age=18, maximum_age=100),
            "company_name": fake.company(),
        }

        # Log the generated demographics
        log.info(f"Generated demographics: {demographics}")

    except Exception as e:
        log.error(f"Error generating fake demographics: {e}")
        raise

    return demographics


def scroll_down_to_bottom(driver):
    """Scroll down to the bottom of the page. Load the page if not loaded."""
    log = custom_logger()
    try:
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(2)  # Adjust the sleep time as needed
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                log.info("Reached the bottom of the page.")
                break
            last_height = new_height
            log.info(f"Scrolling down... New height: {new_height}")
    except JavascriptException as e:
        log.error(f"JavaScript error while scrolling: {e}")
        raise
    except Exception as e:
        log.error(f"Error scrolling down: {e}")
        raise
