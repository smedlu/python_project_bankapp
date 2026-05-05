from typing import Any, Dict, List, cast

import pandas as pd


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
    except Exception as e:
        # В реальном проекте лучше логировать ошибку
        print(f"Ошибка при чтении CSV файла {file_path}: {e}")
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
    except Exception as e:
        # В реальном проекте лучше логировать ошибку
        print(f"Ошибка при чтении Excel файла {file_path}: {e}")
        return []
