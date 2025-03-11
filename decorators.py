import functools
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования функций.
    """

    def decorator(func: Callable) -> Callable:
        """
        Внутренний декоратор, который обертывает функцию для логирования.
        """
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """
            Обертка функции, которая выполняет логирование.
            """
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
            except Exception as e:
                log_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                result = None

            if filename:
                with open(filename, 'a') as file:
                    file.write(log_message + "\n")
            else:
                print(log_message)

            return result

        return wrapper

    return decorator
