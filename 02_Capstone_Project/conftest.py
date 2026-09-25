import pytest
from pathlib import Path

from utils.driver_factory import DriverFactory
from utils.logger import Logger


logger = Logger.get_logger()


@pytest.fixture
def driver(request):

    logger.info("Starting browser session")

    driver = DriverFactory.create_driver()

    yield driver

    # Capture screenshot if the test failed
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:

        screenshot_directory = (
            Path(__file__).resolve().parent / "screenshots"
        )

        screenshot_directory.mkdir(exist_ok=True)

        screenshot_path = (
            screenshot_directory
            / f"{request.node.name}.png"
        )

        driver.save_screenshot(str(screenshot_path))

        logger.error(
            f"Test failed. Screenshot saved at: {screenshot_path}"
        )

    logger.info("Closing browser session")

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    setattr(
        item,
        f"rep_{report.when}",
        report
    )