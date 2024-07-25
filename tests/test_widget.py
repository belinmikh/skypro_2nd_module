from typing import Any

import pytest

from src.widget import get_date, mask_account_card


def test_get_date_nonsense(nonsense: Any) -> None:
    for test_case in nonsense:
        assert get_date(test_case) is None


@pytest.mark.parametrize(
    "test_input, expected_result", [("12.12.12, 22:22:22.22222", None)]  # wrong date and time format
)
def test_get_date_incorrect(test_input: Any, expected_result: Any) -> None:
    assert get_date(test_input) == expected_result


@pytest.mark.parametrize(
    "test_input, expected_result", [("2012-12-12T22:22:22.222222", "12.12.2012")]  # exact date and time format
)
def test_get_date_correct(test_input: Any, expected_result: Any) -> None:
    assert get_date(test_input) == expected_result


def test_mask_account_card_nonsense(nonsense: Any) -> None:
    for test_case in nonsense:
        assert mask_account_card(test_case) is None


@pytest.mark.parametrize(
    "test_input, expected_result",
    [
        ("MasterCard 7158300734726758", None),  # MasterCard is not listed
        ("Счет73654108430135874305", None),  # space before number is required
        ("Счет ", None),
        ("Visa Platinum abobus", None),
    ],
)
def test_mask_account_card_incorrect(test_input: Any, expected_result: Any) -> None:
    assert mask_account_card(test_input) == expected_result


@pytest.mark.parametrize(
    "test_input, expected_result",
    [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"), ("Счет 35383033474447895560", "Счет **5560")],
)
def test_mask_account_card_correct(test_input: Any, expected_result: Any) -> None:
    assert mask_account_card(test_input) == expected_result
