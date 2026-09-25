import unittest

from utils.config_reader import ConfigReader


class TestConfigReader(unittest.TestCase):

    def test_base_url_configuration(self):

        config = ConfigReader()

        base_url = config.get(
            "application",
            "base_url"
        )

        self.assertEqual(
            base_url,
            "https://automationexercise.com"
        )

    def test_explicit_wait_configuration(self):

        config = ConfigReader()

        timeout = config.get_int(
            "timeouts",
            "explicit_wait"
        )

        self.assertGreater(
            timeout,
            0
        )


if __name__ == "__main__":
    unittest.main()