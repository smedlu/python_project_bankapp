import sys
from pathlib import Path
import pytest

# Добавляем корень проекта в пути поиска
root_path = Path(__file__).resolve().parent.parent
if str(root_path) not in sys.path:
    sys.path.insert(0, str(root_path))

from src.project_bankapp.masks import get_mask_card_number, get_mask_account


# Тесты для маскировки карты
def test_get_mask_card_number_valid():
    """Проверка корректной маскировки карты"""
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    assert get_mask_card_number("7000 7922 8960 6361") == "7000 79** **** 6361"

def test_get_mask_card_number_invalid_length():
    """Проверка ошибки при неверной длине номера карты"""
    with pytest.raises(ValueError, match="Номер карты должен состоять из 16 цифр"):
        get_mask_card_number("12345")

def test_get_mask_card_number_not_digits():
    """Проверка ошибки, если в номере карты есть буквы"""
    with pytest.raises(ValueError, match="Номер карты должен состоять из 16 цифр"):
        get_mask_card_number("700079228960636a")

# Тесты для маскировки счета
def test_get_mask_account_valid():
    """Проверка корректной маскировки счета"""
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("123456789012") == "**9012"

def test_get_mask_account_invalid_length():
    """Проверка ошибки при слишком коротком номере счета"""
    with pytest.raises(ValueError, match="Номер счета должен содержать минимум 4 цифры"):
        get_mask_account("123")

def test_get_mask_account_not_digits():
    """Проверка ошибки, если в номере счета есть буквы"""
    with pytest.raises(ValueError, match="Номер счета должен содержать минимум 4 цифры"):
        get_mask_account("123a")
