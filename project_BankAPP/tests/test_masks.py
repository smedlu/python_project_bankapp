import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src", "project_bankapp"))

from project_bankapp.masks import get_mask_account, get_mask_card_number  # noqa: E402


class TestMasks(unittest.TestCase):
    """Тесты для функций маскировки карт и счетов"""

    def test_get_mask_card_number(self) -> None:
        """Тест маскировки номеров карт"""
        test_cases = [
            ("7000792289606361", "7000 79** **** 6361"),
            ("7000 7922 8960 6361", "7000 79** **** 6361"),
            ("1234567812345678", "1234 56** **** 5678"),
        ]

        for input_card, expected in test_cases:
            with self.subTest(card=input_card):
                self.assertEqual(get_mask_card_number(input_card), expected)

    def test_get_mask_account(self) -> None:
        """Тест маскировки номеров счетов"""
        test_cases = [
            ("73654108430135874305", "**4305"),
            ("123456789012", "**9012"),
            ("1234", "**1234"),
        ]

        for input_account, expected in test_cases:
            with self.subTest(account=input_account):
                self.assertEqual(get_mask_account(input_account), expected)

    def test_card_number_validation(self) -> None:
        """Тест валидации номера карты"""
        with self.assertRaises(ValueError):
            get_mask_card_number("12345")

        with self.assertRaises(ValueError):
            get_mask_card_number("12345678123456789")

        with self.assertRaises(ValueError):
            get_mask_card_number("1234abcd56789012")

    def test_account_validation(self) -> None:
        """Тест валидации номера счета"""
        with self.assertRaises(ValueError):
            get_mask_account("123")

        with self.assertRaises(ValueError):
            get_mask_account("12ab")


if __name__ == "__main__":
    unittest.main()
