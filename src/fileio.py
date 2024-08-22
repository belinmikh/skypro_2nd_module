import pandas as pd

from src.loggers import create_basic_logger
from src.utils import read_json_local

logger = create_basic_logger(__name__)


def xlsx_to_list(path: str = "data/transactions_excel.xlsx") -> list[dict]:
    """Tries to convert .xlsx to list of dictionaries, returns empty list if fails

    :param path: file path
    :return: list of dictionaries made of rows
    """
    try:
        return pd.read_excel(path).to_dict("records")
    except Exception as ex:
        logger.error(f"Caught exception: {ex}")
        return []


def csv_to_list(path: str = "data/transactions.csv", sep: str = ";") -> list[dict]:
    """Tries to convert .csv to list of dictionaries, returns empty list if fails

    :param path: file path
    :param sep: csv separator (default set as ';')
    :return: list of dictionaries made of rows
    """
    try:
        return pd.read_csv(path, sep=sep, header=0).to_dict("records")
    except Exception as ex:
        logger.error(f"Caught exception: {ex}")
        return []


def file_to_list(path: str) -> list[dict]:
    """Gets transactions out of .csv or .xlsx, empty list if something goes wrong

    :param path: file path
    :return: list of transactions as dictionaries"""
    if path.endswith(".xlsx"):
        return xlsx_to_list(path)
    elif path.endswith(".csv"):
        return csv_to_list(path)
    elif path.endswith(".json"):
        return read_json_local(path)
    else:
        logger.error(f"{path} file extension not supported")
        return []
