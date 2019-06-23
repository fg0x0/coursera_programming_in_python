from functools import wraps
import json


def to_json(f):
    """Сериализует возврат функции в json"""
    @wraps(f)
    def wrapped(*args, **kwargs):
        return json.dumps(f(*args, **kwargs))
    return wrapped
