def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты в формате XXXX XX** **** XXXX.

    Args:
        card_number (str): Номер карты (16 цифр).

    Returns:
        str: Замаскированный номер карты.

    Raises:
        ValueError: Если номер карты не состоит из 16 цифр.
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
    Маскирует номер счета в формате **XXXX.

    Args:
        account_number (str): Номер счета.

    Returns:
        str: Замаскированный номер счета.

    Raises:
        ValueError: Если номер счета содержит менее 4 цифр.
    """
    cleaned_number = account_number.replace(" ", "")

    if len(cleaned_number) < 4 or not cleaned_number.isdigit():
        raise ValueError("Номер счета должен содержать минимум 4 цифры")

    last_four = cleaned_number[-4:]
    return f"**{last_four}"
