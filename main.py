from typing import Any, Callable, Iterable

from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card


def functest(func: Callable, test_arr: Iterable[Any]) -> None:
    """Experimental: just playing with python"""
    print(f"\nTEST OF {func.__name__} FUNCTION IN PROGRESS:\n")
    for i in test_arr:
        print(f"(*) {type(i)}: {i} --> {func(i)}")
    return None


def main() -> None:
    # We haven't used pytest yet, so I decided to show tests here

    card_input_test = [123, 2200240813573827, "bimbim", "123", "2200240813573827", ["ы", 1], None]

    account_input_test = [123, 12342200240813573827, "bambam", "123", "12342200240813573827", ["ы", 1], None]

    mask_account_card_test = [
        "2200240813573827",
        12342200240813573827,
        None,
        ["ы", 1],
        "Maestro 1596837868705199",
        "Счет 64686473678894779589",
        "MasterCard 7158300734726758",
        "Счет 35383033474447895560",
        "Visa Classic 6831982476737658",
        "Visa Platinum 8990922113665229",
        "Visa Gold 5999414228426353",
        "Счет 73654108430135874305",
        "Счет73654108430135874305",
    ]

    get_date_test = [123, "bimbim", None, "2024-03-11T02:26:18.671407"]

    tests_arr = {
        get_mask_account: account_input_test,
        get_mask_card_number: card_input_test,
        mask_account_card: mask_account_card_test,
        get_date: get_date_test,
    }

    for f, a in tests_arr.items():
        functest(f, a)


if __name__ == "__main__":
    main()
