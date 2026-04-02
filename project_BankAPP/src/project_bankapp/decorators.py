import functools
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор, который логирует вызов функции, результат или ошибку."""
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                _write_log(message, filename)
                return result
            except Exception as e:
                # Разбиваем строку, чтобы она была короче 79 символов
                err_type = type(e).__name__
                message = f"{func.__name__} error: {err_type}. " \
                          f"Inputs: {args}, {kwargs}"
                _write_log(message, filename)
                raise e
        return inner
    return wrapper


def _write_log(message: str, filename: Optional[str]) -> None:
    """Записывает лог в файл или выводит в консоль."""
    if filename:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(message + "\n")
    else:
        print(message)

# Убедись, что после этой строки есть одна пустая строка
