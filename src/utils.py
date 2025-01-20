import json

def get_transactions(filepath: str) ->list:
    """Извлекает данные о финансовых транзакциях из JSON-файла"""
    try:
        with open(filepath, 'r', encoding = 'utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    if not isinstance(data, list):
        return []
    if not data:
        return []
    return data




