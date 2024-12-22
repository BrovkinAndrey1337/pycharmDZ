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
