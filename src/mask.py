import logging

# Настройка логера для модуля masks
masks_logger = logging.getLogger("masks")
masks_logger.setLevel(logging.DEBUG)

# Создаем file_handler для записи логов в файл
file_handler = logging.FileHandler("logs/masks.log", mode="w")
file_handler.setLevel(logging.DEBUG)

# Создаем форматтер для логов
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Добавляем handler к логеру
masks_logger.addHandler(file_handler)


def get_mask_card_number(card_number: int) -> str:
    """
    Возвращает замаскированный номер карты в формате XXXX XX** **** XXXX.
    Если длина номера карты меньше 16 символов, вызывает исключение ValueError.
    """
    try:
        card_str = str(card_number)
        if len(card_str) < 16:
            raise ValueError("Номер карты слишком короткий")
        masked_card = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
        masks_logger.info(f"Успешно замаскирован номер карты: {masked_card}")
        return masked_card
    except ValueError as e:
        masks_logger.error(f"Ошибка при маскировании номера карты: {e}")
        raise


def get_mask_account(account_number: int) -> str:
    """
    Возвращает замаскированный номер счета в формате **XXXX.
    Если длина номера счета меньше 10 символов, вызывает исключение ValueError.
    """
    try:
        account_str = str(account_number)
        if len(account_str) < 10:
            raise ValueError("Номер счета слишком короткий")
        masked_account = f"**{account_str[-4:]}"
        masks_logger.info(f"Успешно замаскирован номер счета: {masked_account}")
        return masked_account
    except ValueError as e:
        masks_logger.error(f"Ошибка при маскировании номера счета: {e}")
        raise
