from abc import abstractmethod, ABCMeta


class AbstractCommand(metaclass=ABCMeta):

    def __init__(self, args, config, io):
        self._args = args
        self._config = config
        self._io = io
        self._legal_config = config.load()

    @abstractmethod
    def execute(self):
        pass

    def set_account_info(self, username, key_id):
        self._username = username
        self._key_id = key_id

    def username(self):
        return self._username

    def key_id(self):
        return self._key_id

    def config(self):
        if not self._legal_config:
            return {}
        return self._config.config()
