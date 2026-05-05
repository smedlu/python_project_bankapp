import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def convert_to_rub(transaction: dict[str, Any]) -> float:
    """Извлекает сумму и конвертирует в рубли, если валюта USD или EUR."""
    amount_data = transaction.get("operationAmount", {})
    amount = float(amount_data.get("amount", 0))
    currency = amount_data.get("currency", {}).get("code")

    if currency == "RUB":
        return amount

    if currency in ["USD", "EUR"]:
        url = "https://api.apilayer.com/exchangerates_data/convert"
        params = {"to": "RUB", "from": currency, "amount": amount}
        headers = {"apikey": API_KEY}

        try:
            response = requests.get(
                url,
                params=params,
                headers=headers,
                timeout=10

            )
            response.raise_for_status()
            data = response.json()
            return float(data.get("result", 0))
        except (requests.RequestException, ValueError, KeyError):
            return 0.0

    return 0.0
