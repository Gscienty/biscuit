from abc import abstractmethod, ABCMeta


class CommandArgs(metaclass=ABCMeta):
    @abstractmethod
    def parse(self):
        pass

    @abstractmethod
    def arguments(self):
        pass
