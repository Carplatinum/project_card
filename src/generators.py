def filter_by_currency(transactions, currency_code):
    """
    Фильтрует транзакции по заданной валюте.
    """
    for transaction in transactions:
        if transaction.get('operationAmount', {}).get('currency', {}).get('code') == currency_code:
            yield transaction


def transaction_descriptions(transactions):
    """
    Генерирует описания транзакций.
    """
    for transaction in transactions:
        yield transaction.get('description', '')


def card_number_generator(start, stop):
    """
    Генерирует номера банковских карт в заданном диапазоне.
    """
    for i in range(start, stop + 1):
        card_number = f"{i:016d}"
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
