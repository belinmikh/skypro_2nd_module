from collections import Counter
from typing import Iterable

from src.tools import extract


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


def filter_by_description(data: list[dict], incl: str) -> list[dict]:
    """Returns selected data as list of dictionaries
    which 'description' option contains incl string as a substring;
    case doesn't matter

    :param data: list of dictionaries
    :param incl: string needs to be included
    :return: filtered list of dictionaries"""
    if not isinstance(incl, str) or not isinstance(data, list):
        raise ValueError
    to_return = []
    for elem in data:
        check = extract(elem, ("description",))
        if isinstance(check, str):
            check = check.lower().strip()
            if incl.lower().strip() in check:
                to_return.append(elem)
    return to_return


def sort_by_date(data: Iterable[dict], reverse: bool = True) -> Iterable[dict] | None:
    """Returns data as list of dictionaries
    ordered by its date and time, descending by default,
    None if data is not a list of dictionaries with correct date or reverse is not bool

    :param data: list of dictionaries with operations
    :param reverse: boolean, default: True (descending)
    :return: ordered by date and time list of dictionaries with operations"""
    # if not isinstance(data, list) or not isinstance(reverse, bool):
    #     return None
    # for item in data:
    #     if not isinstance(item, dict) or "date" not in item.keys() or get_date(item["date"]) is None:
    #         return None
    # calling get_date() here is for right type of date and time checking
    dict_date = lambda elem: extract(elem, ("date",)) if isinstance(extract(elem, ("date",)), str) else ""
    return sorted(data, key=dict_date, reverse=reverse)


def count_by_categories(data: list[dict]) -> dict[str, int]:
    """Counts categories in transactions

    :param data: transactions in list of dictionaries
    :return: dictionary in {category: number of transactions} formatted"""
    to_count = [
        extract(t, ("description",)) if isinstance(extract(t, ("description",)), str) else "Описание отсутствует"
        for t in data
    ]
    counter = Counter(to_count)
    return dict(counter)
