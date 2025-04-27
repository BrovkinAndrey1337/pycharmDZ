from unittest.mock import patch

import pandas as pd
import pytest

from src.transactions import read_transactions_from_csv, read_transactions_from_excel, filter_transactions, categorize_transactions


def test_read_transactions_from_csv():
    mock_csv_data = pd.DataFrame(
        {
            "date": ["2023-01-01", "2023-01-02"],
            "amount": [100, 200],
            "description": ["Transaction 1", "Transaction 2"],
        }
    )
    expected_result = [
        {"date": "2023-01-01", "amount": 100, "description": "Transaction 1"},
        {"date": "2023-01-02", "amount": 200, "description": "Transaction 2"},
    ]

    with patch("pandas.read_csv", return_value=mock_csv_data):
        result = read_transactions_from_csv("test.csv")
        assert result == expected_result


def test_read_transactions_from_excel():
    mock_excel_data = pd.DataFrame(
        {
            "date": ["2023-01-01", "2023-01-02"],
            "amount": [100, 200],
            "description": ["Transaction 1", "Transaction 2"],
        }
    )

    with patch("pandas.read_excel", return_value=mock_excel_data):
        result = read_transactions_from_excel("test.xlsx")
        expected_result = mock_excel_data.to_dict(orient="records")
        assert result == expected_result


def test_read_transactions_from_csv_exception():
    with patch("pandas.read_csv", side_effect=Exception("Ошибка чтения")):
        with pytest.raises(Exception) as excinfo:
            read_transactions_from_csv("test.csv")
        assert str(excinfo.value) == "Произошла ошибка при чтении файла: Ошибка чтения"


def test_read_transactions_from_excel_exception():
    with patch("pandas.read_excel", side_effect=Exception("Ошибка чтения")):
        with pytest.raises(Exception) as excinfo:
            read_transactions_from_excel("test.xlsx")
        assert str(excinfo.value) == "Произошла ошибка при чтении файла: Ошибка чтения"

def test_filter_transactions():
    transactions = [
        {'id': 1, 'description': 'Оплата за интернет', 'amount': -100},
        {'id': 2, 'description': 'Перевод другу', 'amount': -50},
        {'id': 3, 'description': 'Зарплата за март', 'amount': 1500},
        {'id': 4, 'description': 'Оплата за мобильный телефон', 'amount': -30},
    ]
    result = filter_transactions(transactions, 'оплата')
    assert len(result) == 2
    assert all('оплата' in t['description'].lower() for t in result)

    result = filter_transactions(transactions, 'перевод')
    assert len(result) == 1
    assert result[0]['description'] == 'Перевод другу'

    result = filter_transactions(transactions, 'покупка')
    assert len(result) == 0

    with pytest.raises(ValueError, match="Параметр 'transactions' должен быть списком."):
        filter_transactions({}, 'оплата')

    with pytest.raises(ValueError, match="Параметр 'search_string' должен быть строкой."):
        filter_transactions(transactions, 123)


def test_categorize_transactions():
    transactions = [
        {"description": "Оплата за интернет"},
        {"description": "Перевод средств"},
        {"description": "Оплата за мобильную связь"},
        {"description": "Оплата за интернет"},
        {"description": "Купля товаров"},
    ]

    categories = ["Оплата", "Перевод", "Купля"]

    result = categorize_transactions(transactions, categories)
    assert result == {'Оплата': 3, 'Перевод': 1, 'Купля': 1}


def test_empty_transactions():
    transactions = []
    categories = ["Оплата", "Перевод", "Купля"]

    result = categorize_transactions(transactions, categories)
    assert result == {}


def test_invalid_transactions_type():
    with pytest.raises(ValueError, match="transactions должен быть списком словарей"):
        categorize_transactions("invalid_type", ["Оплата"])

def test_no_matching_categories():
    transactions = [{"description": "Неизвестная операция"}]
    categories = ["Оплата", "Перевод", "Купля"]

    result = categorize_transactions(transactions, categories)
    assert result == {}
