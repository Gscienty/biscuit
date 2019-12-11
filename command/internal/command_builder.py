from biscuit.command.internal.args_parser import args_parse
from biscuit.command.internal.args.receive_pack import GIT_RECEIVE_PACK
from biscuit.command.internal.commands.receive_pack import ReceivePackCommand
from biscuit.config import Config

SPEC_COMMANDS = {
    GIT_RECEIVE_PACK: ReceivePackCommand
}


def build_command(executable, io):
    args = args_parse(executable, io)
    if args is None:
        return None
    command_type = args.command_type()
    if command_type not in SPEC_COMMANDS:
        print('illegal command', file=io.error())
        return None
    home = executable.home()
    return SPEC_COMMANDS[command_type](args, Config(home), io)
