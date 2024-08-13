import json
from json import JSONDecodeError

from src.external_api import convert_to_rub
from src.tools import extract


def read_json_local(path: str) -> list[dict]:
    """Gets .json file path, returns list of transactions
    (empty list if file not found or doesn't contain list)

    :param path: .json file path
    :return: list of transactions"""
    to_return = []
    try:
        with open(path, "r") as file:
            transactions = json.load(file)
            if isinstance(transactions, list):
                if sum([isinstance(x, dict) for x in transactions]) == len(transactions):
                    to_return = transactions
    except JSONDecodeError:
        pass
    except FileNotFoundError:
        pass
    return to_return


def get_rub_amount(data: dict) -> float:
    """Gets amount out of transaction, converts it to RUB if necessary
    using date of transaction

    :param data: transaction dict
    :return: amount in RUB"""
    cur = extract(
        data,
        (
            "operationAmount",
            "currency",
            "code",
        ),
    )

    amount = extract(
        data,
        (
            "operationAmount",
            "amount",
        ),
    )
    amount = float(amount)

    if cur == "RUB":
        return amount
    else:
        try:
            date = extract(data, ("date",))
            date = date[:10]
            return convert_to_rub(amount, cur, date)
        except Exception as ex:
            # don't sure it should be that way,
            # but for now I decide to just throw it up
            raise ex
