from functools import wraps
from typing import Any, Callable

from src.tools import output


def log(filename: str = "") -> Callable:
    def log_internal(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                res = func(*args, **kwargs)
                output(f"{func.__name__} ok", filename=filename)
            except Exception as ex:
                output(f"{func.__name__} {type(ex).__name__}: '{ex}'. Inputs: ", end="", filename=filename)
                output(*args, kwargs, sep=", ", filename=filename)
                raise ex
            return res

        return wrapper

    return log_internal
