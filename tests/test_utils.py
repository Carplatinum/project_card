import pytest
import json
from pathlib import Path
from src.utils import read_json_file


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
