from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
    TimeoutException,
)

from utils.wait_utility import WaitUtility


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitUtility(driver)

    def safe_click(self, locator):
        """
        Wait until an element is clickable and then click it.
        Retries once for transient Selenium interaction issues.
        """
        for attempt in range(2):
            try:
                element = self.wait.wait_for_clickable(locator)
                element.click()
                return
            except (
                StaleElementReferenceException,
                ElementClickInterceptedException,
            ):
                if attempt == 1:
                    raise

    def safe_type(self, locator, text):
        """
        Wait until an element is visible, clear it and enter text.
        """
        element = self.wait.wait_for_visible(locator)
        element.clear()
        element.send_keys(text)

    def safe_get_text(self, locator):
        """
        Wait until an element is visible and return its text.
        """
        element = self.wait.wait_for_visible(locator)
        return element.text

    def is_visible(self, locator):
        """
        Return True if the element becomes visible within the configured wait.
        """
        try:
            self.wait.wait_for_visible(locator)
            return True
        except TimeoutException:
            return False