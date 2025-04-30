import pytest

from src.processing import sort_by_date


@pytest.fixture
def sample_data():
    return [
        {"id": 1, "date": "2023-01-01T10:00:00"},
        {"id": 2, "date": "2022-06-15T12:30:00"},
        {"id": 3, "date": "2024-03-20T09:15:00"},
    ]


@pytest.fixture
def same_dates_data():
    return [
        {"id": 1, "date": "2023-05-01T00:00:00"},
        {"id": 2, "date": "2023-05-01T00:00:00"},
        {"id": 3, "date": "2023-05-01T00:00:00"},
    ]


@pytest.fixture
def invalid_date_data():
    return [
        {"id": 1, "date": "2023-13-01T10:00:00"},  # неверный месяц
        {"id": 2, "date": "abc"},                  # не дата
        {"id": 3, "date": ""},                     # пустая строка
    ]


def test_sort_descending(sample_data):
    sorted_data = sort_by_date(sample_data, descending=True)
    dates = [item["date"] for item in sorted_data]
    assert dates == sorted(dates, reverse=True)


def test_sort_ascending(sample_data):
    sorted_data = sort_by_date(sample_data, descending=False)
    dates = [item["date"] for item in sorted_data]
    assert dates == sorted(dates)


def test_same_dates_order(same_dates_data):
    sorted_data = sort_by_date(same_dates_data)
    assert sorted_data == same_dates_data  # порядок не должен измениться


def test_invalid_date_raises(invalid_date_data):
    with pytest.raises(ValueError):
        sort_by_date(invalid_date_data)
