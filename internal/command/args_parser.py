from internal.command.args.shell_args import ShellArgs
from internal.command.args.auth_key_args import AuthKeyArgs
from internal.command.args.auth_princ_args import AuthPrnicArgs
from internal.command.args.generic_args import GenericArgs
from internal.executable import SHELL
from internal.executable import AUTHORIZED_KEYS_CHECK
from internal.executable import AUTHORIZED_PRINC_CHECK


def args_parse(executable, arguments):
    args = GenericArgs(arguments)
    if executable.name() == SHELL:
        args = ShellArgs(arguments)
    elif executable.name() == AUTHORIZED_KEYS_CHECK:
        args = AuthKeyArgs(arguments)
    elif executable.name() == AUTHORIZED_PRINC_CHECK:
        args = AuthPrincArgs(arguments)
    if not args.parse():
        return []
    return args

