import json
import os
from typing import Any


def get_transactions_data(path: str) -> list[dict[str, Any]]:
    """Читает JSON-файл и возвращает список транзакций."""
    if not os.path.exists(path):
        return []

    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, UnicodeDecodeError):
        return []