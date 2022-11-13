# Написать функцию-декоратор для кеширования значений функции
# Написать функцию seq(n)
# n = 0 ....N
# (1 + n) ** n возвращает [x1, x2, x3, , , , xn]

from functools import wraps
import datetime
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time_ns()
        res = func(*args, **kwargs)
        finish = time.time_ns()
        print(finish - start)
        return res

    return wrapper


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        log_msg = f'{datetime.datetime.now():%d.%m.%Y %H:%M:%S}\t'
        log_msg += f'функция: {func.__name__}\t'
        log_msg += f"параметры: {', '.join(map(str, args))}\t"
        res = func(*args, **kwargs)
        log_msg += f'результат: {res}\n'
        with open('log_file.log', 'a', encoding='utf-8') as fp:
            fp.write(log_msg)
        return res

    return wrapper


def cacher(func):
    cach = {}
    @wraps(func)
    def wrapper(*args):
        key = args
        if key not in cach:
            cach[key] = func(*args)
        print(cach)
        return cach[key]

    return wrapper


@timer
@logger
@cacher
def seq(n):
    x = []
    for i in range(0, n, 1):
        x.append((1 + i) ** i)
    return x


def main():
    seq(1)
    seq(2)
    seq(3)
    seq(1)
    seq(100)
    seq(100)


main()