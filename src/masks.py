from typing import Union

from src.loggers import create_basic_logger

logger = create_basic_logger(__name__)


def get_mask_card_number(card_number: Union[str, int]) -> str | None:
    """Returns masked card number if input matches 16 digits string or integer, None otherwise

    :param card_number: 16-digit string or integer card number
    :return: masked card number
    """
    logger.debug("get_mask_card_number called")
    if isinstance(card_number, int):
        card_number = str(card_number)
    if not isinstance(card_number, str) or len(card_number) != 16 or not card_number.isdigit():
        logger.error("Value does not match agreed card number format")
        return None
    card_number_iterable = [x for x in card_number]
    masked_card_number = []
    for i in range(len(card_number_iterable)):
        if i > 0 and i % 4 == 0:
            masked_card_number.append(" ")
        if 6 <= i < 12:
            masked_card_number.append("*")
        else:
            masked_card_number.append(card_number_iterable[i])
    logger.info("Card number has been masked successfully")
    return "".join(masked_card_number)


def get_mask_account(account: Union[str, int]) -> str | None:
    """Returns masked account number if input matches 20 digits string or integer, None otherwise

    :param account: 20-digit string or integer account number
    :return: masked account number
    """
    logger.debug("get_mask_account called")
    if isinstance(account, int):
        account = str(account)
    if not isinstance(account, str) or len(account) != 20 or not account.isdigit():
        logger.error("Value does not match agreed account format")
        return None
    account_iterable = [x for x in account]
    masked_account = ["*", "*"]
    for i in account_iterable[-4:]:
        masked_account.append(i)
    logger.info("Account has been masked successfully")
    return "".join(masked_account)
