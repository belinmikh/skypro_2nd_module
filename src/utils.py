import json

from src.external_api import convert_to_rub
from src.loggers import create_basic_logger
from src.tools import extract

logger = create_basic_logger(__name__)


def read_json_local(path: str) -> list[dict]:
    """Gets .json file path, returns list of transactions
    (empty list if file not found or doesn't contain list)

    :param path: .json file path
    :return: list of transactions"""
    logger.debug("read_json_local called")
    to_return = []
    try:
        with open(path, "r") as file:
            transactions = json.load(file)
            if isinstance(transactions, list):
                if sum([isinstance(x, dict) for x in transactions]) == len(transactions):
                    to_return = transactions
        logger.info(f"List of transactions have been created successfully from {path}")
    except Exception as ex:
        logger.error(f"Returned empty list because of {ex}")
    return to_return


def get_rub_amount(data: dict) -> float:
    """Gets amount out of transaction, converts it to RUB if necessary
    using date of transaction

    :param data: transaction dict
    :return: amount in RUB"""
    logger.debug("get_rub_amount called")
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
        logger.debug("Currency is already RUB")
        logger.info("Amount extracted")
        return amount
    else:
        try:
            date = extract(data, ("date",))
            date = date[:10]
            to_return = convert_to_rub(amount, cur, date)
            logger.info("Currency has been converted")
            return to_return
        except Exception as ex:
            # don't sure it should be that way,
            # but for now I decide to just throw it up
            logger.error("Caught {ex} during currency converting")
            raise ex
