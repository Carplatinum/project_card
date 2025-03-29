import pytest
from typing import Dict, List
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# Фикстура для тестовых данных по транзакциям
@pytest.fixture
def transactions() -> List[Dict]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        }
    ]


def test_filter_by_currency(transactions: List[Dict]) -> None:
    """Тестирование фильтрации по валюте."""
    usd_transactions = filter_by_currency(transactions, "USD")
    expected_ids = [939719570, 142264268]
    actual_ids = [transaction['id'] for transaction in usd_transactions]
    assert actual_ids == expected_ids

    # Проверка отсутствия транзакций в другой валюте
    rub_transactions = filter_by_currency(transactions, "RUB")
    expected_rub_ids = [873106923]
    actual_rub_ids = [transaction['id'] for transaction in rub_transactions]
    assert actual_rub_ids == expected_rub_ids

    # Проверка пустого списка
    empty_transactions = filter_by_currency([], "USD")
    assert list(empty_transactions) == []


def test_transaction_descriptions(transactions: List[Dict]) -> None:
    """Тестирование генерации описаний транзакций."""
    descriptions = transaction_descriptions(transactions)
    expected_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет"
    ]
    actual_descriptions = list(descriptions)
    assert actual_descriptions == expected_descriptions

    # Проверка пустого списка
    empty_descriptions = transaction_descriptions([])
    assert list(empty_descriptions) == []


@pytest.mark.parametrize("start, stop, expected", [
    (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
    (10, 12, ["0000 0000 0000 0010", "0000 0000 0000 0011", "0000 0000 0000 0012"])
])
def test_card_number_generator(start: int, stop: int, expected: List[str]) -> None:
    """Тестирование генератора номеров карт."""
    card_numbers = list(card_number_generator(start, stop))
    assert card_numbers == expected

    # Проверка корректности форматирования
    for card_number in card_numbers:
        assert len(card_number) == 19
        assert card_number.count(' ') == 3

    # Проверка крайних значений
    single_card = list(card_number_generator(1, 1))
    assert single_card == ["0000 0000 0000 0001"]
