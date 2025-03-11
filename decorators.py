import functools


def log(filename=None):
    """
    Декоратор для логирования функций.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
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
