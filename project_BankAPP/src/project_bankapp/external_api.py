import os
import requests
from dotenv import load_dotenv
from typing import Any

# Загружаем переменные из .env
load_dotenv()
API_KEY = os.getenv("API_KEY")


def convert_to_rub(transaction: dict[str, Any]) -> float:
    """Извлекает сумму и конвертирует в рубли, если валюта USD или EUR."""
    amount = float(transaction.get("operationAmount", {}).get("amount", 0))
    currency = transaction.get("operationAmount", {}).get("currency", {}).get("code")

    if currency == "RUB":
        return amount

    if currency in ["USD", "EUR"]:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        headers = {"apikey": API_KEY}

        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            return float(data.get("result", 0))
        except (requests.RequestException, ValueError, KeyError):
            return 0.0

    return 0.0