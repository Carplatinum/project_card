from typing import Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


# Фикстура для тестовых данных
@pytest.fixture
def test_data() -> List[Dict]:
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': '2025-01-01T10:00:00'},
        {'id': 2, 'state': 'CANCELED', 'date': '2025-01-02T12:00:00'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2025-01-03T14:00:00'}
    ]


# Фикстура для данных с неверным форматом даты
@pytest.fixture
def test_data_invalid_date(test_data: List[Dict]) -> List[Dict]:
    data = test_data.copy()
    data[0]['date'] = "InvalidDate"
    return data


# Фикстура для данных с несуществующим состоянием
@pytest.fixture
def test_data_unknown_state(test_data: List[Dict]) -> List[Dict]:
    data = test_data.copy()
    data[0]['state'] = 'UNKNOWN'
    return data


@pytest.mark.parametrize("state, expected_length", [
    ('EXECUTED', 2),
    ('CANCELED', 1),
    ('UNKNOWN', 0)
])
def test_filter_by_state(test_data: List[Dict], state: str, expected_length: int) -> None:
    """Тестирование фильтрации по состоянию."""
    filtered = filter_by_state(test_data, state=state)
    assert len(filtered) == expected_length


@pytest.mark.parametrize("reverse, expected", [
    (True, [{'id': 3, 'state': 'EXECUTED', 'date': '2025-01-03T14:00:00'},
            {'id': 2, 'state': 'CANCELED', 'date': '2025-01-02T12:00:00'},
            {'id': 1, 'state': 'EXECUTED', 'date': '2025-01-01T10:00:00'}]),
    (False, [{'id': 1, 'state': 'EXECUTED', 'date': '2025-01-01T10:00:00'},
             {'id': 2, 'state': 'CANCELED', 'date': '2025-01-02T12:00:00'},
             {'id': 3, 'state': 'EXECUTED', 'date': '2025-01-03T14:00:00'}])
])
def test_sort_by_date(test_data: List[Dict], reverse: bool, expected: List[Dict]) -> None:
    """Тестирование сортировки по дате."""
    sorted_data = sort_by_date(test_data, reverse=reverse)
    assert sorted_data == expected


def test_sort_by_date_invalid_date(test_data_invalid_date: List[Dict]) -> None:
    """Тестирование сортировки с невалидной датой."""
    with pytest.raises(ValueError):
        sort_by_date(test_data_invalid_date)
