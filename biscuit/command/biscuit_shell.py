import sys
from flask import Blueprint
import click
from biscuit.command.internal.io import IO
from biscuit.command.internal.executable import Executable
from biscuit.command.internal.config import Config
from biscuit.command.internal.args.receive_pack import GIT_RECEIVE_PACK
from biscuit.command.internal.args_parser import args_parse
from biscuit.command.receive_pack import ReceivePackCommand


def __build_command(executable, args, config, io):
    spec_commands = {
        GIT_RECEIVE_PACK: lambda: ReceivePackCommand(args, config, io)
    }
    if args.command_type() is None:
        return None
    if args.command_type() not in spec_commands:
        return None
    return spec_commands[args.command_type()]()


def command_new(executable, config, io):
    args = args_parse(executable)
    if args is None:
        return None
    return __build_command(executable, args, config, io)


biscuit_shell = Blueprint('biscuit_shell', __name__)


@biscuit_shell.cli.command('shell')
@click.argument('username')
@click.argument('key_id')
def do_biscuit_shell(username, key_id):
    io = IO(sys.stdin, sys.stdout, sys.stderr)
    executable = Executable()
    config = Config(executable.home())
    if not config.load():
        exit(1)
    command = command_new(executable, config, io)
    if command is None:
        exit(1)
    command.set_account_info(username, key_id)
    command.execute()
