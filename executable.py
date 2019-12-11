import os

HOME = os.environ.get('BISCUIT_HOME')
SSH_CONNECTION = os.environ.get('SSH_CONNECTION')
SSH_ORIGINAL_COMMAND = os.environ.get('SSH_ORIGINAL_COMMAND')


class Executable:
    def __init__(self):
        self._home = HOME
        self._is_ssh_connection = SSH_CONNECTION is not None
        self._command = SSH_ORIGINAL_COMMAND

    def home(self):
        return self._home

    def is_ssh_connection(self):
        return self._is_ssh_connection

    def command(self):
        return self._command
