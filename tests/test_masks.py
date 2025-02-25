import pytest
from src.mask import get_mask_account, get_mask_card_number
from typing import List, Dict


# Фикстура для номеров карт
@pytest.fixture
def card_numbers() -> List[Dict]:
    return [
        {"number": 1234567890123456, "expected": "1234 56** **** 3456"},
        {"number": 9876543210987654, "expected": "9876 54** **** 7654"}
    ]


# Фикстура для коротких номеров карт
@pytest.fixture
def short_card_numbers() -> List[int]:
    return [
        1234567890123,
        9876543210987
    ]


# Фикстура для номеров счетов
@pytest.fixture
def account_numbers() -> List[Dict]:
    return [
        {"number": 1234567890, "expected": "**7890"},
        {"number": 9876543210, "expected": "**3210"}
    ]


# Фикстура для коротких номеров счетов
@pytest.fixture
def short_account_numbers() -> List[int]:
    return [
        12345,
        98765
    ]


# Фикстура для пустых номеров
@pytest.fixture
def empty_numbers() -> List[int]:
    return [0]


def test_get_mask_card_number_standard(card_numbers: List[Dict]) -> None:
    """
    Проверка маскирования номера карты стандартной длины.
    """
    for data in card_numbers:
        masked_card_number = get_mask_card_number(data["number"])
        assert masked_card_number == data["expected"]


def test_get_mask_card_number_short(short_card_numbers: List[int]) -> None:
    """
    Проверка маскирования короткого номера карты.
    """
    for number in short_card_numbers:
        with pytest.raises(ValueError):
            get_mask_card_number(number)


def test_get_mask_card_number_empty(empty_numbers: List[int]) -> None:
    """
    Проверка обработки пустого номера карты.
    """
    for number in empty_numbers:
        with pytest.raises(ValueError):
            get_mask_card_number(number)


def test_get_mask_account_standard(account_numbers: List[Dict]) -> None:
    """
    Проверка маскирования номера счета стандартной длины.
    """
    for account in account_numbers:
        masked_account_number = get_mask_account(account["number"])
        assert masked_account_number == account["expected"]


def test_get_mask_account_short(short_account_numbers: List[int]) -> None:
    """
    Проверка маскирования короткого номера счета.
    """
    for number in short_account_numbers:
        with pytest.raises(ValueError):
            get_mask_account(number)


def test_get_mask_account_empty(empty_numbers: List[int]) -> None:
    """
    Проверка обработки пустого номера счета.
    """
    for number in empty_numbers:
        with pytest.raises(ValueError):
            get_mask_account(number)
