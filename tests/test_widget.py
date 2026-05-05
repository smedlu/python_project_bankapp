import pytest

from project_bankapp.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "date_string, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
    ],
)
def test_get_date(date_string, expected):
    assert get_date(date_string) == expected


def test_get_date_empty():
    """Проверка пустой даты"""
    with pytest.raises(ValueError, match="Дата не может быть пустой"):
        get_date("")


def test_mask_account_card_visa():
    card_info = "Visa Platinum 7000792289606361"
    expected = "Visa Platinum 7000 79** **** 6361"
    assert mask_account_card(card_info) == expected


def test_mask_account_card_account():
    account = "Счет 73654108430135874305"
    expected = "Счет **4305"
    assert mask_account_card(account) == expected


def test_mask_account_card_empty():
    assert mask_account_card("") == ""


def test_mask_account_card_maestro():
    """Дополнительно проверяем другой тип карты"""
    card = "Maestro 1596837493215786"
    expected = "Maestro 1596 83** **** 5786"
    assert mask_account_card(card) == expected
