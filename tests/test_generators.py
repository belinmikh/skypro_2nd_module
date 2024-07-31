from typing import Any

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_card_number_generator() -> None:
    card_number_generator_impl = card_number_generator(12345, 12350)
    assert next(card_number_generator_impl) == "0000 0000 0001 2345"
    assert next(card_number_generator_impl) == "0000 0000 0001 2346"
    assert next(card_number_generator_impl) == "0000 0000 0001 2347"
    assert next(card_number_generator_impl) == "0000 0000 0001 2348"
    assert next(card_number_generator_impl) == "0000 0000 0001 2349"
    with pytest.raises(StopIteration):
        next(card_number_generator_impl)


def test_filter_by_currency(to_generators: Any) -> None:
    filter_by_currency_impl = filter_by_currency(to_generators, "USD")
    assert next(filter_by_currency_impl) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(filter_by_currency_impl) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(filter_by_currency_impl) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }
    with pytest.raises(StopIteration):
        next(filter_by_currency_impl)


def test_filter_by_currency_missing_data(to_generators_missing_data: Any) -> None:
    filter_by_currency_impl = filter_by_currency(to_generators_missing_data, "USD")
    assert next(filter_by_currency_impl) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    with pytest.raises(StopIteration):
        next(filter_by_currency_impl)


def test_transaction_descriptions(to_generators: Any) -> None:
    transaction_descriptions_impl = transaction_descriptions(to_generators)
    assert next(transaction_descriptions_impl) == "Перевод организации"
    assert next(transaction_descriptions_impl) == "Перевод со счета на счет"
    assert next(transaction_descriptions_impl) == "Перевод со счета на счет"
    assert next(transaction_descriptions_impl) == "Перевод с карты на карту"
    assert next(transaction_descriptions_impl) == "Перевод организации"
    with pytest.raises(StopIteration):
        next(transaction_descriptions_impl)


def test_transaction_descriptions_missing_data(to_generators_missing_data: Any) -> None:
    transaction_descriptions_impl = transaction_descriptions(to_generators_missing_data)
    assert next(transaction_descriptions_impl) == "Перевод со счета на счет"
    assert next(transaction_descriptions_impl) == "Перевод со счета на счет"
    assert next(transaction_descriptions_impl) == "Перевод с карты на карту"
    with pytest.raises(StopIteration):
        next(transaction_descriptions_impl)
