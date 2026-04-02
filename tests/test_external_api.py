import pytest
from unittest.mock import patch, mock_open
from project_bankapp.utils import get_transactions_data


@patch("os.path.exists")  # 1. Добавляем патч для проверки пути
def test_get_transactions_data_success(mock_exists):
    """Тест успешного чтения корректного JSON."""
    # 2. Говорим моку, что файл как будто существует
    mock_exists.return_value = True

    mock_json_content = '[{"id": 1, "state": "EXECUTED"}]'

    # 3. Мокаем само чтение файла
    with patch("builtins.open", mock_open(read_data=mock_json_content)):
        result = get_transactions_data("fake_path.json")
        assert result == [{"id": 1, "state": "EXECUTED"}]


@patch("os.path.exists")
def test_get_transactions_data_not_found(mock_exists):
    """Тест ситуации, когда файл реально не найден."""
    mock_exists.return_value = False

    result = get_transactions_data("non_existent.json")
    assert result == []