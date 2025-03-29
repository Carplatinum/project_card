import pandas as pd
from typing import List, Dict


def read_csv_file(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из CSV-файла.
    :param file_path: Путь к файлу CSV.
    :return: Список транзакций в виде словарей.
    """
    try:
        df = pd.read_csv(file_path)
        transactions = df.to_dict(orient='records')
        return transactions
    except Exception as e:
        print(f"Ошибка при чтении CSV-файла: {e}")
        raise


def read_excel_file(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из Excel-файла.
    :param file_path: Путь к файлу Excel.
    :return: Список транзакций в виде словарей.
    """
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
        if df.empty:
            raise pd.errors.EmptyDataError("No data in Excel file")
        transactions = df.to_dict(orient='records')
        return transactions
    except Exception as e:
        print(f"Ошибка при чтении Excel-файла: {e}")
        raise
