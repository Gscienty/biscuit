from biscuit.command.internal.command import Command
from biscuit.command.internal.args.receive_pack import GIT_RECEIVE_PACK


class ReceivePackCommand(Command):
    def __init__(self, args, config, io):
        self._config = config
        self._args = args
        self._io = io

    def execute(self):
        if self._args.command_type() != GIT_RECEIVE_PACK:
            print('biscuit internal error', file=self._io.error())
            exit(1)
        # TODO
