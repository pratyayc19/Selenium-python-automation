# Selenium Python Automation Framework

## E-Commerce Login and Product Search Automation

A Selenium Python automation framework for testing the **Login and Product Search** functionality of an e-commerce web application.

This project is developed as part of **Capstone Assignment 2: Selenium Python Framework Development (Unittest + PyTest + POM)**.

The framework is designed using reusable Page Objects, utility classes, configuration management, CSV-based test data, explicit waits, logging, failure screenshots, and HTML reporting.

---

## 1. Project Objective

The objective of this project is to design and develop a reusable and maintainable Selenium Python automation framework for automating the following e-commerce workflow:

```text
Launch Browser
      ↓
Open Application
      ↓
Login
      ↓
Navigate to Products
      ↓
Search Product
      ↓
Verify Search Results
      ↓
Verify Requested Product
```

The framework demonstrates the practical implementation of:

- Selenium WebDriver
- Python
- PyTest
- Unittest
- Page Object Model (POM)
- Utility Classes
- Configuration Management
- CSV Test Data Handling
- Explicit Waits
- Exception Handling
- Logging
- Failure Screenshots
- HTML Reporting

---

## 2. Application Under Test

The framework is implemented using the public demo application:

**Automation Exercise**

```text
https://automationexercise.com/
```

The application is used only for automation practice and academic demonstration.

---

## 3. Key Features

### Selenium WebDriver

Selenium WebDriver is used to automate browser interactions including:

- Browser launch
- Navigation
- Element interaction
- Login
- Product search
- Result verification

### Page Object Model

The framework follows the Page Object Model design pattern.

Page-specific locators and operations are maintained separately from the test cases.

Current Page Objects:

- `LoginPage`
- `ProductsPage`
- `BasePage`

### Explicit Waits

The framework uses Selenium `WebDriverWait` and expected conditions instead of fixed delays.

Supported wait operations include:

- Visibility of elements
- Clickability of elements
- Presence of elements

### Reusable Base Page

The `BasePage` provides common browser interaction methods:

```text
safe_click()
safe_type()
safe_get_text()
is_visible()
```

This avoids duplicating common Selenium interaction logic across Page Objects.

### Configuration Management

Application and browser settings are maintained separately in:

```text
config/config.ini
```

Example:

```ini
[application]
base_url = https://automationexercise.com

[browser]
name = chrome
block_ads = true

[timeouts]
explicit_wait = 10
page_load_timeout = 30
```

This allows configuration values to be modified without changing the test implementation.

### CSV Test Data

Test data is maintained separately in:

```text
data/test_data.csv
```

Example:

```csv
email,search_product
YOUR_REGISTERED_EMAIL,Men Tshirt
```

PyTest parameterization is used to execute the test using the CSV data.

### Secure Credential Handling

The test password is not stored in the CSV file or source code.

It is stored locally using an environment variable:

```env
TEST_PASSWORD=YOUR_PASSWORD
```

The `.env` file is excluded from version control.

**Never commit real credentials to the repository.**

### Logging

Centralized logging is implemented using Python's `logging` module.

The framework records events such as:

- Browser startup
- Application navigation
- Login execution
- Product search
- Test failures
- Browser cleanup

### Failure Screenshots

When a test fails, the framework automatically captures a browser screenshot.

Screenshots are stored in:

```text
screenshots/
```

This provides visual evidence for debugging failed automation tests.

### HTML Reporting

The project uses `pytest-html` to generate an HTML execution report.

The report is generated in:

```text
reports/report.html
```

---

## 4. Framework Architecture

The framework follows a layered architecture:

```text
                    TEST CASES
                        │
                        ▼
                 PAGE OBJECTS
                        │
             ┌──────────┴──────────┐
             ▼                     ▼
        LoginPage            ProductsPage
             │                     │
             └──────────┬──────────┘
                        ▼
                    BasePage
                        │
             ┌──────────┴──────────┐
             ▼                     ▼
       WaitUtility           Selenium WebDriver
```

Supporting framework components:

```text
DriverFactory
ConfigReader
CSVReader
Logger
PyTest Fixtures
Failure Screenshot Handler
HTML Reporting
```

---

## 5. Project Structure

