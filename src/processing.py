from typing import List, Dict

def filter_by_state(list_of_dictionaries: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    filtered_dict_list = []
    for item in list_of_dictionaries:
        if item['state'] == state:
            filtered_dict_list.append(item)
    return filtered_dict_list

