
from src.masks import get_mask_card_number


def test_valid_card_number():
    """Проверка корректной маскировки номера карты"""
    assert get_mask_card_number("1234567812345678") == "1234 56** **** 5678"


def test_short_card_number():
    """Проверка обработки номера карты длиной меньше 16 символов"""
    assert get_mask_card_number("12345678") == "Проверьте правильность номера карты"


def test_long_card_number():
    """Проверка обработки номера карты длиной больше 16 символов"""
    assert get_mask_card_number("123456781234567890") == ("Проверьте правильность"
                                                          " номера карты")


def test_card_number_with_letters():
    """Проверка обработки номера карты, содержащего буквы"""
    assert get_mask_card_number("1234abcd5678efgh") == ("Проверьте"
                                                        " правильность номера карты")


def test_card_number_with_special_chars():
    """Проверка обработки номера карты, содержащего специальные символы"""
    assert get_mask_card_number("1234-5678-1234-5678") == ("Проверьте"
                                                           " правильность номера карты")


def test_empty_card_number():
    """Проверка обработки пустой строки"""
    assert get_mask_card_number("") == ("Проверьте правильность"
                                        " номера карты")
