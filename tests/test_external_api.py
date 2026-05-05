import pytest
import requests
from unittest.mock import patch

from src.project_bankapp.external_api import convert_to_rub


def test_convert_to_rub_rub():
    transaction = {
        "operationAmount": {"amount": "2500", "currency": {"code": "RUB"}}
    }
    assert convert_to_rub(transaction) == 2500.0


def test_convert_to_rub_usd_to_rub():
    transaction = {
        "operationAmount": {"amount": "100", "currency": {"code": "USD"}}
    }

    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"result": 9150.0}
        mock_get.return_value.raise_for_status.return_value = None

        result = convert_to_rub(transaction)
        assert result == 9150.0
        mock_get.assert_called_once()


def test_convert_to_rub_eur_to_rub():
    transaction = {
        "operationAmount": {"amount": "50", "currency": {"code": "EUR"}}
    }

    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"result": 5123.5}
        mock_get.return_value.raise_for_status.return_value = None

        result = convert_to_rub(transaction)
        assert result == 5123.5
        mock_get.assert_called_once()

def test_convert_to_rub_api_error():
    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}

    with patch("requests.get", side_effect=requests.RequestException):
        result = convert_to_rub(transaction)
        assert result == 0.0