```text
02_Capstone_Project/
│
├── config/
│   └── config.ini
│
├── data/
│   └── test_data.csv
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   └── products_page.py
│
├── tests/
│   ├── test_browser.py
│   ├── test_login_search.py
│   └── test_unittest_component.py
│
├── utils/
│   ├── config_reader.py
│   ├── csv_reader.py
│   ├── driver_factory.py
│   ├── logger.py
│   └── wait_utility.py
│
├── screenshots/
│   └── Generated automatically when tests fail
│
├── reports/
│   └── report.html
│
├── logs/
│   └── execution.log
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

### Generated Files

The following directories contain runtime-generated files:

```text
reports/
screenshots/
logs/
```

They are excluded from version control using `.gitignore`.

Python cache directories such as:

```text
__pycache__/
.pytest_cache/
```

are also excluded from version control.

---

## 6. Framework Components

### 6.1 Driver Factory

File:

```text
utils/driver_factory.py
```

The Driver Factory is responsible for creating and configuring the Selenium WebDriver.

Responsibilities include:

- Creating Chrome WebDriver
- Reading browser configuration
- Configuring Chrome options
- Configuring browser notification settings
- Optional ad-related network blocking
- Setting page-load timeout

---

### 6.2 Configuration Reader

File:

```text
utils/config_reader.py
```

The Configuration Reader loads values from:

```text
config/config.ini
```

It provides methods for reading:

- String configuration values
- Integer configuration values

The configuration file is also validated before use.

---

### 6.3 Wait Utility

File:

```text
utils/wait_utility.py
```

The Wait Utility provides centralized explicit waits using Selenium's:

```python
WebDriverWait
```

and expected conditions.

Available methods:

```text
wait_for_visible()
wait_for_clickable()
wait_for_presence()
```

Centralizing waits improves consistency and reduces duplicated synchronization logic.

---

### 6.4 Base Page

File:

```text
pages/base_page.py
```

`BasePage` contains reusable browser interaction methods used by other Page Objects.

Methods include:

```text
safe_click()
safe_type()
safe_get_text()
is_visible()
```

The `safe_click()` method also provides controlled retry handling for selected transient Selenium interaction exceptions.

---

### 6.5 Login Page

File:

```text
pages/login_page.py
```

The Login Page Object manages:

- Opening the Login page
- Entering email
- Entering password
- Clicking the Login button
- Verifying successful login

---

### 6.6 Products Page

File:

```text
pages/products_page.py
```

The Products Page Object manages:

- Opening the Products page
- Entering a product search term
- Clicking the Search button
- Verifying that search results are displayed
- Verifying that the requested product appears in the results

---

### 6.7 CSV Reader

File:

```text
utils/csv_reader.py
```

The CSV Reader loads test data from:

```text
data/test_data.csv
```

The data is passed to the PyTest test through parameterization.

Example:

```csv
email,search_product
YOUR_REGISTERED_EMAIL,Men Tshirt
```

---

### 6.8 Logger

File:

```text
utils/logger.py
```

The Logger provides centralized execution logging.

Logs are written to:

```text
logs/execution.log
```

Console logging is also enabled during test execution.

---

## 7. Test Cases

### Test Case 1 — Browser Launch

File:

```text
tests/test_browser.py
```

Purpose:

- Verify that the browser launches successfully
- Open the configured application URL
- Verify the application page title

---

### Test Case 2 — Login and Product Search

File:

```text
tests/test_login_search.py
```

Purpose:

- Open the application
- Navigate to Login
- Enter user credentials
- Verify successful login
- Navigate to Products
- Search for the specified product
- Verify that search results are displayed
- Verify that the requested product appears in the search results

The test uses CSV-based test data and PyTest parameterization.

---

### Test Case 3 — Configuration Component Tests

File:

```text
tests/test_unittest_component.py
```

Purpose:

- Verify that the configured application URL is loaded correctly
- Verify that the explicit wait timeout is configured correctly

These tests demonstrate the use of Python's `unittest` framework within the automation project.

---

## 8. PyTest Fixture

File:

```text
conftest.py
```

The PyTest fixture manages the browser lifecycle.

The fixture:

1. Starts the browser before the test
2. Provides the WebDriver instance to the test
3. Detects test failures
4. Captures a screenshot when required
5. Logs execution information
6. Closes the browser after execution

This avoids duplicating browser setup and teardown code across individual tests.

---

## 9. Failure Screenshot Mechanism

The framework automatically captures a screenshot when a test fails.

The workflow is:

```text
Test Execution
      ↓
