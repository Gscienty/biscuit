import os
from internal.command.command import Command


class ReceivePackCommand(Command):
    def __init__(self, args, config, io):
        self._config = config
        self._args = args
        self._io = io

    def execute(self):
        os.system(' '.join(self._args.ssh_arguments()))
