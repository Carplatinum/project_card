import pytest
import pandas as pd
from pathlib import Path
from typing import Dict, List
from unittest.mock import patch, Mock
from src.readers import read_csv_file, read_excel_file


@pytest.fixture
def tmp_files(tmp_path: Path) -> Dict[str, Path]:
    """Фикстура для создания временных файлов."""
    files = {
        "csv": tmp_path / "test.csv",
        "excel": tmp_path / "test.xlsx",
        "json": tmp_path / "test.json",
    }
    return files


def create_csv_file(file_path: Path, data: List[str]) -> None:
    """Создает CSV-файл с заданными данными."""
    with open(file_path, "w") as f:
        for row in data:
            f.write(row + "\n")


def create_excel_file(file_path: Path, data: List[List[str]]) -> None:
    """Создает Excel-файл с заданными данными."""
    df = pd.DataFrame(data[1:], columns=data[0])
    df.to_excel(file_path, index=False, engine='openpyxl')


def test_read_csv_file_success(tmp_files: Dict[str, Path]) -> None:
    """Тест успешного чтения CSV-файла."""
    csv_data = ["id;amount;currency", "1;100;USD", "2;200;EUR"]
    create_csv_file(tmp_files["csv"], csv_data)

    # Создаем mock для pd.read_csv с учетом delimiter=';'
    mock_read_csv = Mock(return_value=pd.DataFrame([{"id": 1, "amount": 100, "currency": "USD"},
                                                    {"id": 2, "amount": 200, "currency": "EUR"}]))
    with patch("src.readers.pd.read_csv", new=mock_read_csv):
        result = read_csv_file(str(tmp_files["csv"]))
        expected = [
            {"id": 1, "amount": 100, "currency": "USD"},
            {"id": 2, "amount": 200, "currency": "EUR"},
        ]
        assert result == expected
        mock_read_csv.assert_called_once_with(str(tmp_files["csv"]), delimiter=';')


def test_read_csv_file_not_found(tmp_files: Dict[str, Path]) -> None:
    """Тест чтения несуществующего CSV-файла."""
    mock_read_csv = Mock(side_effect=FileNotFoundError)
    with patch("src.readers.pd.read_csv", new=mock_read_csv):
        with pytest.raises(FileNotFoundError):
            read_csv_file("nonexistent_file.csv")
        mock_read_csv.assert_called_once_with("nonexistent_file.csv", delimiter=';')


def test_read_csv_file_empty(tmp_files: Dict[str, Path]) -> None:
    """Тест чтения пустого CSV-файла."""
    mock_read_csv = Mock(side_effect=pd.errors.EmptyDataError)
    tmp_files["csv"].touch()
    with patch("src.readers.pd.read_csv", new=mock_read_csv):
        with pytest.raises(pd.errors.EmptyDataError):
            read_csv_file(str(tmp_files["csv"]))
        mock_read_csv.assert_called_once_with(str(tmp_files["csv"]), delimiter=';')


def test_read_excel_file_success(tmp_files: Dict[str, Path]) -> None:
    """Тест успешного чтения Excel-файла."""
    excel_data = [["id", "amount", "currency"], ["1", "100", "USD"], ["2", "200", "EUR"]]
    create_excel_file(tmp_files["excel"], excel_data)
    result = read_excel_file(str(tmp_files["excel"]))
    expected = [
        {"id": 1, "amount": 100, "currency": "USD"},
        {"id": 2, "amount": 200, "currency": "EUR"},
    ]
    assert result == expected


def test_read_excel_file_not_found(tmp_files: Dict[str, Path]) -> None:
    """Тест чтения несуществующего Excel-файла."""
    with pytest.raises(FileNotFoundError):
        read_excel_file("nonexistent_file.xlsx")


def test_read_excel_file_empty(tmp_files: Dict[str, Path]) -> None:
    """Тест чтения пустого Excel-файла."""
    import pandas as pd
    df = pd.DataFrame()  # Создаем пустой DataFrame
    file_path = str(tmp_files["excel"])
    df.to_excel(file_path, index=False, engine='openpyxl')  # Записываем пустой DataFrame в Excel-файл
    with pytest.raises(pd.errors.EmptyDataError):
        read_excel_file(file_path)


def test_read_csv_file_with_semicolon(tmp_files: Dict[str, Path]) -> None:
    """Тест чтения CSV-файла с разделителем ';'."""
    csv_data = [
        "id;state;date;amount;currency_name;currency_code;from;to;description",
        "1;EXECUTED;2025-01-01T10:00:00;100;USD;USD;Счет 1234567890123456;Счет 6543210987654321;Перевод",
        "2;CANCELED;2025-01-02T12:00:00;200;EUR;EUR;Счет 1111222233334444;Счет 5555666677778888;Платеж"
    ]
    # Указываем кодировку UTF-8 при создании файла
    with open(tmp_files["csv"], "w", encoding="utf-8") as f:
        for row in csv_data:
            f.write(row + "\n")
    result = read_csv_file(str(tmp_files["csv"]))
    expected = [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2025-01-01T10:00:00",
            "amount": 100,
            "currency_name": "USD",
            "currency_code": "USD",
            "from": "Счет 1234567890123456",
            "to": "Счет 6543210987654321",
            "description": "Перевод"
        },
        {
            "id": 2,
            "state": "CANCELED",
            "date": "2025-01-02T12:00:00",
            "amount": 200,
            "currency_name": "EUR",
            "currency_code": "EUR",
            "from": "Счет 1111222233334444",
            "to": "Счет 5555666677778888",
            "description": "Платеж"
        }
    ]
    assert result == expected
