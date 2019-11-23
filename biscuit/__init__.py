from flask_mongoengine import MongoEngine
from biscuit.app import app, config
from biscuit.command.biscuit_shell import biscuit_shell
from biscuit.service.user import user_mod


if 'server_mongo' in config.config():
    app.config['MONGODB_SETTINGS'] = config.config()['server_mongo']
    MongoEngine(app)

app.register_blueprint(biscuit_shell)
app.register_blueprint(user_mod)
