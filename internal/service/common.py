INTERNAL_API_PATH = '/api/v1/internal'
CONFIG_API_SECRET_KEY = 'internal-api-secret'


class ServiceSide:
    def __init__(self, config):
        self._config = config


def normalize_path(path):
    if not path.startswith('/'):
        path = '/' + path
    if not path.startswith(INTERNAL_API_PATH):
        path = INTERNAL_API_PATH + path
    return path
