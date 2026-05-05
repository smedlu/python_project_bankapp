import json
import os
from typing import Any, List

from .readers import read_csv_transactions, read_excel_transactions


def get_transactions_data(file_path: str) -> List[Any]:
    """
    Загружает данные транзакций из файла.

    Args:
        file_path (str): Путь к файлу.

    Returns:
        List[Any]: Список транзакций.
    """
    if not os.path.exists(file_path):
        return []

    if file_path.endswith('.json'):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    elif file_path.endswith('.csv'):
        return read_csv_transactions(file_path)
    elif file_path.endswith('.xlsx'):
        return read_excel_transactions(file_path)
    else:
        return []
