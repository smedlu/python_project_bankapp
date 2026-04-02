from project_bankapp.masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """Маскирует информацию о карте или счете."""
    if not info:
        return ""

    parts = info.split()
    number = parts[-1]
    # Собираем название (все элементы, кроме последнего)
    type_name = " ".join(parts[:-1])

    if type_name.lower().startswith("счет"):
        return f"{type_name} {get_mask_account(number)}"
    else:
        return f"{type_name} {get_mask_card_number(number)}"


def get_date(date_string: str) -> str:
    """Преобразует дату в формат ДД.ММ.ГГГГ"""
    if not date_string:
        raise ValueError("Дата не может быть пустой")
    date_part = date_string.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"
