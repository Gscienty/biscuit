from internal.command.args.__init__ import CommandArgs


class AuthKeyArgs(CommandArgs):
    def __init__(self, arguments):
        self._arguments = arguments
        self._expect_user = ''
        self._actual_user = ''
        self._key = ''

    def arguments(self):
        return self._arguments

    def parse(self):
        if not self.__valid():
            return False
        self._expect_user = self._arguments[0]
        self._acutal_user = self._arguments[1]
        self._key = self._arguments[2]
        return True

    def __valid(self):
        if len(self._arguments) != 3:
            return False
        return '' not in self._arguments
