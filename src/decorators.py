from datetime import datetime
from typing import Any, Callable, Optional
from functools import wraps


def log(filename: Optional[str] = None) -> Callable:
    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                result = func(*args, **kwargs)
                log_message = f"{now} {func.__name__} ok\n"
            except Exception as err:
                log_message = f"{now} {func.__name__} error: {type(err).__name__}. Inputs: {args}, {kwargs}\n"
                result = None
            if filename:
                with open(filename, "a") as file:
                    file.write(log_message)
            else:
                print(log_message)
            return result
        return inner
    return wrapper


@log(filename="my_log.txt")
def my_function(x: int, y: int) -> int:
    """Функция возвращает сумму двух чисел"""
    return x + y


print(my_function(1, "2"))
