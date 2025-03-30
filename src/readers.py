import pandas as pd
from typing import Any, Dict, Hashable, List
from pandas.core.frame import DataFrame


def read_csv_file(file_path: str) -> List[Dict[Hashable, Any]]:
    """
    Считывает финансовые операции из CSV-файла.
    :param file_path: Путь к файлу CSV.
    :return: Список транзакций в виде словарей.
    """
    try:
        # Указываем разделитель ';' для корректного чтения файла
        df: DataFrame = pd.read_csv(file_path, delimiter=';')
        transactions: List[Dict[Hashable, Any]] = df.to_dict(orient='records')
        return transactions
    except Exception as e:
        print(f"Ошибка при чтении CSV-файла: {e}")
        raise


def read_excel_file(file_path: str) -> List[Dict[Hashable, Any]]:
    """
    Считывает финансовые операции из Excel-файла.
    :param file_path: Путь к файлу Excel.
    :return: Список транзакций в виде словарей.
    """
    try:
        df: DataFrame = pd.read_excel(file_path, engine='openpyxl')
        if df.empty:
            raise pd.errors.EmptyDataError("No data in Excel file")
        transactions: List[Dict[Hashable, Any]] = df.to_dict(orient='records')
        return transactions
    except Exception as e:
        print(f"Ошибка при чтении Excel-файла: {e}")
        raise
