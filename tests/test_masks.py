import pytest
from src.mask import get_mask_card_number, get_mask_account

def get_mask_card_number(card_number):
    """
    Маскирует номер карты.
    Если длина номера карты меньше 16 символов,
    вызывает исключение ValueError.
    """
    if len(str(card_number)) < 16:  # Проверка на короткий номер
        raise ValueError("Номер карты слишком короткий")


def get_mask_account(account_number):
    """
    Маскирует номер счета.
    Если длина номера счета меньше 10 символов,
    вызывает исключение ValueError.
    """
    if len(str(account_number)) < 10:  # Проверка на короткий номер
        raise ValueError("Номер счета слишком короткий")


def test_get_mask_account_short():
    """
    Проверка на короткий номер счета.
    """
    with pytest.raises(ValueError):
        get_mask_account(12345)


def test_get_mask_card_number_short():
    """
    Проверка на короткий номер карты.
    """
    with pytest.raises(ValueError):
        get_mask_card_number(1234567890123)
