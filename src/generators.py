from typing import Dict, List

def filter_by_currency(transactions: List[Dict[str, int]], currency: str):
    """Генератор фильтрует транзакции по заданной валюте"""
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction

def transaction_descriptions(transactions):
    """Генератор, который возвращает описание каждой транзакции"""
    for transaction in transactions:
        yield transaction.get("description", "")

def card_number_generator(start: int, end: int):
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    for number in range(start, end + 1):
        card_number = str(number)
        while len(card_number) < 16:
            card_number = '0' + card_number
        formatted_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_number


