from biscuit.command.internal.args.common import CommandArgs

GIT_RECEIVE_PACK = 'git-receive-pack'


class ReceivePackArgs(CommandArgs):
    def __init__(self, shell_args):
        self._arguments = shell_args.ssh_arguments()
        self._repo_name = None

    def arguments(self):
        return self._arguments

    def command_type(self):
        return GIT_RECEIVE_PACK

    def repo_name(self):
        return self._repo_name

    def parse(self):
        if len(self._arguments) != 2:
            return False
        self._repo_name = self._arguments[1][1:-1]
        return True
