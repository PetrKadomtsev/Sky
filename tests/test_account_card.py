import pytest

from src.widget import mask_account_card


@pytest.mark.parametrize("input_str,expected", [
    ("Visa Platinum 1234567812345678", "Visa Platinum 1234 56** **** 5678"),
    ("Maestro 8765432187654321", "Maestro 8765 43** **** 4321"),
    ("Счет 40817810099910004312", "Счет **4312"),
])
def test_valid_masking(input_str, expected):
    """Параметризованный тест корректной маскировки карт и счетов"""
    assert mask_account_card(input_str) == expected


@pytest.mark.parametrize("input_str", [
    "Visa Platinum 12345678",
    "Счет ABCD123456789",
    "Visa",
    "Счет",
    "",
])
def test_invalid_inputs(input_str):
    """Проверка обработки некорректных данных"""
    assert "Проверьте правильность" in mask_account_card(input_str)


def test_masking_card_with_multiple_words():
    """Проверка карт с многословным типом"""
    result = mask_account_card("Visa Gold Classic 1234567812345678")
    assert result == "Visa Gold Classic 1234 56** **** 5678"


def test_masking_account_with_uppercase_keyword():
    """Проверка обработки слова 'Счет' в разных регистрах"""
    result = mask_account_card("СЧЕТ 40817810099910004312")
    assert result == "Счет **4312"
