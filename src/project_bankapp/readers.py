import pandas as pd
from typing import Any, Dict, List, cast


def read_csv_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Считывает финансовые операции из CSV-файла.

    Args:
        file_path (str): Путь к CSV-файлу.

    Returns:
        List[Dict[str, Any]]: Список словарей с транзакциями.
    """
    try:
        df = pd.read_csv(file_path, sep=';')
        return cast(List[Dict[str, Any]], df.to_dict('records'))
    except Exception:
        return []


def read_excel_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Считывает финансовые операции из Excel-файла.

    Args:
        file_path (str): Путь к Excel-файлу.

    Returns:
        List[Dict[str, Any]]: Список словарей с транзакциями.
    """
    try:
        df = pd.read_excel(file_path)
        return cast(List[Dict[str, Any]], df.to_dict('records'))
    except Exception:
        return []
