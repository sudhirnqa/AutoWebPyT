import datetime
import inspect
import logging

import allure
from faker import Faker
import random

from time import sleep

from selenium.common import JavascriptException


def allure_attach_screenshot(driver):
    """Attach a screenshot to the Allure report."""
    # Get the name of the test function
    test_name = inspect.stack()[1][3]
    # Attach the screenshot to the Allure report
    now = datetime.datetime.now()
    formated_now = now.strftime("%Y-%m-%d-%H-%M-%S-%f") + str(
        int(now.strftime("%f")) * random.randrange(1, 100)
    )
    test_name = f"{test_name}_{formated_now}"
    allure.attach(
        driver.get_screenshot_as_png(),
        name=test_name,
        attachment_type=allure.attachment_type.PNG,
    )


def custom_logger(log_level=logging.DEBUG):
    """Create and configure a custom logger."""
    """Using log settings from pytest.ini"""
    name = inspect.stack()[1][3]
    logger = logging.getLogger(name)

    return logger


def data_faker():
    """Generate fake demographic data."""
    log = custom_logger()
    try:
        fake = Faker()

        # Create an empty dictionary to store the fake data
        fake_data = {
            "name": fake.name(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "address": fake.address(),
            "address_1": fake.address(),
            "address_2": fake.address(),
            "street_address": fake.street_address(),
            "city": fake.city(),
            "state": fake.state(),
            "zipcode": fake.zipcode(),
            "country": fake.country(),
            "email": fake.email(),
            "safe_email": fake.safe_email(),
            "password": fake.password(),
            "phone_number": fake.phone_number(),
            "company": fake.company(),
            "job": fake.job(),
            "text": fake.text(max_nb_chars=100),
            "texts": fake.texts(nb_texts=3, max_nb_chars=100),
            "sentence": fake.sentence(),
            "paragraph": fake.paragraph(),
            "date_of_birth": fake.date_of_birth(minimum_age=18, maximum_age=90),
            "date_this_decade": fake.date_this_decade(),
            "url": fake.url(),
            "ipv4": fake.ipv4(),
            "user_agent": fake.user_agent(),
            "uuid4": fake.uuid4(),
            "credit_card_number": fake.credit_card_number(),
            "currency_code": fake.currency_code(),
            "color_name": fake.color_name(),
            "boolean": fake.boolean(),
        }

        # Log the generated demographics
        log.info(f"Generated demographics: {fake_data}")

    except Exception as e:
        log.error(f"Error generating fake demographics: {e}")
        raise

    return fake_data


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
