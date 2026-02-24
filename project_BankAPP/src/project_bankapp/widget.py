from project_bankapp.masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """Маскирует информацию о карте или счете."""
    parts = info.split()
    number = parts[-1]
    type_name = " ".join(parts[:-1])

    if type_name.lower().startswith("счет"):
        return f"{type_name} {get_mask_account(number)}"
    else:
        return f"{type_name} {get_mask_card_number(number)}"


def get_date(date_string: str) -> str:
    """Преобразует ISO дату в формат ДД.ММ.ГГГГ."""
    date_part = date_string.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"


if __name__ == "__main__":
    # Проверка работы маскировки
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))

    # Проверка работы даты
    print(get_date("2026-01-11T02:26:18.671407"))  # Должно быть: 11.01.2026
