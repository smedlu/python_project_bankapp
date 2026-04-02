import pytest
from project_bankapp.decorators import log


def test_log_console_success(capsys):
    """Тест вывода 'ok' в консоль."""

    @log()
    def my_func():
        return True

    my_func()
    captured = capsys.readouterr()
    assert captured.out.strip() == "my_func ok"


def test_log_error_console(capsys):
    """Тест вывода ошибки в консоль."""

    @log()
    def fail_func(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        fail_func(1, 0)

    captured = capsys.readouterr()
    assert "fail_func error: ZeroDivisionError" in captured.out
    assert "Inputs: (1, 0), {}" in captured.out


def test_log_to_file(tmp_path):
    """Тест записи в лог-файл."""
    log_file = tmp_path / "mylog.txt"

    @log(filename=str(log_file))
    def test_file_func():
        return "success"

    test_file_func()
    assert log_file.read_text().strip() == "test_file_func ok"