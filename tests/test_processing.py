import pytest

from project_bankapp.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_data():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-10T20:30:10.100100"},
        {"id": 2, "state": "CANCELED", "date": "2020-11-15T15:10:05.500500"},
        {"id": 3, "state": "EXECUTED", "date": "2018-01-01T10:00:00.000000"},
    ]


def test_filter_by_state(sample_data):
    """Тест фильтрации по статусу"""
    executed = filter_by_state(sample_data, "EXECUTED")
    assert len(executed) == 2
    assert all(item["state"] == "EXECUTED" for item in executed)


def test_sort_by_date_desc(sample_data):
    """Тест сортировки по дате (по умолчанию — убывание)"""
    sorted_data = sort_by_date(sample_data)
    assert sorted_data[0]["id"] == 2  # 2020 год
    assert sorted_data[-1]["id"] == 3  # 2018 год


def test_sort_by_date_asc(sample_data):
    """Тест сортировки по дате (возрастание)"""
    sorted_data = sort_by_date(sample_data, reverse=False)
    assert sorted_data[0]["id"] == 3
