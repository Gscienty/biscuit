import sys
from biscuit.config import Config
from biscuit.executable import Executable
from biscuit.io import IO
from biscuit.ipc_server.scene.repo import repo_blueprint
from flask import Flask


app = Flask(__name__)
executable = Executable()
config = Config(executable.home())
io = IO(sys.stdin, sys.stdout, sys.stderr)

app.register_blueprint(repo_blueprint)
