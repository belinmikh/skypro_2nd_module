import os
from typing import Any
from unittest.mock import patch

from dotenv import load_dotenv

from src.external_api import convert_to_rub


@patch("requests.request")  # I used requests.request instead of requests.get because of example at their site
def test_convert_to_rub(mock_get: Any) -> None:
    mock_get.return_value.json.return_value = {
        "date": "2018-02-22",
        "historical": "",
        "info": {"rate": 148.972231, "timestamp": 1519328414},
        "query": {"amount": 10.0, "from": "GBP", "to": "RUB"},
        "result": 1000.0,
        "success": True,
    }

    load_dotenv()
    erd_api_key = os.getenv("ERD_API_KEY")

    headers = {"apikey": erd_api_key}
    payload: dict = {}

    assert convert_to_rub(10.0, "GBP", "2018-02-22") == 1000.0
    mock_get.assert_called_once_with(
        "GET",
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=GBP&amount=10.0&date=2018-02-22",
        headers=headers,
        data=payload,
    )
