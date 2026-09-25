from utils.config_reader import ConfigReader


config = ConfigReader()
BASE_URL = config.get("application", "base_url")


def test_browser_launch(driver):

    driver.get(BASE_URL)

    assert "Automation Exercise" in driver.title