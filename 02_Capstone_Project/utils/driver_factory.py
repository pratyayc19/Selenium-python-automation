from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utils.config_reader import ConfigReader


class DriverFactory:

    @staticmethod
    def create_driver():

        config = ConfigReader()
        browser = config.get("browser", "name").lower()

        if browser == "chrome":

            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            options.page_load_strategy = "eager"

            # Block browser notification prompts
            prefs = {
                "profile.default_content_setting_values.notifications": 2,
                "profile.default_content_setting_values.popups": 0,
            }

            options.add_experimental_option(
                "prefs",
                prefs
            )

            driver = webdriver.Chrome(
                service=Service(
                    ChromeDriverManager().install()
                ),
                options=options
            )

            # Optional ad blocking
            block_ads = config.get(
                "browser",
                "block_ads"
            ).lower() == "true"

            if block_ads:

                blocked_urls = [
                    "*doubleclick.net/*",
                    "*googlesyndication.com/*",
                    "*googleadservices.com/*",
                    "*adservice.google.com/*",
                    "*googletagmanager.com/*",
                    "*google-analytics.com/*",
                ]

                driver.execute_cdp_cmd(
                    "Network.setBlockedURLs",
                    {
                        "urls": blocked_urls
                    }
                )

                driver.execute_cdp_cmd(
                    "Network.enable",
                    {}
                )

        else:
            raise ValueError(
                f"Unsupported browser: {browser}"
            )

        page_load_timeout = config.get_int(
            "timeouts",
            "page_load_timeout"
        )

        driver.set_page_load_timeout(
            page_load_timeout
        )

        return driver