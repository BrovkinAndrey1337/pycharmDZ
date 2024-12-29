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


@pytest.mark.parametrize("transaction_data, expected_descriptions", [
    (
        [
            {'description': "Перевод организации"},
            {'description': "Перевод со счета на счет"},
            {'description': "Перевод в евро"},
            {'description': "Перевод в йенах"},
            {'description': "Небольшой перевод"}
        ],
        [
            "Перевод организации",
            "Перевод со счета на счет",
            "Перевод в евро",
            "Перевод в йенах",
            "Небольшой перевод"
        ]
    ),
    (
        [
            {'description': "Тестовый перевод 1"},
            {'description': "Тестовый перевод 2"}
        ],
        [
            "Тестовый перевод 1",
            "Тестовый перевод 2"
        ]
    ),
    (
        [{'description': "Перевод без описания"}],
        ["Перевод без описания"]
    ),
    (
        [{'description': ""}],
        [""]
    ),
    (
        [],
        []
    )
])

def test_transaction_descriptions(transaction_data, expected_descriptions):
    result = list(transaction_descriptions(transaction_data))
    assert result == expected_descriptions

@pytest.mark.parametrize("start, end, expected", [
    (0, 5, [
        "0000 0000 0000 0000",
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005"
    ]),
    (10, 15, [
        "0000 0000 0000 0010",
        "0000 0000 0000 0011",
        "0000 0000 0000 0012",
        "0000 0000 0000 0013",
        "0000 0000 0000 0014",
        "0000 0000 0000 0015"
    ]),
    (9995, 10000, [
        "0000 0000 0000 9995",
        "0000 0000 0000 9996",
        "0000 0000 0000 9997",
        "0000 0000 0000 9998",
        "0000 0000 0000 9999",
        "0000 0000 0001 0000"
    ])
])

def test_card_number_generator(start, end, expected):
    result = list(card_number_generator(start, end))
    assert result == expected


