from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card


def main() -> None:
    # We haven't used pytest yet, so I decided to show tests here

    # v1.0
    print("get_mask_card_number:")
    card_input_test = [123, 2200240813573827, "bimbim", "123", "2200240813573827", ["ы", 1], None]
    for i in card_input_test:
        print(f"(*) {type(i)}: {i} --> {get_mask_card_number(i)}")
    print()

    print("get_mask_account:")
    account_input_test = [123, 12342200240813573827, "bambam", "123", "12342200240813573827", ["ы", 1], None]
    for i in account_input_test:
        print(f"(*) {type(i)}: {i} --> {get_mask_account(i)}")
    print()

    # v2.1
    print("mask_account_card:")
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
        "Счет73654108430135874305"
    ]
    for i in mask_account_card_test:
        print(f"(*) {type(i)}: {i} --> {mask_account_card(i)}")
    print()

    # v2.2
    print("get_date:")
    get_date_test = [123, "bimbim", None, "2024-03-11T02:26:18.671407"]
    for i in get_date_test:
        print(f"(*) {type(i)}: {i} --> {get_date(i)}")
    print()


if __name__ == "__main__":
    main()
