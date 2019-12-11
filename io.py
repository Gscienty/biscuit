import sys


class IO:
    def __init__(self,
                 input=sys.stdin,
                 output=sys.stdout,
                 error=sys.stderr):
        self._in = input
        self._out = output
        self._err = error

    def input(self):
        return self._in

    def output(self):
        return self._out

    def error(self):
        return self._err
