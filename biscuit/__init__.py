from biscuit.app import app
from biscuit.command.biscuit_shell import biscuit_shell


app.register_blueprint(biscuit_shell)
