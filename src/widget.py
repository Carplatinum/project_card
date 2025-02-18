from datetime import datetime

from src.mask import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """
    Маскирует номер карты или счета на основе входной строки.

    :param info: Строка, содержащая тип и номер карты или счета.
    :return: Замаскированный номер карты или счета в виде строки.
    """
    parts: list[str] = info.split()
    card_type: str = " ".join(parts[:-1])
    number: str = parts[-1]

    if card_type in ["Visa Platinum", "Maestro", "MasterCard", "Visa Classic", "Visa Gold"]:
        return f"{card_type} {get_mask_card_number(int(number))}"
    elif card_type == "Счет":
        return f"{card_type} {get_mask_account(int(number))}"
    else:
        raise ValueError("Неподдерживаемый тип карты или счета.")


def get_date(date_str: str) -> str:
    """
    Преобразует строку с датой в формат ДД.ММ.ГГГГ.

    :param date_str: Дата в формате ISO.
    :return: Дата в формате ДД.ММ.ГГГГ.
    """
    date_obj: datetime = datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")
