import json
from pathlib import Path

import pytest

from src.utils import read_json_file


@pytest.fixture
def json_file(tmp_path: Path) -> Path:
    """Фикстура для создания тестового JSON-файла. Создает файл `test.json` в временной директории
    и записывает в него список словарей. Возвращает путь до созданного файла."""
    file_path = tmp_path / "test.json"
    with open(file_path, 'w') as _:
        json.dump([{"id": 1}, {"id": 2}], _)
    return file_path


def test_read_json_file(json_file: Path) -> None:
    """Тест чтения JSON-файла с валидными данными. Проверяет, что функция `read_json_file`
    корректно читает JSON-файл и возвращает список словарей."""
    data = read_json_file(str(json_file))
    assert len(data) == 2


def test_read_json_file_empty(tmp_path: Path) -> None:
    """Тест чтения пустого JSON-файла. Проверяет, что функция `read_json_file`
    возвращает пустой список при чтении пустого JSON-файла."""
    file_path = tmp_path / "empty.json"
    with open(file_path, 'w') as _:
        pass
    data = read_json_file(str(file_path))
    assert data == []


def test_read_json_file_not_found(tmp_path: Path) -> None:
    """Тест попытки прочитать несуществующий JSON-файл. Проверяет, что функция `read_json_file`
    возвращает пустой список при попытке прочитать несуществующий файл."""
    file_path = tmp_path / "not_found.json"
    data = read_json_file(str(file_path))
    assert data == []


def test_read_json_file_invalid_json(tmp_path: Path) -> None:
    """Тест чтения файла с невалидным JSON. Проверяет, что функция `read_json_file`
    возвращает пустой список при попытке прочитать файл с невалидным JSON."""
    file_path = tmp_path / "invalid.json"
    with open(file_path, 'w') as _:
        _.write("Invalid JSON")
    data = read_json_file(str(file_path))
    assert data == []
