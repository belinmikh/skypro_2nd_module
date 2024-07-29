import sys
from typing import Any, Callable, Iterable

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
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


def print_iterable(obj: Any, pred: str = "") -> None:
    """Prints iterable objects as their sub-objects each at new line
    and prints average if not iterable

    :param obj: anything
    :param pred: string (for recursive outputs)
    :return: None (just prints objects in different ways)"""
    if isinstance(obj, Iterable) and not isinstance(obj, str):
        print(f"{type(obj)}:")
        for item in obj:
            if isinstance(obj, dict):
                print(f"{pred}{type(item)} (key) {item} ", end="")
                print_iterable(obj[item], pred + "\t")
            else:
                print(f"{pred}\t{item},")
    else:
        print(f"{type(obj)}: {obj}")
    return None


def main() -> None:
    if len(sys.argv) in [2, 3] and sys.argv[1] == "v5.0":
        if len(sys.argv) == 3 and sys.argv[2] not in [
            "card_number_generator",
            "filter_by_currency",
            "transaction_descriptions"
        ]:
            sys.exit("Unknown function name. Use only v5.0 new functions by one\n"
                     "(card_number_generator, filter_by_currency, transaction_descriptions)\n"
                     "or run 'python main.py v5.0' to test them all at the same time")
        if len(sys.argv) == 3:
            to_test = sys.argv[2]
        else:
            to_test = ""
        transactions = (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {
                        "amount": "9824.07",
                        "currency": {
                            "name": "USD",
                            "code": "USD"
                        }
                    },
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702"
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {
                        "amount": "79114.93",
                        "currency": {
                            "name": "USD",
                            "code": "USD"
                        }
                    },
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188"
                },
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {
                        "amount": "43318.34",
                        "currency": {
                            "name": "руб.",
                            "code": "RUB"
                        }
                    },
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160"
                },
                {
                    "id": 895315941,
                    "state": "EXECUTED",
                    "date": "2018-08-19T04:27:37.904916",
                    "operationAmount": {
                        "amount": "56883.54",
                        "currency": {
                            "name": "USD",
                            "code": "USD"
                        }
                    },
                    "description": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                    "to": "Visa Platinum 8990922113665229"
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {
                        "amount": "67314.70",
                        "currency": {
                            "name": "руб.",
                            "code": "RUB"
                        }
                    },
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657"
                }
            ]
        )

        if to_test in ["filter_by_currency", "transaction_descriptions", ""]:
            print("Current test data is ", end="")
            print_iterable(transactions)

        print()
        print("Initialization:")
        print()
        if to_test in ["card_number_generator", ""]:
            card_number_generator_impl = card_number_generator(9999, 10005)
            print("card_number_generator_impl = card_number_generator(9999, 10005)")
        if to_test in ["filter_by_currency", ""]:
            filter_by_currency_impl = filter_by_currency(transactions, "USD")
            print('filter_by_currency_impl = filter_by_currency(transactions, "USD")')
        if to_test in ["transaction_descriptions", ""]:
            transaction_descriptions_impl = transaction_descriptions(transactions)
            print("transaction_descriptions_impl = transaction_descriptions(transactions)")
        print()

        counter = 0

        while True:
            user_input = input("Press enter to run next() for all generator implementations\n"
                               "or enter 'exit' to finish manual testing\n")
            if user_input == "exit":
                break
            print(f"\nRunning iteration number {counter}:")
            print()

            if to_test in ["card_number_generator", ""]:
                try:
                    print(f"next(card_number_generator_impl) --> {next(card_number_generator_impl)}")
                except StopIteration:
                    print("Caught StopIteration running card_number_generator_impl")
                print()

            if to_test in ["filter_by_currency", ""]:
                try:
                    to_print = next(filter_by_currency_impl)
                    print("next(filter_by_currency_impl) --> ", end="")
                    print_iterable(to_print)
                except StopIteration:
                    print("Caught StopIteration running filter_by_currency_impl")
                print()

            if to_test in ["transaction_descriptions", ""]:
                try:
                    print(f"next(transaction_descriptions_impl) --> {next(transaction_descriptions_impl)}")
                except StopIteration:
                    print("Caught StopIteration running transaction_descriptions_impl")
                print()
            counter += 1

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

    if len(sys.argv) == 2 and sys.argv[1] == 'v3.1':
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
