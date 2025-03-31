import re
import json
import logging
from datetime import datetime
from typing import Any, Dict, List
from collections import Counter

# Настройка логера для модуля utils
utils_logger = logging.getLogger("utils")
utils_logger.setLevel(logging.DEBUG)

# Создаем file_handler для записи логов в файл
file_handler = logging.FileHandler("logs/utils.log", mode="w")
file_handler.setLevel(logging.DEBUG)

# Создаем форматтер для логов
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Добавляем handler к логеру
utils_logger.addHandler(file_handler)


def filter_by_state(data: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """
    Фильтрует список словарей по значению ключа 'state'.
    """
    try:
        filtered_data = [item for item in data if item.get('state') == state]
        message = f"Успешно отфильтровано по состоянию '{state}': {len(filtered_data)} записей"
        utils_logger.info(message)
        return filtered_data
    except Exception as e:
        utils_logger.error(f"Ошибка при фильтрации данных: {e}")
        raise


def sort_by_date(data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по дате.
    """
    try:
        sorted_data = sorted(data, key=lambda x: datetime.fromisoformat(x['date']), reverse=reverse)
        message = f"Успешно отсортировано по дате: {len(sorted_data)} записей"
        utils_logger.info(message)
        return sorted_data
    except Exception as e:
        utils_logger.error(f"Ошибка при сортировке данных: {e}")
        raise


def read_json_file(file_path: str) -> List[Dict[Any, Any]]:
    """
    Чтение JSON-файла и возврат данных в виде списка словарей.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        data: List[Dict[Any, Any]] = json.load(file)
    return data


def filter_by_description(transactions: List[Dict[str, Any]], search_string: str) -> List[Dict[str, Any]]:
    """
    Фильтрует список транзакций по заданной строке в описании, используя регулярные выражения.

    :param transactions: Список словарей с данными о банковских операциях.
    :param search_string: Строка для поиска в описании операций.
    :return: Список словарей с операциями, у которых в описании есть данная строка.
    """
    try:
        filtered_transactions = [
            transaction for transaction in transactions
            if re.search(search_string, transaction.get('description', ''), re.IGNORECASE)
        ]
        message = (
            f"Успешно отфильтровано по описанию '{search_string}': "
            f"{len(filtered_transactions)} записей"
        )
        utils_logger.info(message)
        return filtered_transactions
    except Exception as e:
        utils_logger.error(f"Ошибка при фильтрации по описанию: {e}")
        raise


def count_transaction_categories(transactions: List[Dict[str, Any]]) -> Dict[str, int]:
    """
    Подсчитывает количество банковских операций определенного типа.
    """
    try:
        descriptions = [transaction.get('description', '') for transaction in transactions]
        category_counts = Counter(descriptions)
        utils_logger.info(f"Успешно подсчитаны категории транзакций: {category_counts}")
        return dict(category_counts)
    except Exception as e:
        utils_logger.error(f"Ошибка при подсчете категорий транзакций: {e}")
        raise
