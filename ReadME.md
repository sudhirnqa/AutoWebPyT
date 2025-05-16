# AutoWebPyT

AutoWebPyT is a Python-based automation framework designed for end-to-end testing of web application. It leverages
popular libraries like `pytest`, `selenium`, and `faker` to provide a robust and scalable solution for automating UI
tests, generating test data, and producing detailed test reports.

---

### Framework Features and Components:

- **End-to-End Testing**: Automates web application workflows using Selenium WebDriver.
- **Page Object Model (POM)**: Encapsulates web elements and actions for each page.
- **Fixtures**: Manages test setup and teardown.
- **Soft Assertions**: Allows multiple assertions in a single test.
- **Allure Reporting**: Provides detailed test execution reports with screenshots for failures using `pytest-allure`.
- **HTML Reporting**: Generates HTML reports with screenshot for test results using `pytest-html`.
- **Directories**: Reports and Screenshots are organized in separate directories, created dynamically during runtime.
- **Config File**: Centralized configuration for environment variables and test settings.
- **Logging**: Captures detailed logs for test execution.
- **Data Generation**: Uses `faker` library for generating random user data.
- **Custom Waits**: Implements explicit waits for dynamic elements.
- **Cross-Browser Testing**: Supports multiple browsers (Chrome, Firefox, Edge).
- **Openpyxl**: For Excel file operations.
- **Scalability**: Modular design for easy addition of new test cases and components.

---

### Prerequisites

1. **Python**: Ensure Python 3.8+ is installed.
2. **Browser Driver**: Update the appropriate WebDriver (e.g., ChromeDriver) in //Drivers.
3. **Dependencies**: Install required Python packages using `pip`.

---

### Installation

Follow these steps to set up the project:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sudhirnqa/AutoWebPyT.git
   cd AutoWebPyT
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Allure (for Reporting)**:
    - Download and install Allure from the [official website](https://docs.qameta.io/allure/).
    - Add Allure to your system's PATH.

---

## Project Structure

```
AutoWebPyT/
├── Drivers/                # Webdrivers (e.g., Chromedriver.exe, Geckodriver.exe)
├── Helpers/                # Common helper functions (e.g,. handling files)
├── Locators/               # Page locators
├── Pages/                  # Page Object Model (POM) classes
├── Reports/                # HTML reports
├── Screenshots/            # Screenshots of failed tests           
├── Testdata/               # Test data files (e.g., JSON)
├── Testsuite/              # Test cases
├── Utilities/              # Utility functions (e.g., logging, data generation)
├── conftest.py             # Pytest configuration/ fixture file
├── pytest.ini              # Pytest configuration file
├── requirements.txt        # Project dependencies
└── ReadME.md               # Project documentation
```

---

## Execution

### Running Tests

To execute the test suite, use the following command: (the required *args are handled in `pytest.ini` file)

```bash
pytest
```

### Generating Allure Reports

After running the tests, generate and view the Allure report:

```bash
allure serve reports/
```

---

## Testing and Reporting

1. **Test Execution**:
    - Tests are written using `pytest` and follow a modular structure.
    - Soft assertions are used to ensure multiple validations can run in a single test.

2. **Reporting**:
    - Allure reports provide detailed insights into test execution, including screenshots for failed tests.
    - Logs are generated for debugging purposes.
