from typing import Iterable

from src.widget import get_date


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


def sort_by_date(data: Iterable[dict], reverse: bool = True) -> Iterable[dict] | None:
    """Returns data as list of dictionaries
    ordered by its date and time, descending by default,
    None if data is not a list of dictionaries with correct date or reverse is not bool

    :param data: list of dictionaries with operations
    :param reverse: boolean, default: True (descending)
    :return: ordered by date and time list of dictionaries with operations"""
    if not isinstance(data, list) or not isinstance(reverse, bool):
        return None
    for item in data:
        if not isinstance(item, dict) or "date" not in item.keys() or get_date(item["date"]) is None:
            return None
    # calling get_date() here is for right type of date and time checking
    dict_date = lambda elem: elem["date"]
    return sorted(data, key=dict_date, reverse=reverse)
