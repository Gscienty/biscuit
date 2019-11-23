def check_require_fields(json, require_fields):
    for field in require_fields:
        if field not in json:
            return False
    return True
