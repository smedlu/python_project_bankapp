def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты по формату 0000 00** **** 0000.

    Args:
        card_number (str): Номер карты (16 цифр).

    Returns:
        str: Замаскированный номер карты.

    Raises:
        ValueError: Если номер карты не состоит из 16 цифр.
    """
    card_number = card_number.replace(' ', '')
    if not card_number.isdigit() or len(card_number) != 16:
        raise ValueError("Номер карты должен состоять из 16 цифр")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:] }"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счёта по формату **0000.

    Args:
        account_number (str): Номер счёта.

    Returns:
        str: Замаскированный номер счёта.

    Raises:
        ValueError: Если номер счёта содержит менее 4 цифр.
    """
    account_number = account_number.replace(' ', '')
    if not account_number.isdigit() or len(account_number) < 4:
        raise ValueError("Номер счета должен содержать минимум 4 цифры")
    return f"**{account_number[-4:]}"