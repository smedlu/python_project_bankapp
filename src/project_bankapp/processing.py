import re
from collections import Counter
from typing import Any, Dict, List


def process_bank_search(data: List[Dict[str, Any]],
                        search: str) -> List[Dict[str, Any]]:
    """
    Ищет транзакции по описанию с использованием регулярных выражений.

    Args:
        data (List[Dict[str, Any]]): Список словарей с транзакциями.
        search (str): Строка для поиска в описании.

    Returns:
        List[Dict[str, Any]]: Список транзакций, содержащих строку в описании.
    """
    pattern = re.compile(search, re.IGNORECASE)
    return [transaction for transaction in data
            if 'description' in transaction and
            pattern.search(transaction['description'])]


def process_bank_operations(data: List[Dict[str, Any]],
                            categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций по категориям на основе описания.

    Args:
        data (List[Dict[str, Any]]): Список словарей с транзакциями.
        categories (List[str]): Список категорий для подсчета.

    Returns:
        Dict[str, int]: Словарь с количеством операций по категориям.
    """
    descriptions = [transaction.get('description', '') for transaction in data]
    counter = Counter(descriptions)
    return {category: counter.get(category, 0) for category in categories}
