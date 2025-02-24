import pytest

@pytest.fixture
def valid_card_numbers():
    return [
        ("1234567890123456", "1234 56** **** 3456"),
        ("9876543210987654", "9876 54** **** 7654")
    ]

@pytest.fixture
def invalid_numbers():
    return [
        "1337",
        "Мяу",
        ""
    ]

@pytest.fixture
def valid_account_numbers():
    return [
        ("12345678901234564444", "**4444"),
        ("98765432109876545656", "**5656")
    ]

@pytest.fixture
def invalid_dates():
    return [
        "",
        "Люблю_чебупели",
    ]

@pytest.fixture
def data_state():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-04-01"},
        {"id": 2, "state": "EXECUTED", "date": "2021-04-01"},
        {"id": 3, "state": "EXECUTED", "date": "2022-12-25"},
        {"id": 4, "state": "PENDING",  "date": "2023-01-15"},
        {"id": 5, "state": "CANCELLED", "date": "2020-04-01"},
    ]

@pytest.fixture
def transaction_data():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 123456789,
            "state": "EXECUTED",
            "date": "2020-01-01T12:00:00.000000",
            "operationAmount": {
                "amount": "5000.00",
                "currency": {
                    "name": "EUR",
                    "code": "EUR"
                }
            },
            "description": "Перевод в евро",
            "from": "Счет 12345678901234567890",
            "to": "Счет 09876543210987654321"
        },
        {
            "id": 987654321,
            "state": "EXECUTED",
            "date": "2021-05-05T15:30:00.000000",
            "operationAmount": {
                "amount": "2500.00",
                "currency": {
                    "name": "JPY",
                    "code": "JPY"
                }
            },
            "description": "Перевод в йенах",
            "from": "Счет 11111111111111111111",
            "to": "Счет 22222222222222222222"
        },
        {
            "id": 111111112,
            "state": "EXECUTED",
            "date": "2022-07-10T09:45:00.000000",
            "operationAmount": {
                "amount": "100.00",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Небольшой перевод",
            "from": "Счет 33333333333333333333",
            "to": "Счет 44444444444444444444"
        }
    ]