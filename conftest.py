from datetime import datetime
from pathlib import Path

from pytest import fixture, hookimpl
from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService

from Utilities.common_utils import custom_logger

global driver


def pytest_addoption(parser):
    """Add custom command-line options for pytest."""
    parser.addoption("--browser", action="store", default="chrome", help="chrome or edge or firefox")
    parser.addoption("--env", action="store", default="qa", help="environment under test")


@fixture(scope='session')
def browser_and_env(request):
    """Fixture to retrieve browser and environment options."""
    return [request.config.getoption("--browser"), request.config.getoption("--env")]


@fixture(scope='session', autouse=True)
def invoke_browser(browser_and_env):
    """Fixture to initialize and yield the browser driver."""
    global driver
    log = custom_logger()
    browser = browser_and_env[0].lower()
    base_url = {
        'dev': 'https://dev.automationexercise.com/',
        'qa': 'https://automationexercise.com/',
        'staging': 'https://stage.automationexercise.com/'
    }[browser_and_env[1].lower()]

    log.info(f"Browser: {browser}")
    log.info(f"Base URL: {base_url}")

    try:
        if browser in ['chrome', 'gc']:
            chrome_options = ChromeOptions()
            chrome_options.add_argument("--incognito")
            driver = webdriver.Chrome(service=ChromeService(executable_path="./Drivers/chromedriver.exe"),
                                      options=chrome_options)
        elif browser in ['firefox', 'ff']:
            firefox_options = FirefoxOptions()
            firefox_options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"
            driver = webdriver.Firefox(service=FirefoxService(executable_path="./Drivers/geckodriver.exe"),
                                       options=firefox_options)
        else:
            driver = webdriver.Edge(service=EdgeService(executable_path="./Drivers/msedgedriver.exe"))

    except WebDriverException as e:
        print(f"WebDriverException: {e}")
        log.error(f"WebDriverException: {e}")

    except Exception as e:
        print(f"Error initializing browser: {e}")
        log.error(f"Error initializing browser: {e}")

    log.info(f"Driver initialized: {driver}")
    log.info(f"Driver ID: {id(driver)}")
    driver.implicitly_wait(5)
    log.info(f"implicitly_wait: {5} seconds")
    driver.maximize_window()
    driver.get(base_url)
    log.info(f"Navigated to URL: {base_url}")

    yield driver
    if driver is not None:
        driver.quit()
        log.info(f"Driver quit: {driver}")


@hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture screenshots for failed tests."""
    log = custom_logger()
    now = datetime.now()
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when in ['call', 'setup']:
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            log.info(f"Test failed: {report.nodeid}")
            # file_name = report.nodeid.replace("::", "_").replace("[","_").replace("]","_") + ".png"
            file_name = str(screenshot) + "/screenshot" + now.strftime("%S%H%d%m%Y") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = ('<div><img src="/%s" alt="screenshot" style="width:304px;height:228px;" '
                        'onclick="window.open(this.src)" align="right"/></div>') % file_name
                extra.append(pytest_html.extras.html(html))
        report.extras = extra


@hookimpl(tryfirst=True)
def pytest_configure(config):
    """Configure pytest to generate reports and screenshots."""
    log = custom_logger()
    log.info(''.center(100, "-"))
    log.info("Initializing Test".center(100, "-"))
    log.info(''.center(100, "-"))
    log.info(f"Configuring pytest: {config}")
    global screenshot
    now = datetime.now()
    report_dir = Path('Reports', now.strftime("%S%H%d%m%Y"))
    report_dir.mkdir(parents=True, exist_ok=True)
    screenshot = Path('Screenshots', now.strftime("%S%H%d%m%Y"))
    screenshot.mkdir(parents=True, exist_ok=True)
    pytest_html = report_dir / f"report_{now.strftime('%H%M%S')}.html"
    config.option.htmlpath = pytest_html
    config.option.self_contained_html = True
    log.info(f"Report directory created: {report_dir}")
    log.info(f"Screenshot directory created: {screenshot}")
    log.info(f"Report path: {pytest_html}")


def _capture_screenshot(name):
    """Capture a screenshot."""
    log = custom_logger()
    log.info(f"Capturing screenshot on failure: {name}")
    driver.get_screenshot_as_file(name)


def pytest_html_report_title(report):
    """Set the title for the HTML report."""
    log = custom_logger()
    log.info("Setting HTML report title")
    now = datetime.now().strftime("%m-%d-%Y-%H:%S")
    report.title = f"Test Automation Report - {now}"
    log.info(f"Report title set: {report.title}")
