from datetime import datetime

from src.mask import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """
    Маскирует номер карты или счета на основе входной строки.
    """
    if not info:  # Проверка на пустую строку
        raise ValueError("Пустая строка")

    parts: list[str] = info.split()
    if len(parts) < 2:  # Проверка на корректность формата
        raise ValueError("Некорректный формат входных данных")

    card_type: str = " ".join(parts[:-1])
    number: str = parts[-1]

    if card_type in ["Visa Platinum", "Maestro", "MasterCard", "Visa Classic", "Visa Gold"]:
        masked_number = get_mask_card_number(int(number))
        # Удаление лишнего пробела
        formatted_number = f"{masked_number[:4]}{masked_number[4:6]}** **** {masked_number[-4:]}"
        return f"{card_type} {formatted_number}"
    elif card_type == "Счет":
        masked_number = get_mask_account(int(number))
        return f"{card_type} {masked_number}"
    else:
        raise ValueError("Неподдерживаемый тип карты или счета.")


def get_date(date_str: str) -> str:
    """
    Преобразует строку с датой в формат ДД.ММ.ГГГГ.
    """
    if not date_str:
        raise ValueError("Пустая дата")

    try:
        date_obj: datetime = datetime.fromisoformat(date_str)
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError("Некорректная дата")
