from biscuit.command.internal.commands.abstract_command import AbstractCommand


class ReceivePackCommand(AbstractCommand):

    def __init__(self, args, config, io):
        AbstractCommand.__init__(self, args, config, io)

    def execute(self):
        out_format = self.config()['shell']['out-format']
        print(out_format['git-receive-pack-checking-permission'] %
              (self.username(), self._args.repo_name()),
              file=self._io.error())
        # TODO checking permission of user in repo
