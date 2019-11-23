from flask import (
    Blueprint,
    request
)
from biscuit.service.business.common_response import (
    bad_request,
    not_found,
    created,
    conflict,
    service_unavailable,
    method_not_allowed
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
    if not check_require_fields(request.json, ['username', 'password']):
        return bad_request()
    if user_exist(request.json['username']):
        return conflict()
    if not user_add(request.json['username'], request.json['password']):
        return service_unavailable()
    return created()


def __do_user_email_add():
    if not check_require_fields(request.json, ['username', 'email']):
        return bad_request()
    if not user_exist(request.json['username']):
        return not_found()
    return created()


@user_mod.route('/email', methods=['GET', 'POST', 'DELETE'])
def do_user_email():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        return __do_user_email_add()
    elif request.method == 'DELETE':
        pass
    return method_not_allowed()
