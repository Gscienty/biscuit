from flask import (
    Blueprint,
    request,
    jsonify
)
from biscuit.service.business.util import check_require_fields
from biscuit.service.business.user import (
    user_exist,
    user_add
)

user_mod = Blueprint('biscuit_server_user',
                     __name__,
                     url_prefix='/api/v1/user')


@user_mod.route('/register', methods=['POST'])
def do_user_register():
    if not check_require_fields(request.json, [
        'username',
        'password'
    ]):
        return jsonify({
            'status': 'error',
            'reason': 'Bad Request'
        }), 400
    if user_exist(request.json['username']):
        return jsonify({
            'status': 'error',
            'reason': 'Conflict'
        }), 409
    if not user_add(request.json['username'], request.json['password']):
        return jsonify({
            'reason': 'Service Unavailable'
        }), 503
    return jsonify({
        'status': 'success',
        'reason': 'Created'
    }), 201
