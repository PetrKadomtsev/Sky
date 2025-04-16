import pytest

from src.processing import filter_by_state

test_data = [
    {"id": 1, "state": "EXECUTED"},
    {"id": 2, "state": "CANCELED"},
    {"id": 3, "state": "EXECUTED"},
    {"id": 4, "state": "PENDING"},
]


@pytest.mark.parametrize("state,expected_ids", [
    ("EXECUTED", [1, 3]),
    ("CANCELED", [2]),
    ("PENDING", [4]),
    ("UNKNOWN", []),
])
def test_filter_by_state(state, expected_ids):
    result = filter_by_state(test_data, state)
    result_ids = [item["id"] for item in result]
    assert result_ids == expected_ids


def test_filter_by_state_default():
    """Проверка фильтрации по умолчанию (EXECUTED)"""
    result = filter_by_state(test_data)
    result_ids = [item["id"] for item in result]
    assert result_ids == [1, 3]
