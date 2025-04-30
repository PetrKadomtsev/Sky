from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """Функция обработки данных карт и счетов"""

    parts = info.split(" ")

    if len(parts) < 2:
        return "Проверьте правильность ввода"

    if parts[0].lower() == "счет":
        number = parts[1]
        masked = get_mask_account(number)
        return f"Счет {masked}" if "Проверьте" not in masked else masked
    else:
        card_type = " ".join(parts[:-1])
        number = parts[-1]
        masked = get_mask_card_number(number)
        return f"{card_type} {masked}" if "Проверьте" not in masked else masked


def get_date(date_str: str) -> str:

    try:
        dt = datetime.fromisoformat(date_str)
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        return "Неверный формат даты"
