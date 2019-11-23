from biscuit.service.business.util import calc_hashed_password
from biscuit.service.schema.user import User


def user_exist(username):
    return User.objects(username=username).first() is not None


def user_add(username, password):
    User(
        username=username,
        password=calc_hashed_password(username, password),
        is_available=True
    ).save()
    return True
