import pytest
from pathlib import Path
from typing import Any
from decorators import log


# Фикстура для теста вывода в консоль
@pytest.fixture
def capsys(capsys: Any) -> Any:
    """Фикстура для перехвата вывода в консоль."""
    return capsys


def test_log_console(capsys: Any) -> None:
    """Тест логирования в консоль."""

    @log()
    def test_function(x: int, y: int) -> int:
        """Тестовая функция для логирования."""
        return x + y

    test_function(1, 2)
    captured = capsys.readouterr()
    assert "test_function ok" in captured.out


def test_log_file(tmp_path: Path) -> None:
    """Тест логирования в файл."""
    filename = tmp_path / "test_log.txt"

    @log(filename=str(filename))
    def test_function(x: int, y: int) -> int:
        """Тестовая функция для логирования."""
        return x + y

    test_function(1, 2)
    with open(filename, 'r') as file:
        log_content = file.read()
    assert "test_function ok" in log_content


def test_log_error_console(capsys: Any) -> None:
    """Тест логирования ошибки в консоль."""

    @log()
    def test_error_function(x: int, y: int) -> None:
        """Тестовая функция для логирования ошибки."""
        raise ValueError("Ошибка")

    try:
        test_error_function(1, 2)
    except Exception:
        pass
    captured = capsys.readouterr()
    assert "test_error_function error: ValueError" in captured.out


def test_log_error_file(tmp_path: Path) -> None:
    """Тест логирования ошибки в файл."""
    filename = tmp_path / "test_error_log.txt"

    @log(filename=str(filename))
    def test_error_function(x: int, y: int) -> None:
        """Тестовая функция для логирования ошибки."""
        raise ValueError("Ошибка")

    try:
        test_error_function(1, 2)
    except Exception:
        pass
    with open(filename, 'r') as file:
        log_content = file.read()
    assert "test_error_function error: ValueError" in log_content
