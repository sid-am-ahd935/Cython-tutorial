import time
import random


def generate_nums(n= 100):
    return [random.randint(-n, n) for _ in range(n)]


def timeit(func= None, *args, **kwargs):
    t1 = time.time()
    result = func(*args, **kwargs)
    t2 = time.time()

    return (result, t2-t1)