from math import sqrt
from typing import Any

from src.decorators import log


def test_log_file() -> None:
    @log(filename="test_sqrt_log.txt")
    def my_sqrt(a: Any) -> float:
        if not (isinstance(a, float) or isinstance(a, int)):
            raise ValueError("Can't get sqrt out of non-number")
        if a >= 0:
            return sqrt(a)
        else:
            raise ValueError("Can't get real sqrt out of negative")

    # Since I'm appending data to file, it's necessary to work with empty one:
    with open("test_sqrt_log.txt", "w", encoding="UTF-8"):
        pass

    my_sqrt(16)

    try:
        my_sqrt(-1)
    except ValueError:
        pass

    with open("test_sqrt_log.txt", "r", encoding="UTF-8") as file:
        assert file.readline() == "my_sqrt ok\n"
        assert file.readline() == "my_sqrt ValueError: 'Can't get real sqrt out of negative'. Inputs: -1, {}\n"


def test_log_console(capsys: Any) -> None:
    @log()
    def divide(a: Any, b: Any) -> float:
        if not (isinstance(a, float) or isinstance(a, int)):
            raise ValueError("Can't divide non-numbers")
        if not (isinstance(b, float) or isinstance(b, int)):
            raise ValueError("Can't divide non-numbers")
        if b == 0:
            raise ZeroDivisionError("Can't divide by zero")
        return a / b

    divide(4, 2)
    captured = capsys.readouterr()
    assert captured.out == "divide ok\n"

    try:
        divide(4, 0)
    except ZeroDivisionError:
        pass
    captured = capsys.readouterr()
    assert captured.out == "divide ZeroDivisionError: 'Can't divide by zero'. Inputs: 4, 0, {}\n"
