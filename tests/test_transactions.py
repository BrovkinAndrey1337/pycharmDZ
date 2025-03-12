from unittest.mock import patch

import pandas as pd
import pytest

from src.transactions import read_transactions_from_csv, read_transactions_from_excel


def test_read_transactions_from_csv():
    mock_csv_data = pd.DataFrame(
        {
            "date": ["2023-01-01", "2023-01-02"],
            "amount": [100, 200],
            "description": ["Transaction 1", "Transaction 2"],
        }
    )
    with patch("pandas.read_csv", return_value=mock_csv_data):
        result = read_transactions_from_csv("test.csv")
        expected_result = mock_csv_data
        pd.testing.assert_frame_equal(result, expected_result)


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
