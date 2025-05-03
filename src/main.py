from typing import Any, Dict, List

from src.generators import filter_by_currency
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.transactions import (
    filter_transactions,
    read_transactions_from_csv,
    read_transactions_from_excel,
)
from src.utils import get_transactions


def print_transactions(transactions: List[Dict[str, Any]]):
    """Выводит транзакции в заданном формате"""
    for transaction in transactions:
        date = transaction.get("date")
        if date is not None:
            date = date.split("T")[0]
        description = transaction.get("description")
        operation_amount = transaction.get("operationAmount", {})
        currency = operation_amount.get("currency", {}).get("name")
        amount = operation_amount.get("amount")

        from_account = transaction.get("from")
        to_account = transaction.get("to")

        if from_account and to_account:
            from_type = "Счет" if "Счет" in from_account else from_account.split()[0]
            masked_from = (
                get_mask_card_number(from_account)
                if "Счет" not in from_account
                else get_mask_account(from_account)
            )
            to_type = "Счет" if "Счет" in to_account else to_account.split()[0]
            masked_to = (
                get_mask_card_number(to_account)
                if "Счет" not in to_account
                else get_mask_account(to_account)
            )
            print(
                f"{date} {description}\n{from_type} {masked_from} -> {to_type} {masked_to}\nСумма: {amount} {currency}\n"
            )
        elif from_account:
            masked_from = (
                get_mask_card_number(from_account)
                if "Счет" not in from_account
                else get_mask_account(from_account)
            )
            print(f"{date} {description}\n{masked_from}\nСумма: {amount} {currency}\n")
        elif to_account:
            masked_to = (
                get_mask_card_number(to_account)
                if "Счет" not in to_account
                else get_mask_account(to_account)
            )
            print(f"{date} {description}\n{masked_to}\nСумма: {amount} {currency}\n")
        else:
            print(
                f"{date} {description}\nНет данных о счетах\nСумма: {amount} {currency}\n"
            )


if __name__ == "__main__":
    answer_sort_by_date = False
    while True:
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        choice = input("Пользователь: ")

        transactions = []
        if choice == "1":
            try:
                transactions = get_transactions("../data/operations.json")
                print("Для обработки выбран JSON-файл.")
            except Exception as e:
                print(e)
            break
        elif choice == "2":
            try:
                transactions = read_transactions_from_csv("../data/transactions.csv")
                print("Для обработки выбран CSV-файл.")
            except Exception as e:
                print(e)
            break
        elif choice == "3":
            try:
                transactions = read_transactions_from_excel(
                    "../data/transactions_excel.xlsx"
                )
                print("Для обработки выбран XLSX-файл.")
            except Exception as e:
                print(e)
            break
        else:
            print("Выбранного варианта ответа нет. Пожалуйста, выберите 1, 2 или 3.")

    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию (EXECUTED, CANCELED, PENDING): "
        )
        if status.upper() in valid_statuses:
            transactions = filter_by_state(transactions, status.upper())
            break
        else:
            print(f"Статус операции {status} недоступен.")
            continue

    while True:
        answer_date = input("Отсортировать по дате? Да/Нет\n")
        if answer_date.lower() == "да":
            answer_sort_by_date = True
            break
        elif answer_date.lower() == "нет":
            break
        else:
            print("Выберите либо да, либо нет")
            continue

    if answer_sort_by_date:
        while True:
            answer_date = input("Отсортировать по возрастанию/убыванию?\n")
            if answer_date.lower() == "по возрастанию":
                try:
                    transactions = sort_by_date(transactions, True)
                    break
                except Exception as e:
                    print(e)
            elif answer_date.lower() == "по убыванию":
                try:
                    transactions = sort_by_date(transactions, False)
                    break
                except Exception as e:
                    print(e)
            else:
                print("Выберите либо по возрастанию, либо по убыванию")
                continue

    while True:
        answer_rubles = input("Выводить только рублевые транзакции? Да/Нет\n")
        if answer_rubles.lower() == "да":
            try:
                transactions = list(filter_by_currency(transactions, "RUB"))
                break
            except Exception as e:
                print(e)
        elif answer_date.lower() == "нет":
            break
        else:
            print("Выберите либо да, либо нет")
            continue

    while True:
        answer_description_bool = input(
            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n"
        )
        if answer_description_bool.lower() == "да":
            try:
                answer_description = input("Введите необходимое слово\n")
                transactions = filter_transactions(transactions, answer_description)
                break
            except Exception as e:
                print(e)
        elif answer_description_bool.lower() == "нет":
            break
        else:
            print("Выберите либо да, либо нет")
            continue

    if len(transactions) != 0:
        print(
            f"Распечатываю итоговый список транзакций...\nВсего банковских операций в выборке: {len(transactions)}\n"
        )
        print_transactions(transactions)
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
