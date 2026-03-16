import pytest
from project_bankapp.widget import mask_account_card, get_date

@pytest.mark.parametrize("date_string, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2018-07-11T02:26:18.671407", "11.07.2018"),
])
def test_get_date(date_string, expected):
    assert get_date(date_string) == expected

def test_get_date_empty():
    """ЗАКРЫВАЕМ СТРОКУ 23"""
    with pytest.raises(ValueError, match="Дата не может быть пустой"):
        get_date("")

def test_mask_account_card_visa():
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"

def test_mask_account_card_account():
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"

def test_mask_account_card_empty():
    assert mask_account_card("") == ""

def test_mask_account_card_maestro():
    """Дополнительно проверяем другой тип карты"""
    assert mask_account_card("Maestro 1596837493215786") == "Maestro 1596 83** **** 5786"