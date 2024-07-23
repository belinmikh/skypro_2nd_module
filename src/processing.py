from typing import Callable, Iterable

from src.widget import get_date


def filter_by_state(data: Iterable[dict], state: str = "EXECUTED") -> Iterable[dict] | None:
    """Returns selected data as list of dictionaries
    which 'state' option is equal to state string (default: 'EXECUTED'),
    returns None if input data is not a list or state is not a string"""
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
    if not isinstance(data, list):
        return None
    # calling get_date() here is for right type of date and time checking
    dict_date: Callable[[dict], str | None] = lambda elem: (
        elem["date"] if "date" in elem.keys() and not get_date(elem["date"]) is None else None
    )
    return sorted(data, key=dict_date, reverse=reverse)
