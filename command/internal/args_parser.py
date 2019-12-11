from biscuit.command.internal.args.shell_args import ShellArgs
from biscuit.command.internal.args.receive_pack import GIT_RECEIVE_PACK
from biscuit.command.internal.args.receive_pack import ReceivePackArgs

SPEC_ARGS = {
    GIT_RECEIVE_PACK: lambda args: ReceivePackArgs(args)
}


def args_parse(executable, io):
    args = ShellArgs(executable)
    if not args.parse():
        print('shell parse failed.', file=io.error())
        return None
    if args.command_type() not in SPEC_ARGS:
        print('command not registered.', file=io.error())
        return None
    args = SPEC_ARGS[args.command_type()](args)
    if not args.parse():
        print('illegal command parameter.', file=io.error())
        return None
    return args
