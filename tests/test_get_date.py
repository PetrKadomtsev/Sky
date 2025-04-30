import pytest

from src.widget import get_date


@pytest.mark.parametrize("input_str, expected", [
    ("2018-07-11T02:26:18.671407", "11.07.2018"),
    ("2020-01-01T00:00:00", "01.01.2020"),
    ("1999-12-31T23:59:59", "31.12.1999"),
])
def test_valid_dates(input_str, expected):
    """Проверка корректного преобразования ISO даты в формат дд.мм.гггг"""
    assert get_date(input_str) == expected


@pytest.mark.parametrize("invalid_input", [
    "11.07.2018",
    "2020/01/01",
    "01-01-2020",
    "abc",
    "",
    "2020-13-01T00:00:00",
    "2020-12-32T00:00:00",
])
def test_invalid_dates(invalid_input):
    """Проверка обработки некорректных строк"""
    assert get_date(invalid_input) == "Неверный формат даты"
