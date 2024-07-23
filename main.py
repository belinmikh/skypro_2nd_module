import sys
from typing import Any, Callable, Iterable

from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card


def functest(func: Callable, test_arr: Iterable[Any]) -> None:
    """Experimental: just playing with python

    :param func: function to test (temporarily accepts only one argument)
    :param test_arr: list of possible arguments for function
    :return: None (just prints calling results while execution)"""
    print(f"\nTEST OF {func.__name__} FUNCTION IN PROGRESS:\n")
    for i in test_arr:
        print(f"(*) {type(i)}: {i} --> {func(i)}")
    return None


def print_iterable(obj: Any) -> None:
    """Prints iterable objects as their sub-objects each at new line
    and prints average if not iterable

    :param obj: anything
    :return: None (just prints objects in different ways)"""
    if isinstance(obj, Iterable):
        print(f"{type(obj)}:")
        for item in obj:
            print(f"\t{item},")
    else:
        print(f"{type(obj)}: {obj}")
    return None


def main() -> None:
    # We haven't used pytest yet, so I decided to show tests here

    if len(sys.argv) == 2 and sys.argv[1] == "v2.3":
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

        for func, args in tests_arr.items():
            functest(func, args)

    if len(sys.argv) == 1:
        processing_test = [
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        ]

        for test_case in processing_test:
            print("data, ", end="")
            print_iterable(test_case)
            print()

            print("(*) filter_by_state(data) --> ", end="")
            print_iterable(filter_by_state(test_case))
            print()

            print("(*) filter_by_state(data, 'CANCELED') --> ", end="")
            print_iterable(filter_by_state(test_case, "CANCELED"))
            print()

            print("(*) sort_by_date(data) --> ", end="")
            print_iterable(sort_by_date(test_case))
            print()

            print("(*) sort_by_date(data, reverse=False) --> ", end="")
            print_iterable(sort_by_date(test_case, reverse=False))


if __name__ == "__main__":
    main()
