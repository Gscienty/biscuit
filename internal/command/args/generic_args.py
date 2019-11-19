from internal.command.args.__init__ import CommandArgs


class GenericArgs(CommandArgs):
    def __init__(self, arguments):
        self._arguments = arguments

    def parse(self):
        return True

    def arguments(self):
        return self._arguments
