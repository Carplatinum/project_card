import json
import logging
from datetime import datetime
from typing import Any, Dict, List

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
        utils_logger.info(f"Успешно отфильтровано по состоянию '{state}': {len(filtered_data)} записей")
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
        utils_logger.info(f"Успешно отсортировано по дате: {len(sorted_data)} записей")
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
