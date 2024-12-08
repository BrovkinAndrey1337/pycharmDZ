from masks import get_mask_account, get_mask_card_number

def mask_account_card(account: str)->str:
    masked_number_list = list()
    first_number_index = 0
    for index in range(len(account)):
        if account[index].isdigit():
            first_number_index = index
            break
    masked_number = account[first_number_index:]
    if 'счет' in account.lower():
        masked_deposit_number = get_mask_account(masked_number)
        masked_deposit = account[:first_number_index] + masked_deposit_number
        return masked_deposit
    else:
        masked_card_number = get_mask_card_number(masked_number)
        masked_card = account[:first_number_index] + masked_card_number
        return masked_card
