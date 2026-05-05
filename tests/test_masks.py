import pytest

from project_bankapp.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number_valid():
    """Тест корректной маскировки карты"""
    card = "7000792289606361"
    assert get_mask_card_number(card) == "7000 79** **** 6361"


def test_get_mask_card_number_invalid_len():
    """Тест на ошибку длины номера"""
    with pytest.raises(
        ValueError, match="Номер карты должен состоять из 16 цифр"
    ):
        get_mask_card_number("12345")


def test_get_mask_account_short():
    """Тест маскировки счета"""
    assert get_mask_account("73654108430135874305") == "**4305"


def test_get_mask_account_invalid_len():
    """Тест на слишком короткий номер счета"""
    with pytest.raises(
        ValueError, match="Номер счета должен содержать минимум 4 цифры"
    ):
        get_mask_account("123")
