import re
from collections import Counter
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


def filter_transactions(transactions: List[Dict], search_string: str) -> List[Dict]:
    """Фильтрует список словарей с банковскими операциями по описанию"""
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


def categorize_transactions(transactions: List[Dict], categories: List):
    """Функция для подсчета кол-ва операций в каждой категории"""
    if not isinstance(transactions, list):
        raise ValueError("transactions должен быть списком словарей")

    if not isinstance(categories, list):
        raise ValueError("categories должен быть списком строк")

    category_count = list()

    for transaction in transactions:
        description = transaction["description"].lower()
        for category in categories:
            if re.search(r"\b" + re.escape(category.lower()) + r"\b", description):
                category_count.append(category)

    category_counter = Counter(category_count)

    return dict(category_counter)
