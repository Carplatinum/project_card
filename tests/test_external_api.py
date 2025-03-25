import json
import pytest
from pathlib import Path


@pytest.fixture
def json_file(tmp_path: Path) -> Path:
    """Фикстура для создания тестового JSON-файла. Создает файл `test.json` в временной директории
    и записывает в него список словарей. Возвращает путь до созданного файла."""
    file_path = tmp_path / "test.json"
    with open(file_path, 'w') as _:
        json.dump([{"id": 1}, {"id": 2}], _)
    return file_path
