from typing import Callable, Iterable


def filter_by_state(data: Iterable[dict], state: str = "EXECUTED") -> Iterable[dict] | None:
    """Returns selected data as list of dictionaries
    which 'state' option is equal to state string (default: 'EXECUTED'),
    returns None if input data is not a list or state is not a string

    :param data: list of dictionaries with operations
    :param state: filtration parameter
    :return: filtered list of operations
    """
    if not isinstance(state, str) or not isinstance(data, list):
        return None
    to_return = []
    for elem in data:
        if not isinstance(elem, dict):
            continue
        if "state" in elem.keys() and elem["state"] == state:
            to_return.append(elem)
    return to_return
