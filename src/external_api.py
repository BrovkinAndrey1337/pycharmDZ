from datetime import datetime
import requests
import os
from dotenv import load_dotenv
from utils import get_transactions
load_dotenv()

API_KEY = os.getenv('API_KEY')

def convertation(transaction: dict) -> float | None:
    """Конвертирует сумму транзакции в рубли с курсом на сегодняшнюю дату"""
    date_today = datetime.now().strftime("%Y-%m-%d")
    currency_needed = 'RUB'
    amount = float(transaction['operationAmount']['amount'])
    currency_code = transaction['operationAmount']['currency']['code']
    if currency_code == currency_needed:
        return amount
    elif currency_code in ('USD', 'EUR'):
        url = f"https://api.apilayer.com/exchangerates_data/convert?from={currency_code}&to={currency_needed}&amount={amount}&date={date_today}"
        headers = {"apikey": API_KEY}
        try:
            response = requests.get(url, headers=headers)
            data = response.json()
            rate = data['result']
            return float(rate)
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return None
        except KeyError as e:
            print(f"Key error: {e}")
            return None
    else:
        return None
