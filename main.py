from src.masks import get_mask_account, get_mask_card_number

print("Введите номер карты")
card_number = input()
print("Введите аккаунт")
account = input()
masked_card_number = get_mask_card_number(card_number)
masked_account = get_mask_account(account)
print(f"Замаскированный номер: {masked_card_number}")
print(f"Замаскированный аккаунт: {masked_account}")
