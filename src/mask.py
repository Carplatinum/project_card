def get_mask_card_number(card_number: int) -> str:
    """
    Возвращает замаскированный номер карты в формате XXXX XX** **** XXXX.
    """
    card_str = str(card_number)
    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"


def get_mask_account(account_number: int) -> str:
    """
    Возвращает замаскированный номер счета в формате **XXXX.
    """
    account_str = str(account_number)
    return f"**{account_str[-4:]}"
