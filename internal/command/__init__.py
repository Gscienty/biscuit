from internal.command.args_parser import args_parse
from internal.command.receive_pack import ReceivePackCommand


def __build_command(executable, args, config, io):
    return ReceivePackCommand(args, config, io)


def command_new(executable, arguments, config, io):
    args = args_parse(executable, arguments)
    return __build_command(executable, args, config, io)
