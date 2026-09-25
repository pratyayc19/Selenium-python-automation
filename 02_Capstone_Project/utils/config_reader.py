import configparser
from pathlib import Path


class ConfigReader:

    def __init__(self):

        config_path = (
            Path(__file__).resolve().parent.parent
            / "config"
            / "config.ini"
        )

        if not config_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {config_path}"
            )

        self.config = configparser.ConfigParser()
        self.config.read(config_path)

    def get(self, section, key):
        return self.config.get(section, key)

    def get_int(self, section, key):
        return self.config.getint(section, key)