import pytest

from project_bankapp.generators import (card_number_generator,
                                        filter_by_currency,
                                        transaction_descriptions)


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 1,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Оплата",
        },
        {
            "id": 2,
            "operationAmount": {"currency": {"code": "RUB"}},
            "description": "Перевод",
        },
    ]


def test_filter_by_currency(sample_transactions):
    usd_gen = filter_by_currency(sample_transactions, "USD")
    assert next(usd_gen)["id"] == 1
    with pytest.raises(StopIteration):
        next(usd_gen)


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 2, ["0000 0000 0000 0001", "0000 0000 0000 0002"]),
        (999, 1000, ["0000 0000 0000 0999", "0000 0000 0000 1000"]),
    ],
)
def test_card_number_generator(start, stop, expected):
    assert list(card_number_generator(start, stop)) == expected


def test_filter_by_currency_empty_or_no_match(sample_transactions):
    # Тест на валюту, которой нет в списке
    usd_gen = filter_by_currency(sample_transactions, "EUR")
    assert list(usd_gen) == []

    # Тест на пустой список
    assert list(filter_by_currency([], "USD")) == []


def test_transaction_descriptions(sample_transactions):
    """Тест для проверки описаний транзакций"""
    descriptions = transaction_descriptions(sample_transactions)
    assert next(descriptions) == "Оплата"
    assert next(descriptions) == "Перевод"
