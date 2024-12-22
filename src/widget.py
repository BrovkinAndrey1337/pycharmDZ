from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account: str) -> str:
    """Функция маскировки аккаунта/счета"""
    if len(account) == 0:
        raise ValueError("Введено пустое значение карты/счета")
    first_number_index = 0
    for index in range(len(account)):
        if account[index].isdigit():
            first_number_index = index
            break
    masked_number = account[first_number_index:]
    if masked_number == account or len(masked_number) == 0:
        raise ValueError("Неверное значение счета/карты")
    if "счет" in account.lower():
        masked_deposit_number = get_mask_account(masked_number)
        masked_deposit = account[:first_number_index] + masked_deposit_number
        return masked_deposit
    else:
        masked_card_number = get_mask_card_number(masked_number)
        masked_card = account[:first_number_index] + masked_card_number
        return masked_card


def get_date(date_string):
    """Функция преобразования даты"""
    if not date_string:
        raise ValueError("Пустая дата")
    date_formats = [
        "%Y-%m-%dT%H:%M:%S.%f",
        "%Y-%m-%d",
        "%d.%m.%Y",
        "%m/%d/%Y",
        "%B %d, %Y",
        "%d-%m-%Y",
        "%m-%d-%Y",
        "%d/%m/%Y",
    ]
    for formats in date_formats:
        try:
            date_object = datetime.strptime(date_string, formats)
            return date_object.strftime("%d.%m.%Y")
        except ValueError:
            continue
    raise ValueError("Неверная дата.")
