import pytest
from project_bankapp.processing import (
    process_bank_search,
    process_bank_operations
)


@pytest.fixture
def sample_data():
    return [
        {"description": "Перевод с карты на карту"},
        {"description": "Открытие вклада"},
        {"description": "Перевод организации"},
        {"description": "Перевод с карты на карту"},
    ]


def test_process_bank_search(sample_data):
    result = process_bank_search(sample_data, "перевод")
    assert len(result) == 3
    assert all("перевод" in t["description"].lower() for t in result)


def test_process_bank_search_no_match(sample_data):
    result = process_bank_search(sample_data, "неизвестно")
    assert result == []


def test_process_bank_operations(sample_data):
    categories = ["Перевод с карты на карту",
                  "Открытие вклада",
                  "Перевод организации"]
    result = process_bank_operations(sample_data, categories)
    assert result == {
        "Перевод с карты на карту": 2,
        "Открытие вклада": 1,
        "Перевод организации": 1,
    }


def test_process_bank_operations_no_match(sample_data):
    categories = ["Неизвестная категория"]
    result = process_bank_operations(sample_data, categories)
    assert result == {"Неизвестная категория": 0}
