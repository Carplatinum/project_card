import json
from typing import Dict, List


def read_json_file(file_path: str) -> List[Dict]:
    """
    Читает JSON-файл и возвращает список словарей с данными о финансовых транзакциях.

    Если файл пустой, содержит не список или не найден, возвращается пустой список.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
