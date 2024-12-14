from datetime import datetime
from typing import Dict, List, Union


def filter_by_state(
    list_of_dictionaries: List[Dict[str, Union[int, str]]], state: str = "EXECUTED"
) -> List[Dict[str, Union[int, str]]]:
    """Функция находит список словарей по значению state и возвращает их"""
    filtered_dict_list = []
    for item in list_of_dictionaries:
        if item["state"] == state:
            filtered_dict_list.append(item)
    return filtered_dict_list


def sort_by_date(
    list_of_dictionaries: List[Dict[str, Union[int, str]]], descending: bool = True
) -> List[Dict[str, Union[int, str]]]:
    """Функция фильтрует список словарей по дате (убывание/возрастание - в зависимости от значения descending, по умолчанию - убывание)"""
    sorted_dict_list = sorted(
        list_of_dictionaries, key=lambda x: x["date"], reverse=descending
    )
    return sorted_dict_list
