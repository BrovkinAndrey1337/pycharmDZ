from unittest.mock import patch, mock_open, Mock
import json
from src.utils import get_transactions
from src.external_api import convertation


def test_convertation_rub():
    transaction = {
        "operationAmount": {
            "amount": "1000.00",
            "currency": {
                "code": "RUB"
            }
        }
    }
    assert convertation(transaction) == 1000.00


@patch('src.external_api.requests.get')
def test_convertation_usd(mock_get):
    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {'result': 7500.0}
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {
                "code": "USD"
            }
        }
    }
    assert convertation(transaction) == 7500.00
    mock_get.assert_called_once()


@patch('src.external_api.requests.get')
def test_convertation_eur(mock_get):
    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {'result': 10505.0}
    mock_get.return_value = mock_response
    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {
                "code": "EUR"
            }
        }
    }
    assert convertation(transaction) == 10505.00
    mock_get.assert_called_once()

@patch('src.external_api.requests.get')
def test_convertation_key_error(mock_get):
    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {"wrong_key": 12}
    mock_get.return_value = mock_response
    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {
                "code": "USD"
            }
        }
    }
    assert convertation(transaction) is None
    mock_get.assert_called_once()

def test_get_transactions_valid_file():
    mock_data = [
        {
            "id": 1,
            "state": "EXECUTED",
            "operationAmount": {
                "amount": "100.00",
                "currency": {
                    "code": "RUB"
                }
            }
        },
        {
            "id": 2,
            "state": "EXECUTED",
            "operationAmount": {
                "amount": "200.00",
                "currency": {
                    "code": "USD"
                }
            }
        }
    ]
    with patch("builtins.open", mock_open(read_data=json.dumps(mock_data))) as mock_file:
        transactions = get_transactions('mock_path.json')
        assert transactions == mock_data
        mock_file.assert_called_once_with('mock_path.json', 'r', encoding='utf-8')

def test_get_transactions_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        transactions = get_transactions('non_existent.json')
        assert transactions == []


def test_get_transactions_invalid_json():
    with patch("builtins.open", mock_open(read_data='invalid json')):
        transactions = get_transactions('invalid_json.json')
        assert transactions == []


def test_get_transactions_not_list():
    with patch("builtins.open", mock_open(read_data=json.dumps({"key": "value"}))):
        transactions = get_transactions('not_list.json')
        assert transactions == []


def test_get_transactions_empty_file():
    with patch("builtins.open", mock_open(read_data='[]')):
        transactions = get_transactions('empty_list.json')
        assert transactions == []