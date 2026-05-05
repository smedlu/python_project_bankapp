import pytest

from src.project_bankapp.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency():
    usd_transactions = [
        {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}},
        {"operationAmount": {"amount": "200", "currency": {"code": "EUR"}}},
        {"operationAmount": {"amount": "300", "currency": {"code": "USD"}}},
    ]
    filtered = list(filter_by_currency(usd_transactions, "USD"))
    assert len(filtered) == 2
    assert filtered[0]["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_empty_or_no_match():
    empty_transactions = []
    no_match = [{"operationAmount": {"currency": {"code": "EUR"}}}] * 3
    assert list(filter_by_currency(empty_transactions, "USD")) == []
    assert list(filter_by_currency(no_match, "USD")) == []

def test_transaction_descriptions():
    transactions = [
        {"description": "Перевод организации"},
        {"description": "Покупка в магазине"},
        {},
    ]
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == [
        "Перевод организации",
        "Покупка в магазине",
        "Описание отсутствует",
    ]

@pytest.mark.parametrize("start, stop, expected", [
    (1, 1, "0000 0000 0000 0001"),
    (999, 999, "0000 0000 0000 0999"),
])
def test_card_number_generator(start, stop, expected):
    gen = card_number_generator(start, stop)
    assert next(gen) == expected