import json
import logging
import os
from typing import Any

# --- НАСТРОЙКА ЛОГЕРА ---
# Поднимаемся на 3 уровня из src/project_bankapp/utils.py
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
    os.path.join(LOG_DIR, 'utils.log'),
    mode='w',
    encoding='utf-8'
)

# Выносим формат в переменную, чтобы строка не была слишком длинной
log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
file_formatter = logging.Formatter(log_fmt)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


# ------------------------


def get_transactions_data(path: str) -> list[dict[str, Any]]:
    """Читает JSON-файл и возвращает список транзакций."""
    logger.info(f"Попытка чтения данных из файла: {path}")

    if not os.path.exists(path):
        logger.error(f"Файл не найден по пути: {path}")
        return []

    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)

            if isinstance(data, list):
                logger.info(
                    f"Данные успешно прочитаны. Найдено: {len(data)}"
                )
                return data

            logger.error("Данные в файле не являются списком")
            return []

    except json.JSONDecodeError as e:
        logger.error(f"Ошибка декодирования JSON в файле {path}: {e}")
        return []
    except Exception as e:
        # Разбиваем длинный лог на две строки
        logger.error(
            f"Произошла непредвиденная ошибка при чтении файла {path}: {e}"
        )
        return []
