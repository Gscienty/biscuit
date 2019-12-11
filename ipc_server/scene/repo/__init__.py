from flask import Blueprint
from biscuit.ipc_server.scene.repo.check_permission import check_permission


repo_blueprint = Blueprint('repo', __name__, url_prefix='/repo')


@repo_blueprint.route('/check-permission', methods=['GET'])
def do_check_permission(): return check_permission()
