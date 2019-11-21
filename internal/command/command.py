from abc import abstractmethod, ABCMeta


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute():
        pass