Test Failure
      ↓
PyTest Failure Detection
      ↓
Screenshot Capture
      ↓
Save Screenshot
      ↓
Browser Cleanup
```

Screenshots are saved under:

```text
screenshots/
```

Example:

```text
screenshots/
└── test_browser_launch.png
```

This feature was verified using an intentional test failure.

---

## 10. HTML Test Reporting

The framework uses the `pytest-html` plugin.

The complete test suite can be executed using:

```bash
pytest
```

The HTML report is generated at:

```text
reports/report.html
```

The report provides a consolidated view of the test execution results.

---

## 11. Installation and Setup

### Step 1 — Clone the Repository

```bash
git clone <repository-url>
```

### Step 2 — Navigate to the Project

```bash
cd Selenium-python-automation/02_Capstone_Project
```

### Step 3 — Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scriptsctivate
```

### Step 4 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5 — Configure Credentials

Create a local `.env` file inside:

```text
02_Capstone_Project/
```

Add:

```env
TEST_PASSWORD=YOUR_PASSWORD
```

Do not commit this file to GitHub.

### Step 6 — Configure Test Data

Open:

```text
data/test_data.csv
```

and provide the registered test email and desired product.

Example:

```csv
email,search_product
YOUR_REGISTERED_EMAIL,Men Tshirt
```

---

## 12. Running the Tests

### Run the complete test suite

```bash
pytest
```

### Run the browser test

```bash
pytest tests/test_browser.py -v
```

### Run the login and product search test

```bash
pytest tests/test_login_search.py -v
```

### Run the Unittest component through PyTest

```bash
pytest tests/test_unittest_component.py -v
```

---

## 13. Verified Test Execution

The final framework was successfully tested after configuration and robustness updates.

Verified execution:

```text
tests/test_browser.py::test_browser_launch PASSED
tests/test_login_search.py::test_login_and_product_search[data0] PASSED
tests/test_unittest_component.py::TestConfigReader::test_base_url_configuration PASSED
tests/test_unittest_component.py::TestConfigReader::test_explicit_wait_configuration PASSED

4 passed
```

The HTML report was also generated successfully.

Example final execution result:

```text
4 passed in 37.69s
```

---

## 14. Error Handling and Robustness

The framework includes several mechanisms to improve test reliability and maintainability:

- Explicit waits using `WebDriverWait`
- Selenium expected conditions
- Controlled retry for selected transient interaction exceptions
- Specific timeout handling
- Centralized configuration
- Browser lifecycle management
- Automatic failure screenshots
- Centralized logging
- Page Object separation
- Reusable utility classes
- Environment-based credential handling

---

## 15. Security Considerations

Test credentials are not stored directly in the source code.

The password is loaded from an environment variable:

```env
TEST_PASSWORD=YOUR_PASSWORD
```

The `.env` file is excluded from Git version control.

No real credentials should be committed to the repository.

---

## 16. Scope of the Project

This project specifically implements the requirements of:

**Capstone Assignment 2 — Selenium Python Framework Development (Unittest + PyTest + POM)**

The automated business flow covered by this implementation is:

```text
Launch Browser
      ↓
Login
      ↓
Search Product
      ↓
Verify Search Results
      ↓
Verify Requested Product
```

The framework focuses on reusable automation architecture rather than automating unrelated application functionality.

---

## 17. Conclusion

This project demonstrates the development of a reusable Selenium Python automation framework using:

- Selenium WebDriver
- PyTest
- Unittest
- Page Object Model
- Utility Classes
- Configuration Management
- CSV Test Data
- Explicit Waits
- Exception Handling
- Logging
- Failure Screenshots
- HTML Reporting

The framework separates test logic, page-specific operations, configuration, test data, browser management, synchronization, and reporting into dedicated components.

This structure improves maintainability, reusability, readability, and reliability of Selenium automation tests.

---

## 18. Author

**Pratyay Chowdhury**

B.Tech Computer Science and Engineering  
Specialization: Artificial Intelligence  
Institute of Engineering and Management, Kolkata
