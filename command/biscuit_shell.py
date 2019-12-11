import sys
import click
from biscuit.executable import Executable
from biscuit.io import IO
from biscuit.command.internal.command_builder import build_command


@click.command()
@click.argument('username')
@click.argument('key_id')
def do_biscuit_shell(username, key_id):
    io = IO(sys.stdin, sys.stdout, sys.stderr)
    executable = Executable()
    command = build_command(executable, io)
    if command is None:
        exit(1)
    command.set_account_info(username, key_id)
    command.execute()


if __name__ == '__main__':
    do_biscuit_shell()
