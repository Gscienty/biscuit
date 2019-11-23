import hashlib
from biscuit.service.schema.user import User


def user_exist(username):
    return User.objects(username=username).first() is not None


def user_add(username, password):
    hash_ = hashlib.sha256()
    hash_.update(username.encode())
    hash_.update(password.encode())
    hashed_password = hash_.hexdigest()
    User(
        username=username,
        password=hashed_password,
        is_available=True
    ).save()
    return True
