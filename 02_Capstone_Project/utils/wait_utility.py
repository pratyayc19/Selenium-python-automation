from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.config_reader import ConfigReader


class WaitUtility:

    def __init__(self, driver):
        self.driver = driver
        self.config = ConfigReader()

        timeout = self.config.get_int("timeouts", "explicit_wait")
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_presence(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )