#
from datetime import datetime
from typing import List, Dict


def filter_by_state(data: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.
    """
    return [item for item in data if item.get('state') == state]


def sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]:
    """
    Сортирует список словарей по дате.
    """
    return sorted(data, key=lambda x: datetime.fromisoformat(x['date']), reverse=reverse)


if __name__ == '__main__':
    test_data = [
        {'id': 1, 'state': 'EXECUTED',
         'date': '2025-01-01T10:00:00'},
        {'id': 2, 'state': 'CANCELED',
         'date': '2025-01-02T12:00:00'},
        {'id': 3, 'state': 'EXECUTED',
         'date': '2025-01-03T14:00:00'}
    ]
    print("Фильтрация по состоянию EXECUTED:")
    filtered_data = filter_by_state(test_data)
    print(filtered_data)

    print("Сортировка по дате (по убыванию):")
    sorted_data = sort_by_date(test_data)
    print(sorted_data)

    print("Сортировка по дате (по возрастанию):")
    sorted_data_asc = sort_by_date(test_data, reverse=False)
    print(sorted_data_asc)
