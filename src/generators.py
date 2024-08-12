from typing import Iterator

from src.tools import extract


def filter_by_currency(data: list, currency: str) -> Iterator:
    """Yields filtered by currency code operations

    :param data: list of operations in dictionaries
    :param currency: string of currency code"""
    path = ("operationAmount", "currency", "code")
    for op in data:
        actual_currency = extract(op, path)
        if actual_currency == currency:
            yield op


def transaction_descriptions(data: list) -> Iterator:
    """Yields descriptions of operations,
    returns None if arguments are not instance of expected types

    :param data: list of operations in dictionaries"""
    for op in data:
        if not isinstance(op, dict) or "description" not in op.keys():
            continue
        yield op["description"]


def card_number_generator(start: int = 1, stop: int = 10**16 - 1) -> Iterator:
    """Yields card numbers ∈ [start, stop) increasing by 1,
    returns None if breaks or ends

    :param start: integer, 0 < start < 10 ** 16 - 1, default 1
    :param stop: integer, start < stop < 10 ** 16, default 10 ** 16 - 1"""
    current = start
    while current < stop:
        to_yield = str(current)
        to_yield = (16 - len(to_yield)) * "0" + to_yield
        to_yield = to_yield[:4] + " " + to_yield[4:8] + " " + to_yield[8:12] + " " + to_yield[12:]
        yield to_yield
        current += 1
