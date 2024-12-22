import pytest
from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date
from tests.conftest import invalid_dates, data_state


def test_get_mask_card_number(valid_card_numbers):
    for input_card, expected_output in valid_card_numbers:
        result = get_mask_card_number(input_card)
        assert result == expected_output

def test_invalid_numbers_get_mask_card_number(invalid_numbers):
    for invalid_number in invalid_numbers:
        with pytest.raises(ValueError):
            get_mask_card_number(invalid_number)


def test_get_mask_account(valid_account_numbers):
    for input_card, expected_output in valid_account_numbers:
        result = get_mask_account(input_card)
        assert result == expected_output

def test_invalid_numbers_get_mask_account(invalid_numbers):
    for invalid_number in invalid_numbers:
        with pytest.raises(ValueError):
            get_mask_account(invalid_number)

@pytest.mark.parametrize("account, expected", [
    ("счет 12345678901234563212", "счет **3212"),
    ("карта 9876543210987654", "карта 9876 54** **** 7654"),
    ("счет  ", "Номер карты должен содержать 16 цифр."),
    ("", "Введено пустое значение карты/счета"),
    ("счет abcdefghijklmnop", "Неверное значение счета/карты"),
    ("карта 1234", "Номер карты должен содержать 16 цифр."),
])

def test_mask_account_card(account, expected):
    if "Неверное значение" in expected or "Введено пустое значение" in expected or "должен содержать" in expected:
        with pytest.raises(ValueError):
            mask_account_card(account)
    else:
        result = mask_account_card(account)
        assert result == expected

@pytest.mark.parametrize("input_date, expected_output", [
    ("2023-04-01T12:30:00.000", "01.04.2023"),
    ("2023-04-01", "01.04.2023"),
    ("01.04.2023", "01.04.2023"),
    ("04/01/2023", "01.04.2023"),
    ("April 1, 2023", "01.04.2023"),
    ("01-04-2023", "01.04.2023"),
])

def test_get_date_valid_formats(input_date, expected_output):
    assert get_date(input_date) == expected_output

def test_get_date_invalid_formats(invalid_dates):
    for invalid_date in invalid_dates:
        with pytest.raises(ValueError):
            get_date(invalid_date)

@pytest.mark.parametrize("state, expected_output_state", [
    ("EXECUTED", [
        {"id": 1, "state": "EXECUTED", "date": "2023-04-01"},
        {"id": 2, "state": "EXECUTED", "date": "2021-04-01"},
        {"id": 3, "state": "EXECUTED", "date": "2022-12-25"}
    ]),
    ("PENDING", [{"id": 4, "state": "PENDING", "date": "2023-01-15"}]),
    ("CANCELLED", [{"id": 5, "state": "CANCELLED", "date": "2020-04-01"}]),
    ("NOT_EXIST", []),
])

def test_filter_by_state(data_state, state, expected_output_state):
    result = filter_by_state(data_state, state)  # Вызов вашей функции
    assert result == expected_output_state

@pytest.mark.parametrize("expected_sort_date, descending", [
    (
        [
            {"id": 1, "state": "EXECUTED", "date": "2023-04-01"},
            {"id": 4, "state": "PENDING",  "date": "2023-01-15"},
            {"id": 3, "state": "EXECUTED", "date": "2022-12-25"},
            {"id": 2, "state": "EXECUTED", "date": "2021-04-01"},
            {"id": 5, "state": "CANCELLED", "date": "2020-04-01"},
        ],
        True
    ),
    (
        [
            {"id": 5, "state": "CANCELLED", "date": "2020-04-01"},
            {"id": 2, "state": "EXECUTED", "date": "2021-04-01"},
            {"id": 3, "state": "EXECUTED", "date": "2022-12-25"},
            {"id": 4, "state": "PENDING",  "date": "2023-01-15"},
            {"id": 1, "state": "EXECUTED", "date": "2023-04-01"},
        ],
        False
    ),
])

def test_sort_by_date(data_state, expected_sort_date, descending):
    assert sort_by_date(data_state, descending) == expected_sort_date

@pytest.mark.parametrize("data_invalid", [
    [
        {"id": 1, "state": "EXECUTED", "date": "2023-04-01"},
        {"id": 2, "state": "EXECUTED", "date": "invalid-date"},
        {"id": 3, "state": "EXECUTED", "date": "2022-12-25"},
    ],
    [
        {"id": 1, "state": "EXECUTED", "date": "2023-04-01"},
        {"id": 2, "state": "EXECUTED", "date": "01/04/2023"},
    ],
    [
        {"id": 1, "state": "EXECUTED", "date": "2023-04-01"},
        {"id": 2, "state": "EXECUTED", "date": "2023-04-31"},
    ],
])

def test_sort_by_date_invalid_format(data_invalid):
    with pytest.raises(ValueError):
        sort_by_date(data_invalid)

