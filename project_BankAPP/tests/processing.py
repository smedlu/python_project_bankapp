from project_bankapp.processing import filter_by_state, sort_by_date

def test_filter_by_state():
    data = [
        {'id': 1, 'state': 'EXECUTED'},
        {'id': 2, 'state': 'CANCELED'},
        {'id': 3, 'state': 'EXECUTED'}
    ]
    # Тестируем фильтрацию по умолчанию (EXECUTED)
    assert filter_by_state(data) == [{'id': 1, 'state': 'EXECUTED'}, {'id': 3, 'state': 'EXECUTED'}]
    # Тестируем фильтрацию по CANCELED
    assert filter_by_state(data, 'CANCELED') == [{'id': 2, 'state': 'CANCELED'}]

def test_sort_by_date():
    data = [
        {'id': 1, 'date': '2019-07-03T18:35:29.512364'},
        {'id': 2, 'date': '2020-10-14T08:21:33.419441'}
    ]
    # Проверяем сортировку от новых к старым (по умолчанию)
    sorted_data = sort_by_date(data)
    assert sorted_data[0]['id'] == 2