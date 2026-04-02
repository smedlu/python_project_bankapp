import pytest
from unittest.mock import patch, mock_open
from project_bankapp.utils import get_transactions_data


@patch("os.path.exists")
def test_get_transactions_data_success(mock_exists):
    """Тест успешного чтения: имитируем, что файл есть и он корректен."""
    mock_exists.return_value = True  # Говорим функции: "Файл существует!"
    mock_data = '[{"id": 1, "amount": 100}]'

    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = get_transactions_data("path/to/file.json")
        assert result == [{"id": 1, "amount": 100}]


@patch("os.path.exists")
def test_get_transactions_data_not_found(mock_exists):
    """Тест: файл не найден."""
    mock_exists.return_value = False  # Файла нет
    result = get_transactions_data("non_existent.json")
    assert result == []