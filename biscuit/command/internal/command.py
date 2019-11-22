from abc import abstractmethod, ABCMeta


class Command(metaclass=ABCMeta):
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
