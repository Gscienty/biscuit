import os
import yaml

CONFIG_FILENAME = '.biscuit-config.yml'


class Config:
    def __init__(self, home):
        self._home = home

    def load(self):
        if self._home is None:
            return False
        config_file_path = os.path.join(self._home, CONFIG_FILENAME)
        if not os.path.exists(config_file_path):
            return False
        with open(config_file_path, 'r') as config_file:
            config_content = config_file.read()
            self._config = yaml.load(config_content, Loader=yaml.FullLoader)
        return True

    def config(self):
        return self._config
