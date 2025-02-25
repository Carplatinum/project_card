from typing import Dict, List

import pytest

from src.widget import get_date, mask_account_card


# Фикстура для тестовых данных по маскировке карты
@pytest.fixture
def card_masking_data() -> List[Dict]:
    return [
        {"card_type": "Visa Platinum", "number": "1111222233334444", "expected": "Visa Platinum 1111 2** **** 4444"},
        {"card_type": "Maestro", "number": "1234567890123456", "expected": "Maestro 1234 5** **** 3456"},
        {"card_type": "Счет", "number": "9999888877776666", "expected": "Счет **6666"}
    ]


# Фикстура для тестовых данных по преобразованию даты
@pytest.fixture
def date_conversion_data() -> List[Dict]:
    return [
        {"date": "2025-01-01T10:00:00", "expected": "01.01.2025"},
        {"date": "2025-02-02T12:00:00", "expected": "02.02.2025"}
    ]


# Фикстура для некорректных входных данных
@pytest.fixture
def invalid_input_data() -> List[str]:
    return [
        "Неподдерживаемый тип 1234567890",
        "Некорректная дата",
        ""
    ]


def test_mask_account_card(card_masking_data: List[Dict]) -> None:
    """Тестирование маскировки номера карты или счета."""
    for data in card_masking_data:
        input_string: str = f"{data['card_type']} {data['number']}"
        expected = data["expected"].replace("  ", " ")  # Удаление лишних пробелов
        assert mask_account_card(input_string) == expected


def test_mask_account_card_invalid_input(invalid_input_data: List[str]) -> None:
    """Проверка обработки некорректных входных данных."""
    for input_string in invalid_input_data:
        try:
            mask_account_card(input_string)
            assert False, f"Expected ValueError for input '{input_string}'"
        except ValueError:
            pass


def test_get_date(date_conversion_data: List[Dict]) -> None:
    """Тестирование преобразования даты."""
    for data in date_conversion_data:
        assert get_date(data["date"]) == data["expected"]


def test_get_date_invalid_input(invalid_input_data: List[str]) -> None:
    """Проверка обработки некорректных входных данных."""
    for date in invalid_input_data:
        with pytest.raises(ValueError):
            get_date(date)
