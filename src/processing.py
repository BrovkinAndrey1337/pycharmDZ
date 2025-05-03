from typing import Any, Dict, List, Union

from src.widget import get_date


def filter_by_state(
    list_of_dictionaries: List[Dict[str, Union[int, str]]], state: str = "EXECUTED"
) -> List[Dict[str, Union[int, str]]]:
    """Функция находит список словарей по значению state и возвращает их"""
    filtered_dict_list = []
    for item in list_of_dictionaries:
        if "state" not in item:
            continue
        if item["state"] == state:
            filtered_dict_list.append(item)
    return filtered_dict_list


def sort_by_date(
    list_of_dictionaries: List[Dict[str, Any]], descending: bool = True
) -> List[Dict[str, Any]]:
    """Функция фильтрует список словарей по дате (убывание/возрастание - в зависимости от значения descending, по умолчанию - убывание)"""
    for item in list_of_dictionaries:
        date_str = item.get("date")
        if isinstance(date_str, str):
            try:
                item["date"] = get_date(date_str)
            except ValueError as e:
                raise ValueError(f"Ошибка преобразования даты: {e}")
        else:
            raise ValueError("Поле 'date' должно быть строкой.")

    sorted_dict_list = sorted(
        list_of_dictionaries, key=lambda x: x["date"], reverse=descending
    )
    for item in sorted_dict_list:
        item["date"] = item["date"].strftime("%Y-%m-%d")
    return sorted_dict_list
