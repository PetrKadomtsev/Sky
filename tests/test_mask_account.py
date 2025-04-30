from src.masks import get_mask_account


def test_valid_account_number():
    """Проверка корректной маскировки номера счета"""
    assert get_mask_account("40817810099910004312") == "**4312"


def test_short_account_number():
    """Проверка обработки слишком короткого номера счета"""
    assert get_mask_account("4081781009991000") == ("Проверьте"
                                                    " правильность номера счета")


def test_long_account_number():
    """Проверка обработки слишком длинного номера счета"""
    assert get_mask_account("408178100999100043122345") == ("Проверьте "
                                                            "правильность номера счета")


def test_account_number_with_letters():
    """Проверка обработки номера счета с буквами"""
    assert get_mask_account("40817810ABCD0004312X") == ("Проверьте"
                                                        " правильность номера счета")


def test_account_number_with_special_chars():
    """Проверка обработки номера счета со спецсимволами"""
    assert get_mask_account("40817-8100-9910-0043-12") == ("Проверьте"
                                                           " правильность номера счета")


def test_empty_account_number():
    """Проверка обработки пустой строки"""
    assert get_mask_account("") == ("Проверьте правильность"
                                    " номера счета")
