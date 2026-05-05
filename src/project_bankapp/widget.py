def get_date(date_str: str) -> str:
    """
    Форматирует дату.

    Args:
        date_str (str): Дата в строке.

    Returns:
        str: Отформатированная дата.
    """
    if 'T' in date_str:
        return date_str.split('T')[0]
    return date_str


def mask_account_card(account: str) -> str:
    """
    Маскирует номер карты или счета.

    Args:
        account (str): Номер карты или счета.

    Returns:
        str: Маскированный номер.
    """
    if len(account) > 10:
        return f"**{account[-4:]}"
    return account
