def filter_by_state(data: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param data: Список словарей с данными о транзакциях.
    :param state: Строковое значение статуса (по умолчанию 'EXECUTED').
    :return: Новый список словарей, соответствующих указанному статусу.
    """
    return [item for item in data if item.get('state') == state]


def sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]:
    """
    Сортирует список словарей по значению ключа 'date'.

    :param data: Список словарей с данными о транзакциях.
    :param reverse: Порядок сортировки (True — убывание, False — возрастание).
    :return: Новый отсортированный список.
    """
    return sorted(
        data,
        key=lambda x: x.get('date', ''),
        reverse=reverse
    )