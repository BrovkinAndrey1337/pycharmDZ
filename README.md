# Проект "HOMEWORK 10_1"

Маскировка данных и обработка списков словарей

## Описание

Этот проект предоставляет функции для маскировки номеров карт и аккаунтов, а также для фильтрации и сортировки списков словарей.

## Установка

Скачайте проект по [ссылке](https://github.com/BrovkinAndrey1337/pycharmDZ.git).

## Использование

### Маскировка данных

#### Функция `get_mask_card_number(card_number: str) -> str`
Функция для маскировки номера карты.

##### Параметры:
- `card_number`: Номер карты в виде строки.

##### Возвращаемое значение:
- Маскированный номер карты.

##### Пример использования:
```python
from src.masks import get_mask_card_number

masked_card = get_mask_card_number("1234567890123456")
print(masked_card)  # Вывод: "1234 43** **** 7654"
```
#### Функция `get_mask_account(account: str) -> str:`

##### Параметры:
- `account`: Номер аккаунта в виде строки.

##### Возвращаемое значение:
- Маскированный номер аккаунта.

##### Пример использования:
```python
from src.masks import get_mask_account

masked_account = get_mask_account("1234567890123456")
print(masked_account)  # Вывод: "**3456"
```
#### Функция `get_mask_card_number(card_number: str) -> str:`

##### Параметры:
- `card_number`: Номер счета/карты в виде строки. Также в начале должно быть уточнение, это номер счета или карты, добавляя в начале "Счет" или карту (Например, VISA)

##### Возвращаемое значение:
- Маскированный номер счета/карты.

##### Пример использования:
```python
from src.widget import mask_account_card

masked_account = mask_account_card('Счет 1234432156787654')
print(masked_account)  # Вывод: "Счет **7654"

masked_card = mask_account_card('VISA 1234432156787654')
print(masked_card)  # Вывод: "VISA 1234 43** **** 7654"
```
### Фильтрация списков словарей
#### Функция `def filter_by_state(list_of_dictionaries: List[Dict[str, Union[int, str]]], state: str = "EXECUTED") -> List[Dict[str, Union[int, str]]]:`

##### Параметры:
- list_of_dictionaries: Список словарей, где каждый словарь может содержать различные ключи, включая состояние (state). Значения в словарях могут быть как строками, так и целыми числами.
- state: Необязательный параметр. Строка, представляющая состояние, по которому необходимо фильтровать записи. По умолчанию - 'EXECUTED'
##### Возвращаемое значение:
- Список словарей, содержащий только те записи, которые соответствуют указанному состоянию.

##### Пример использования:
```python
from src.processing import filter_by_state
data = [
    {'id': 1, 'name': 'Item 1', 'state': 'EXECUTED'},
    {'id': 2, 'name': 'Item 2', 'state': 'PENDING'},
    {'id': 3, 'name': 'Item 3', 'state': 'EXECUTED'},
]

filtered_data = filter_by_state(data)
print(filtered_data)  #Вывод: [{'id': 1, 'name': 'Item 1', 'state': 'EXECUTED'}, {'id': 3, 'name': 'Item 3', 'state': 'EXECUTED'}]
```
## Лицензия
Этот проект является открытым и может быть использован, изменён и распространён в соответствии с условиями лицензии MIT.