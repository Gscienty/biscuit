from biscuit.command.internal.executable import Executable
from biscuit.config import Config
from flask import Flask

app = Flask(__name__)
executable = Executable()
config = Config(executable.home())
if not config.load():
    exit(1)
