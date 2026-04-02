import logging
import os


# --- НАСТРОЙКА ЛОГЕРА ---
ROOT_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(__file__))
)
LOG_DIR = os.path.join(ROOT_DIR, 'logs')

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Настраиваем FileHandler (mode='w' — перезапись)
file_handler = logging.FileHandler(
    os.path.join(LOG_DIR, 'masks.log'),
    mode='w',
    encoding='utf-8'
)
# Разбиваем форматтер на две строки, чтобы уложиться в 79 символов
log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
file_formatter = logging.Formatter(log_format)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


# ------------------------


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты в формате XXXX XX** **** XXXX."""
    logger.info(f"Начало маскировки карты: {card_number}")

    cleaned_number = card_number.replace(" ", "")

    if len(cleaned_number) != 16 or not cleaned_number.isdigit():
        # Переносим длинное сообщение лога
        logger.error(
            f"Ошибка маскировки карты: неверный формат номера '{card_number}'"
        )
        raise ValueError("Номер карты должен состоять из 16 цифр")

    first_part = cleaned_number[:4]
    second_part = cleaned_number[4:6]
    last_part = cleaned_number[-4:]

    masked = f"{first_part} {second_part}** **** {last_part}"
    logger.info(f"Успешно замаскирована карта: {masked}")
    return masked


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета в формате **XXXX."""
    logger.info(f"Начало маскировки счета: {account_number}")

    cleaned_number = account_number.replace(" ", "")

    if len(cleaned_number) < 4 or not cleaned_number.isdigit():
        # Переносим длинное сообщение лога
        logger.error(
            f"Ошибка маскировки счета: неверный формат '{account_number}'"
        )
        raise ValueError("Номер счета должен содержать минимум 4 цифры")

    last_four = cleaned_number[-4:]
    masked = f"**{last_four}"

    logger.info(f"Успешно замаскирован счет: {masked}")
    return masked


