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


def output(*args: Any, filename: str = "", sep: str = " ", end: str = "\n") -> None:
    """Outputs *args to console by default, to file if got filename

    :param args: data to output
    :param sep: data separator
    :param end: ends data flow with
    :param filename: name of file ('a' mod)"""
    if not (isinstance(filename, str) and isinstance(sep, str) and isinstance(end, str)):
        raise ValueError
    if filename == "":
        print(*args, sep=sep, end=end)
    else:
        with open(filename, "a", encoding="UTF-8") as file:
            file.write(sep.join(list(map(str, args))) + end)
    return None
