import pytest

from src.mask import get_mask_account, get_mask_card_number


def test_get_mask_account_short() -> None:
    """
    Проверка на короткий номер счета.
    """
    with pytest.raises(ValueError):
        get_mask_account(12345)


def test_get_mask_card_number_short() -> None:
    """
    Проверка на короткий номер карты.
    """
    with pytest.raises(ValueError):
        get_mask_card_number(1234567890123)


# Additional tests to ensure the masking works correctly
def test_get_mask_card_number() -> None:
    """
    Проверка маскирования номера карты.
    """
    card_number = 1234567890123456
    masked_card_number = get_mask_card_number(card_number)
    assert masked_card_number == "1234 56** **** 3456"


def test_get_mask_account() -> None:
    """
    Проверка маскирования номера счета.
    """
    account_number = 1234567890
    masked_account_number = get_mask_account(account_number)
    assert masked_account_number == "**7890"
