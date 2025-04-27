import re
from typing import Dict, List

import pandas as pd


def read_transactions_from_csv(file_path: str):
    """Функция считывания финансовых операций с csv файла и возвращает список словарей"""
    try:
        transactions_info = pd.read_csv(file_path, delimiter=";")
        return transactions_info.to_dict(orient="records")
    except Exception as e:
        raise Exception(f"Произошла ошибка при чтении файла: {e}")


def read_transactions_from_excel(file_path: str):
    """Функция считывания финансовых операций с Excel файла"""
    try:
        df = pd.read_excel(file_path)
        transactions_info = df.to_dict(orient="records")
        return transactions_info
    except Exception as e:
        raise Exception(f"Произошла ошибка при чтении файла: {e}")


def filter_transactions(
    transactions: List[Dict], search_string: str
) -> List[Dict]:
    if not isinstance(transactions, list):
        raise ValueError("Параметр 'transactions' должен быть списком.")
    if not isinstance(search_string, str):
        raise ValueError("Параметр 'search_string' должен быть строкой.")
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)

    filtered_transactions = [
        transaction
        for transaction in transactions
        if isinstance(transaction, dict)
        and "description" in transaction
        and pattern.search(transaction["description"])
    ]

    return filtered_transactions
