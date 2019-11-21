import sys
from internal.io import IO
from internal.executable import Executable
from internal.config import Config
from internal.command import command_new


if __name__ == '__main__':
    io = IO(sys.stdin, sys.stdout, sys.stderr)
    executable = Executable()
    config = Config(executable.home())
    if not config.load():
        exit(1)
    command = command_new(executable, sys.argv[1:], config, io)
    command.execute()
