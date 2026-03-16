import pytest

from project_bankapp.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number_valid():
    """Тест корректной маскировки карты"""
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    assert get_mask_card_number("7000 7922 8960 6361") == "7000 79** **** 6361"

def test_get_mask_card_number_invalid_len():
    """Тест на ошибку длины номера"""
    with pytest.raises(ValueError, match="Номер карты должен состоять из 16 цифр"):
        get_mask_card_number("12345")

def test_get_mask_card_number_not_digit():
    """Тест на наличие букв в номере"""
    with pytest.raises(ValueError, match="Номер карты должен состоять из 16 цифр"):
        get_mask_card_number("700079228960636a")

def test_get_mask_account_valid():
    """Тест корректной маскировки счета"""
    assert get_mask_account("73654108430135874305") == "**4305"

def test_get_mask_account_invalid_len():
    """Тест на слишком короткий номер счета"""
    with pytest.raises(ValueError, match="Номер счета должен содержать минимум 4 цифры"):
        get_mask_account("123")