# utils/timer.py

import time


def timeit(label: str = None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()

            result = func(*args, **kwargs)

            end = time.time()
            name = label or func.__name__

            print(f"TIME TO {name}: {end - start:.4f}s")

            return result

        return wrapper

    return decorator
