def get_mask_card_number(card_number: int) -> str:
    """
    Возвращает замаскированный номер карты в формате XXXX XX** **** XXXX.
    Если длина номера карты меньше 16 символов, вызывает исключение ValueError.
    """
    card_str = str(card_number)
    if len(card_str) < 16:
        raise ValueError("Номер карты слишком короткий")
    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"


def get_mask_account(account_number: int) -> str:
    """
    Возвращает замаскированный номер счета в формате **XXXX.
    Если длина номера счета меньше 10 символов, вызывает исключение ValueError.
    """
    account_str = str(account_number)
    if len(account_str) < 10:
        raise ValueError("Номер счета слишком короткий")
    return f"**{account_str[-4:]}"
