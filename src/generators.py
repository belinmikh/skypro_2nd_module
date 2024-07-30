from src.tools import extract


def filter_by_currency(data: list, currency: str) -> None:
    """Yields filtered by currency code operations,
    returns None if arguments are not instance of expected types

    :param data: list of operations in dictionaries
    :param currency: string of currency code
    :return: None if breaks or ends"""
    if not isinstance(data, list) or not isinstance(currency, str):
        return None
    path = ("operationAmount", "currency", "code")
    for op in data:
        actual_currency = extract(op, path)
        if actual_currency == currency:
            yield op
    return None


def transaction_descriptions(data: list) -> None:
    """Yields descriptions of operations,
    returns None if arguments are not instance of expected types

    :param data: list of operations in dictionaries
    :return: None if breaks or ends"""
    if not isinstance(data, list):
        return None
    for op in data:
        if not isinstance(op, dict) or "description" not in op.keys():
            continue
        yield op["description"]
    return None


def card_number_generator(start: int = 1, stop: int = 10 ** 16 - 1) -> None:
    """Yields card numbers ∈ [start, stop) increasing by 1,
    returns None if breaks or ends

    :param start: integer, 0 < start < 10 ** 16 - 1, default 1
    :param stop: integer, start < stop < 10 ** 16, default 10 ** 16 - 1"""
    if not isinstance(start, int) or not 0 < start < 10 ** 16 - 1:
        return None
    if not isinstance(stop, int) or not start < stop < 10 ** 16:
        return None
    current = start
    while current < stop:
        to_yield = str(current)
        to_yield = (16 - len(to_yield)) * '0' + to_yield
        to_yield = (to_yield[:4] + " "
                    + to_yield[4:8] + " "
                    + to_yield[8:12] + " "
                    + to_yield[12:])
        yield to_yield
        current += 1
    return None
