from unittest.mock import MagicMock, patch

from project_bankapp.readers import (read_csv_transactions,
                                     read_excel_transactions)


@patch("project_bankapp.readers.pd.read_csv")
def test_read_csv_transactions_success(mock_read_csv):
    """Тест успешного чтения CSV файла."""
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{"id": 1, "amount": 100}]
    mock_read_csv.return_value = mock_df

    result = read_csv_transactions("path/to/file.csv")
    assert result == [{"id": 1, "amount": 100}]
    mock_read_csv.assert_called_once_with("path/to/file.csv", sep=';')


@patch("project_bankapp.readers.pd.read_csv")
def test_read_csv_transactions_error(mock_read_csv):
    """Тест ошибки при чтении CSV файла."""
    mock_read_csv.side_effect = Exception("Read error")

    result = read_csv_transactions("path/to/file.csv")
    assert result == []


@patch("project_bankapp.readers.pd.read_excel")
def test_read_excel_transactions_success(mock_read_excel):
    """Тест успешного чтения Excel файла."""
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{"id": 2, "amount": 200}]
    mock_read_excel.return_value = mock_df

    result = read_excel_transactions("path/to/file.xlsx")
    assert result == [{"id": 2, "amount": 200}]
    mock_read_excel.assert_called_once_with("path/to/file.xlsx")


@patch("project_bankapp.readers.pd.read_excel")
def test_read_excel_transactions_error(mock_read_excel):
    """Тест ошибки при чтении Excel файла."""
    mock_read_excel.side_effect = Exception("Read error")

    result = read_excel_transactions("path/to/file.xlsx")
    assert result == []
