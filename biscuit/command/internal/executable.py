import os

HOME = os.environ.get('BISCUIT_HOME')


class Executable:
    def __init__(self):
        self._home = HOME

    def home(self):
        return self._home
