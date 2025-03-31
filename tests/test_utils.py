import pytest
import json
from pathlib import Path
from src.utils import read_json_file, filter_by_description, count_transaction_categories
from typing import List, Dict, Any


@pytest.fixture
def test_data() -> List[Dict[str, Any]]:
    """Фикстура для тестовых данных транзакций."""
    return [
        {
            'id': 1,
            'state': 'EXECUTED',
            'date': '2025-01-01T10:00:00',
            'description': 'Перевод организации',
            'amount': 100,
            'currency_name': 'USD'
        },
        {
            'id': 2,
            'state': 'CANCELED',
            'date': '2025-01-02T12:00:00',
            'description': 'Перевод с карты на карту',
            'amount': 200,
            'currency_name': 'EUR'
        },
        {
            'id': 3,
            'state': 'EXECUTED',
            'date': '2025-01-03T14:00:00',
            'description': 'Открытие вклада',
            'amount': 300,
            'currency_name': 'RUB'
        },
        {
            'id': 4,
            'state': 'EXECUTED',
            'date': '2025-01-04T16:00:00',
            'description': 'Перевод организации',
            'amount': 400,
            'currency_name': 'RUB'
        }
    ]


def test_read_json_file(tmp_path: Path) -> None:
    """Тест чтения валидного JSON-файла."""
    file_path = tmp_path / "valid.json"
    data = [{"key": "value"}]
    with open(file_path, 'w') as f:
        json.dump(data, f)
    result = read_json_file(str(file_path))
    assert result == data


def test_read_json_file_empty(tmp_path: Path) -> None:
    """Тест чтения пустого JSON-файла."""
    file_path = tmp_path / "empty.json"
    with open(file_path, 'w'):
        pass
    with pytest.raises(json.decoder.JSONDecodeError):
        read_json_file(str(file_path))


def test_read_json_file_not_found(tmp_path: Path) -> None:
    """Тест попытки прочитать несуществующий JSON-файла."""
    file_path = tmp_path / "not_found.json"
    with pytest.raises(FileNotFoundError):
        read_json_file(str(file_path))


def test_read_json_file_invalid_json(tmp_path: Path) -> None:
    """Тест чтения файла с невалидным JSON."""
    file_path = tmp_path / "invalid.json"
    with open(file_path, 'w') as f:
        f.write("Invalid JSON")
    with pytest.raises(json.decoder.JSONDecodeError):
        read_json_file(str(file_path))


def test_filter_by_description(test_data: List[Dict[str, Any]]) -> None:
    """Тест фильтрации по описанию."""
    result = filter_by_description(test_data, 'организации')
    assert len(result) == 2
    assert result[0]['id'] == 1
    assert result[1]['id'] == 4

    result = filter_by_description(test_data, 'вклада')
    assert len(result) == 1
    assert result[0]['id'] == 3

    result = filter_by_description(test_data, 'несуществующая строка')
    assert len(result) == 0


def test_count_transaction_categories(test_data: List[Dict[str, Any]]) -> None:
    """Тест подсчета категорий транзакций."""
    result = count_transaction_categories(test_data)
    assert result['Перевод организации'] == 2
    assert result['Перевод с карты на карту'] == 1
    assert result['Открытие вклада'] == 1
