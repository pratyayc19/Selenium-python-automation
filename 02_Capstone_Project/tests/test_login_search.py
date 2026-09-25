import os

import pytest
from dotenv import load_dotenv

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.config_reader import ConfigReader
from utils.csv_reader import CSVReader
from utils.logger import Logger


load_dotenv()

logger = Logger.get_logger()
config = ConfigReader()

BASE_URL = config.get("application", "base_url")

test_data = CSVReader.read_test_data()

password = os.getenv("TEST_PASSWORD")

assert password, "TEST_PASSWORD is not configured"


@pytest.mark.parametrize("data", test_data)
def test_login_and_product_search(driver, data):

    logger.info("Opening AutomationExercise")

    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)

    logger.info("Opening login page")

    login_page.open_login_page()

    logger.info("Logging in")

    login_page.login(
        data["email"],
        password
    )

    assert login_page.is_logged_in(), (
        "Login was not successful"
    )

    logger.info("Login successful")

    products_page.open_products_page()

    logger.info(
        f"Searching for product: {data['search_product']}"
    )

    products_page.search_product(
        data["search_product"]
    )

    assert products_page.is_search_results_displayed(), (
        "Search results were not displayed"
    )

    assert products_page.is_product_displayed(
        data["search_product"]
    ), (
        f"Product '{data['search_product']}' "
        "was not found in search results"
    )

    logger.info("Product search successful")