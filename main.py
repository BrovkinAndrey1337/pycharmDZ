from src.widget import mask_account_card

if __name__ == "__main__":
    print("Введите аккаунт")
    card_number = input()
    masked_result = mask_account_card(card_number)
    print(f"Маска: {masked_result}")
