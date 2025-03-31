import json
import logging
from typing import Any, Dict, List
from datetime import datetime

from src.readers import read_csv_file, read_excel_file
from src.utils import filter_by_state, sort_by_date, filter_by_description


# Настройка логера для модуля main
main_logger = logging.getLogger("main")
main_logger.setLevel(logging.DEBUG)

# Создаем file_handler для записи логов в файл
file_handler = logging.FileHandler("logs/main.log", mode="w")
file_handler.setLevel(logging.DEBUG)

# Создаем форматтер для логов
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Добавляем handler к логеру
main_logger.addHandler(file_handler)


def get_transactions_from_file(file_path: str) -> List[Dict[Any, Any]]:
    """
    Получает список транзакций из файла в зависимости от его типа.
    """
    if file_path.endswith('.json'):
        with open(file_path, 'r', encoding='utf-8') as file:
            transactions: List[Dict[Any, Any]] = json.load(file)
        return transactions
    elif file_path.endswith('.csv'):
        return read_csv_file(file_path)
    elif file_path.endswith('.xlsx'):
        return read_excel_file(file_path)
    else:
        raise ValueError("Неподдерживаемый формат файла")


def display_transaction(transaction: Dict[str, Any]) -> None:
    """
    Выводит информацию о транзакции в консоль.
    """
    date_str = transaction.get('date')
    if date_str:
        date_obj = datetime.fromisoformat(date_str)
        formatted_date = date_obj.strftime("%d.%m.%Y")
    else:
        formatted_date = "Дата не указана"

    description = transaction.get('description', 'Описание не указано')
    amount = transaction.get('amount', 'Сумма не указана')
    currency_name = transaction.get('currency_name', 'Валюта не указана')

    from_account = transaction.get('from', 'Отправитель не указан')
    to_account = transaction.get('to', 'Получатель не указан')

    print(f"{formatted_date} {description}")
    print(f"{from_account} -> {to_account}")
    print(f"Сумма: {amount} {currency_name}\n")


def main() -> None:
    """
    Основная функция программы, обеспечивающая взаимодействие с пользователем.
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    while True:
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        choice = input()

        if choice in ["1", "2", "3"]:
            try:
                if choice == "1":
                    file_path = input("Введите путь к JSON-файлу: ")
                    transactions = get_transactions_from_file(file_path)
                elif choice == "2":
                    file_path = input("Введите путь к CSV-файлу: ")
                    transactions = get_transactions_from_file(file_path)
                elif choice == "3":
                    file_path = input("Введите путь к XLSX-файлу: ")
                    transactions = get_transactions_from_file(file_path)
                break
            except FileNotFoundError:
                print("Файл не найден. Пожалуйста, проверьте путь и попробуйте снова.")
            except ValueError as e:
                print(f"Ошибка: {e}")
        else:
            print("Некорректный ввод. Пожалуйста, выберите один из предложенных пунктов меню.")

    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        state = input().upper()

        if state in ["EXECUTED", "CANCELED", "PENDING"]:
            transactions = filter_by_state(transactions, state)
            print(f'Операции отфильтрованы по статусу "{state}"')
            break
        else:
            print(f'Статус операции "{state}" недоступен.')

    sort_by_date_input = input("Отсортировать операции по дате? Да/Нет: ").lower()
    if sort_by_date_input == "да":
        order = input("Отсортировать по возрастанию или по убыванию? ").lower()
        reverse = order == "по убыванию"
        transactions = sort_by_date(transactions, reverse)

    currency_filter = input("Выводить только рублевые транзакции? Да/Нет: ").lower()
    if currency_filter == "да":
        transactions = list(filter(lambda x: x.get('currency_name') == 'руб.', transactions))

    description_filter = input(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет: "
    ).lower()
    if description_filter == "да":
        search_string = input("Введите слово для поиска в описании: ")
        transactions = filter_by_description(transactions, search_string)

    if transactions:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(transactions)}")
        for transaction in transactions:
            display_transaction(transaction)
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()
