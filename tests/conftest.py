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
