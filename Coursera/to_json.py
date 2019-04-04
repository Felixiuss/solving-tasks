from functools import wraps
from json import dumps


def to_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = dumps(func(*args, **kwargs))
        return result

    return wrapper


@to_json
def get_data():
    return {
        'name': 'Roman',
        'age': 35,
        'wight': 75
    }


if __name__ == '__main__':
    assert get_data() == '{"name": "Roman", "age": 35, "wight": 75}'
    print(get_data())
d