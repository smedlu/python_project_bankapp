def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты в формате XXXX XX** **** XXXX

    Args:
        card_number (str): Номер карты (16 цифр)

    Returns:
        str: Замаскированный номер карты

    Examples:
        >>> get_mask_card_number("7000792289606361")
        '7000 79** **** 6361'
        >>> get_mask_card_number("7000 7922 8960 6361")
        '7000 79** **** 6361'

    Raises:
        ValueError: Если номер карты не состоит из 16 цифр
    """
    cleaned_number = card_number.replace(" ", "")

    if len(cleaned_number) != 16 or not cleaned_number.isdigit():
        raise ValueError("Номер карты должен состоять из 16 цифр")

    first_part = cleaned_number[:4]
    second_part = cleaned_number[4:6]
    last_part = cleaned_number[-4:]

    return f"{first_part} {second_part}** **** {last_part}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета в формате **XXXX

    Args:
        account_number (str): Номер счета

    Returns:
        str: Замаскированный номер счета

    Examples:
        >>> get_mask_account("73654108430135874305")
        '**4305'
        >>> get_mask_account("123456789012")
        '**9012'

    Raises:
        ValueError: Если номер счета содержит менее 4 цифр
    """
    cleaned_number = account_number.replace(" ", "")

    if len(cleaned_number) < 4 or not cleaned_number.isdigit():
        raise ValueError("Номер счета должен содержать минимум 4 цифры")

    last_four = cleaned_number[-4:]

    return f"**{last_four}"


if __name__ == "__main__":
    print("Маскировка номеров карт:")
    test_cards = [
        "7000792289606361",
        "7000 7922 8960 6361",
        "1234567812345678",
    ]

    for card in test_cards:
        print(get_mask_card_number(card))

    print("\nМаскировка номеров счетов:")
    test_accounts = [
        "73654108430135874305",
        "123456789012",
        "1234",
    ]

    for account in test_accounts:
        print(get_mask_account(account))

    try:
        get_mask_card_number("12345")
    except ValueError as e:
        print(f"\nОшибка карты: {e}")

    try:
        get_mask_account("123")
    except ValueError as e:
        print(f"Ошибка счета: {e}")
