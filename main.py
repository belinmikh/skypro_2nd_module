from src.masks import get_mask_account, get_mask_card_number


def main() -> None:
    # We haven't used pytest yet, so I decided to show tests here
    print("get_mask_card_number:")
    card_input_test = [123, 2200240813573827, "bimbim", "123", "2200240813573827", ["ы", 1], None]
    for i in card_input_test:
        print(f"(*) {type(i)}: {i} --> {get_mask_card_number(i)}")
    print()

    print("get_mask_account:")
    account_input_test = [123, 12342200240813573827, "bambam", "123", "12342200240813573827", ["ы", 1], None]
    for i in account_input_test:
        print(f"(*) {type(i)}: {i} --> {get_mask_account(i)}")


if __name__ == "__main__":
    main()
