import requests
import os
from dotenv import load_dotenv
from typing import Dict

load_dotenv()  # Загрузка переменных окружения


def convert_currency(transaction: Dict) -> float:
    """Конвертирует сумму транзакции из USD или EUR в рубли.
    Если транзакция была в другой валюте, возвращает исходную сумму."""
    currency_code = transaction.get('operationAmount', {}).get('currency', {}).get('code')
    amount = transaction.get('operationAmount', {}).get('amount', 0)

    if currency_code in ['USD', 'EUR']:
        api_key = os.getenv('EXCHANGE_RATE_API_KEY')
        if api_key is None:
            print("Ошибка: отсутствует ключ API")
            return float(amount)

        url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency_code}&symbols=RUB"
        headers = {
            "apikey": api_key
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Вызывает исключение для 4xx или 5xx статусов
            data = response.json()
            if 'rates' not in data or 'RUB' not in data['rates']:
                print("Ошибка: неверный формат ответа от API")
                return float(amount)
            exchange_rate = data['rates']['RUB']
            return float(amount * exchange_rate)  # Явное преобразование к float
        except requests.RequestException as e:
            print(f"Ошибка запроса к API: {e}")
            return float(amount)
    else:
        return float(amount)
