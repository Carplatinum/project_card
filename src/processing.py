import re
from typing import List, Dict
from collections import Counter
from typing import List, Dict


def filter_by_state(data: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.
    """
    return [item for item in data if item.get('state') == state]


def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по дате.
    """
    return sorted(data, key=lambda x: datetime.fromisoformat(x['date']), reverse=reverse)


def filter_by_description(transactions: List[Dict], search_string: str) -> List[Dict]:
    """
    Фильтрует список транзакций по строке в описании.
    Использует регулярные выражения для поиска.
    """
    try:
        pattern = re.compile(search_string, re.IGNORECASE)  # Поиск без учета регистра
        filtered_transactions = [t for t in transactions if pattern.search(t.get('description', ''))]
        return filtered_transactions
    except re.error as e:
        print(f"Ошибка в регулярном выражении: {e}")
        return []


def count_transactions_by_category(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
        """
        Подсчитывает количество операций по категориям.
        Категории берутся из поля 'description'.
        """
        descriptions = [t.get('description', '').lower() for t in transactions]
        category_counts = Counter(desc for desc in descriptions if desc in categories)
        return dict(category_counts)
