def get_mask_card_number(card_number: str) -> str:
    """Функция для маскрировки номера карты"""
    first_six_numbers = card_number[:6]
    last_four_numbers = card_number[-4:]
    count_of_stars = len(card_number) - 10
    masked_card_number = first_six_numbers + "*" * count_of_stars + last_four_numbers
    masked_card_number_list = list(masked_card_number)
    for index in range(4, len(masked_card_number_list), 5):
        masked_card_number_list.insert(index, " ")
    masked_card_number = "".join(masked_card_number_list)
    return masked_card_number


def get_mask_account(account: str) -> str:
    """Функция для маскрировки номера аккаунта"""
    last_four_numbers = account[-4:]
    masked_account = "*" * 2 + last_four_numbers
    return masked_account
