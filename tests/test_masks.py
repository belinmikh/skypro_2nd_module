from typing import Any

import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_account_nonsense(nonsense: Any) -> None:
    for test_case in nonsense:
        assert get_mask_account(test_case) is None


@pytest.mark.parametrize(
    "test_input, expected_result",
    [
        ("1234123412341234", None),  # 16-digit, 20 expected
        ("123412341234123412341234", None),  # 24-digit, 20 expected
        ("1Z3412ЗЧ123412341234", None),  # contains alpha-chars, only digit expected
    ],
)
def test_get_mask_account_incorrect(test_input: Any, expected_result: Any) -> None:
    assert get_mask_account(test_input) == expected_result


@pytest.mark.parametrize(
    "test_input, expected_result",
    [("12341234123412341234", "**1234"), ("56785678567856785678", "**5678"), (56785678567856785678, "**5678")],
)
def test_get_mask_account_correct(test_input: Any, expected_result: Any) -> None:
    assert get_mask_account(test_input) == expected_result


def test_get_mask_card_number_nonsense(nonsense: Any) -> None:
    for test_case in nonsense:
        assert get_mask_card_number(test_case) is None


@pytest.mark.parametrize(
    "test_input, expected_result",
    [
        ("123412341234", None),  # 12-digit, 16 expected
        ("12341234123412341234", None),  # 20-digit, 16 expected
        ("1Z3412ЗЧ12341234", None),  # contains alpha-chars, only digit expected
    ],
)
def test_get_mask_card_number_incorrect(test_input: Any, expected_result: Any) -> None:
    assert get_mask_card_number(test_input) == expected_result


@pytest.mark.parametrize(
    "test_input, expected_result",
    [
        ("1234123412341234", "1234 12** **** 1234"),
        ("5678567856785678", "5678 56** **** 5678"),
        (5678567856785678, "5678 56** **** 5678"),
    ],
)
def test_get_mask_card_number_correct(test_input: Any, expected_result: Any) -> None:
    assert get_mask_card_number(test_input) == expected_result
