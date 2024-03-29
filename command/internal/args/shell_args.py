import os


class ShellParserStatus:
    def __init__(self):
        self.args = []
        self.buf = ''
        self.esc = False
        self.double_quo = False
        self.single_quo = False
        self.back_quo = False
        self.dollar_quo = False
        self.backtick = ''
        self.pos = -1
        self.got = False

    def parse_esc(self, r):
        self.buf += r
        self.esc = False

    def parse_transfer_mean(self, r):
        if self.single_quo:
            self.buf += r
        else:
            self.esc = True

    def parse_space(self, r):
        if True in [
            self.single_quo,
            self.double_quo,
            self.back_quo,
            self.dollar_quo
        ]:
            self.buf += r
            self.backtick += r
        elif self.got:
            self.args.append(self.buf)
            self.buf = ''
            self.got = False

    def parse_back_quo(self):
        if False not in [
            not self.single_quo,
            not self.double_quo,
            not self.dollar_quo
        ]:
            self.backtick = ''
            self.back_quo = not self.back_quo

    def parse_rbracket(self):
        if False not in [
            not self.single_quo,
            not self.double_quo,
            not self.back_quo
        ]:
            self.backtick = ''
            self.dollar_quo = not self.dollar_quo

    def parse_bracket(self):
        if False not in [
            not self.single_quo,
            not self.double_quo,
            not self.back_quo
        ]:
            if not self.dollar_quo and self.buf.startswith('$'):
                self.dollar_quo = True
                self.buf += '('
                return True
            else:
                return False

    def parse_double_quo(self):
        if False not in [
            not self.single_quo,
            not self.dollar_quo,
        ]:
            self.double_quo = not self.double_quo

    def parse_single_quo(self):
        if False not in [
            not self.double_quo,
            not self.dollar_quo,
        ]:
            self.single_quo = not self.single_quo


class ShellParser:
    def __init__(self):
        self._parse_env = False
        self._parse_backtick = False
        self._position = 0
        self._dir = ''

    def parse(self, line):
        status = ShellParserStatus()
        ctrl_char = {
            '\\': lambda status: status.parse_back_quo(),
            ')': lambda status: status.parse_rbracket(),
            '"': lambda status: status.parse_double_quo(),
            '\'': lambda status: status.parse_single_quo()
        }
        for r in line:
            if status.esc:
                status.parse_esc(r)
                continue
            if r == '\\':
                status.parse_transfer_mean(r)
                continue
            if self.__is_space(r):
                status.parse_space(r)
                continue
            if r == '(':
                if status.parse_bracket():
                    continue
                else:
                    return []
            if r in ctrl_char:
                ctrl_char[r](status)
            status.got = True
            status.buf += r
            if status.back_quo or status.dollar_quo:
                status.backtick += r
        if status.got:
            status.args.append(status.buf)
        return status.args

    def __is_space(self, r):
        return r == ' ' or r == '\t' or r == '\r' or r == '\n'


class ShellArgs:
    def __init__(self, executable):
        self._ssh_args = []
        self._cmd_type = None
        self._is_ssh_connection = executable.is_ssh_connection()
        self._command = executable.command()

    def ssh_arguments(self):
        return self._ssh_args

    def command_type(self):
        return self._cmd_type

    def parse(self):
        if not self.__valid():
            return False
        self.__parse_command()
        if len(self._ssh_args) >= 1:
            self._cmd_type = self._ssh_args[0]
        return True

    def __valid(self):
        return self._is_ssh_connection and self._command is not None

    def __parse_command(self):
        args = ShellParser().parse(os.environ.get('SSH_ORIGINAL_COMMAND'))
        if len(args) > 1 and args[0] == 'git':
            cmd = '%s-%s' % (args[0], args[1])
            args = [cmd] + args[2:]
        self._ssh_args = args
