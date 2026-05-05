import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
import pytest
from src.project_bankapp.widget import get_date, mask_account_card

def test_get_date_with_T():
    assert get_date("2026-05-05T12:34:56") == "2026-05-05"

def test_get_date_without_T():
    assert get_date("2026-05-05") == "2026-05-05"

def test_mask_account_card_long():
    assert mask_account_card("1234567890123456") == "**3456"

def test_mask_account_card_short():
    assert mask_account_card("12345") == "12345"

