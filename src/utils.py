import json

from src.logger import setup_logger

logger = setup_logger("utils")


def get_transactions(filepath: str) -> list:
    """Извлекает данные о финансовых транзакциях из JSON-файла"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            logger.info("Успешно извлечены транзакции из файла.")
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Ошибка при извлечении транзакций: {e}")
        return []
    if not isinstance(data, list):
        logger.warning("Данные не являются списком.")
        return []
    if not data:
        logger.warning("Список транзакций пуст.")
        return []
    return data
