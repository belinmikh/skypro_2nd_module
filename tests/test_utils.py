import json
import os
from typing import Any
from unittest.mock import patch

import pytest
from dotenv import load_dotenv

from src.utils import get_rub_amount, read_json_local


@pytest.mark.parametrize(
    "content",
    [
        (None,),
        ("abobus",),  # just strange types
        (["bimbim", "bambam"],),  # list of non-dicts
        ([{"0": "bimbim"}, {"1": "bambam"}]),  # list of dicts
    ],
)
def test_read_json_local(content: Any) -> None:
    with open("test_read_json_local.json", "w") as file:
        json.dump(content, file)
    if isinstance(content, list) and sum([isinstance(x, dict) for x in content]) == len(content):
        assert read_json_local("test_read_json_local.json") == content
    else:
        assert read_json_local("test_read_json_local.json") == []


def test_read_json_local_dne() -> None:
    assert read_json_local("does_not_exist.json") == []


@patch("requests.request")  # I used requests.request instead of requests.get because of example at their site
def test_get_rub_amount(mock_get: Any) -> None:
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

    assert (
        get_rub_amount(
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2018-02-22T10:50:58.294041",
                "operationAmount": {"amount": "10.0", "currency": {"name": "pound", "code": "GBP"}},
                "description": "Brawl Stars donation",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            }
        )
        == 1000.0
    )

    mock_get.assert_called_once_with(
        "GET",
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=GBP&amount=10.0&date=2018-02-22",
        headers=headers,
        data=payload,
    )

    assert (
        get_rub_amount(
            {
                "id": 441945887,
                "state": "EXECUTED",
                "date": "2018-02-22T10:50:58.294041",
                "operationAmount": {"amount": "128.0", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "The Digger Online donation",
                "from": "Maestro 1596837868705198",
                "to": "Счет 64686473678894779587",
            }
        )
        == 128.0
    )
