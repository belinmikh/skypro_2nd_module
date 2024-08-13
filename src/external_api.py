import datetime
import os

import requests
from dotenv import load_dotenv

from src.tools import extract


def convert_to_rub(amount: float, currency: str, date: str = datetime.datetime.now().strftime("%Y-%m-%d")) -> float:
    """Converts amount to RUB currency

    HAVING API KEY IN .ENV IS NECESSARY!
    Make sure to handle exceptions OUTSIDE this function while calling

    :param amount: amount, float
    :param currency: currency code ('USD' as example)
    :param date: str 'YYYY-MM-DD' format, today for default
    :return: amount in RUB"""
    load_dotenv()
    erd_api_key = os.getenv("ERD_API_KEY")

    headers = {"apikey": erd_api_key}
    payload: dict = {}

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}&date={date}"

    # I used requests.request instead of requests.get because of example at their site
    response = requests.request("GET", url, headers=headers, data=payload)

    result = response.json()

    return extract(result, ("result",))
