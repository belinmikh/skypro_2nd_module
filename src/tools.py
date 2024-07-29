from typing import Any


def extract(dictionary: dict, _path: tuple) -> Any:
    # To determine recursion...
    #                 ... you should determine recursion
    """Returnable value is returnable value of returnable value of returnable value of...

    Sorry. Just tries to get nested in dict data. None otherwise

    :param dictionary: dict
    :param _path: tuple of anything that could be a key"""
    if not isinstance(dictionary, dict):
        return None
    if not isinstance(_path, tuple):
        return None
    for p in _path:
        if p not in dictionary.keys():
            return None
        if isinstance(dictionary[p], dict) and len(_path) > 1:
            return extract(dictionary[p], tuple(_path[1:]))
        else:
            return dictionary[p]
