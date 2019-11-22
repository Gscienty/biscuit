from biscuit.command.internal.args.shell_args import ShellArgs
from biscuit.command.internal.args.receive_pack import GIT_RECEIVE_PACK
from biscuit.command.internal.args.receive_pack import ReceivePackArgs


def args_parse(executable):
    spec_factory = {
        GIT_RECEIVE_PACK: lambda args: ReceivePackArgs(args)
    }
    args = ShellArgs()
    if not args.parse():
        return None
    if args.command_type() not in spec_factory:
        print(args.command_type())
        return None
    args = spec_factory[args.command_type()](args)
    if not args.parse():
        return None
    return args
