from internal.command.args.__init__ import CommandArgs


class AuthPrincArgs(CommandArgs):
    def __init__(self, arguments):
        self._arguments = arguments
        self._key_id = ''
        self._principals = []

    def arguments(self):
        return self._arguments

    def parse(self):
        if not self.__valid():
            return False
        self._key_id = self._arguments[0]
        self._principals = self._arguments[1:]
        return True

    def __valid(self):
        if len(self._arguments) < 2:
            return False
        return '' not in self._arguments
