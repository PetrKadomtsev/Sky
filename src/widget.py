from datetime import datetime
def mask_account_card(info: str ) -> str:
    """Функция обработки данных карт и счетов"""

    parts = info.split(' ')
    if len(parts) >3:
        return('Проверьте правильность ввода')


    if len(parts) == 3:
        type_one, type_two, number = parts
        masked_number = f"{type_one} {type_two} {number[:4]} {number[4:6]}** **** {number[-4:]}"
    elif len(parts) == 2:
        type_, number = parts
        if type_.lower() == "счет":
             masked_number = f"Счет **{number[-4:]}"
        else:
            masked_number =  f"{type_} {number[:4]} {number[4:6]}** **** {number[-4:]}"
    return (masked_number)






def get_date(date:str) -> str:
    """фунция конвертауии даты"""
    date_obj = datetime.fromisoformat(date)
    return date_obj.strftime("%d.%m.%y")











