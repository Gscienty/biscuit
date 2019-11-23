import hashlib


def check_require_fields(json, require_fields):
    for field in require_fields:
        if field not in json:
            return False
    return True


def calc_hashed_password(salt, password):
    hash_ = hashlib.sha256()
    hash_.update(salt.encode())
    hash_.update(password.encode())
    return hash_.hexdigest()
