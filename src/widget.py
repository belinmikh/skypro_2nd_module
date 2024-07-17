from src.masks import *

CARDS = ["Visa Platinum", "Maestro"]
ACCOUNTS = ["Счет", "Счёт"]
# Well I'm sorry I just like 'ё', couldn't resist it


def mask_account_card(initial: str) -> str | None:
    """Returns masked account or card number if input matches string,
    which begins with allowed (you can change it at widget.py constants)
    account or card type and contains account or card number
    divided from its type with space, None otherwise"""
    if not isinstance(initial, str):
        return None
    for card in CARDS:
        if initial.startswith(card):
            initial = initial.replace(card, "").strip()
            to_return = get_mask_card_number(initial)
            if to_return is not None:
                to_return = card + " " + to_return
            return to_return
    for account in ACCOUNTS:
        if initial.startswith(account):
            initial = initial.replace(account, "").strip()
            to_return = get_mask_account(initial)
            if to_return is not None:
                to_return = account + " " + to_return
            return to_return
    return None
