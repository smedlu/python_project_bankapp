import json
from unittest.mock import mock_open, patch

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


@patch("os.path.exists")
@patch("builtins.open", new_callable=mock_open)
def test_get_transactions_data_invalid_json(mock_file, mock_exists):
    """Тест: файл существует, но содержит некорректный JSON."""
    mock_exists.return_value = True
    mock_file.return_value.read.return_value = '{"invalid": json}'

    with patch("json.load",
               side_effect=json.JSONDecodeError("Invalid JSON", "", 0)):
        result = get_transactions_data("path/to/file.json")
        assert result == []


@patch("os.path.exists")
@patch("builtins.open", new_callable=mock_open)
def test_get_transactions_data_not_list(mock_file, mock_exists):
    """Тест: данные не список."""
    mock_exists.return_value = True

    with patch("json.load",
               return_value={"id": 1, "amount": 100}):
        result = get_transactions_data("path/to/file.json")
        assert result == []


@patch("os.path.exists")
@patch("builtins.open", new_callable=mock_open)
def test_get_transactions_data_unexpected_error(mock_file, mock_exists):
    """Тест: неожиданная ошибка при чтении файла."""
    mock_exists.return_value = True

    with patch("builtins.open", side_effect=Exception("Unexpected error")):
        result = get_transactions_data("path/to/file.json")
        assert result == []
