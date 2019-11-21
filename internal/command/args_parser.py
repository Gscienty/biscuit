from internal.command.args.shell_args import ShellArgs


def args_parse(executable, arguments):
    args = ShellArgs(arguments)
    if not args.parse():
        return None
    return args
