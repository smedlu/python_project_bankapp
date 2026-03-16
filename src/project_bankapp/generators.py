from typing import Generator, Iterable


def filter_by_currency(transactions: Iterable[dict],
                       currency: str) -> Generator[dict, None, None]:
    """Фильтрует транзакции по заданной валюте."""
    for transaction in transactions:
        amount = transaction.get("operationAmount", {})
        if amount.get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: Iterable[dict]
                             ) -> Generator[str, None, None]:
    """Возвращает описания транзакций по очереди."""
    for transaction in transactions:
        yield transaction.get("description", "Описание отсутствует")


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """Генерирует номера карт в формате XXXX XXXX XXXX XXXX."""
    for number in range(start, stop + 1):
        str_num = f"{number:016}"
        yield f"{str_num[:4]} {str_num[4:8]} {str_num[8:12]} {str_num[12:]}"
