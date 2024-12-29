import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.mark.parametrize("currency, expected_ids", [
    ('USD', [939719570, 142264268, 111111112]),
    ('EUR', [123456789]),
    ('JPY', [987654321]),
    ('GBP', []),
])

def test_filter_by_currency(transaction_data, currency, expected_ids):
    result = list(filter_by_currency(transaction_data, currency))
    assert len(result) == len(expected_ids)
    assert [transaction['id'] for transaction in result] == expected_ids

def test_filter_by_currency_empty_list():
    result = list(filter_by_currency([], 'USD'))
    assert len(result) == 0
    result = list(filter_by_currency([], 'EUR'))
    assert len(result) == 0


def test_transaction_descriptions(transaction_data):
    expected_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод в евро",
        "Перевод в йенах",
        "Небольшой перевод"
    ]
    result = list(transaction_descriptions(transaction_data))
    assert result == expected_descriptions

def test_transaction_descriptions_empty():
    result = list(transaction_descriptions([]))
    assert result == []


