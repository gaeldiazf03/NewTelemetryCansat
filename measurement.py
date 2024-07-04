from functools import wraps
from time import time


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'{func.__name__} executed in {end - start:.2f} seconds')
        return result
    return wrapper


def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in cache:
            print(f'Calculating {func.__name__} for {args}')
            cache[key] = func(*args, **kwargs)
        else:
            print(f'Retrieving {func.__name__} for {args}')
        return cache[key]
    return wrapper


def singleton(cls):
    instancia = dict()
    
    def wrapper(*args, **kwargs):
        if cls not in instancia:
            instancia[cls] = cls(*args, **kwargs)
        return instancia[cls]

    return wrapper


@measure_time
@memoize
def main(n: int):
    sum: int = 0
    for i in range(1, n):
        sum += i
    return sum


if __name__ == '__main__':
    print(main(10000000))
    print("")
    print(main(10000000))
