import json, time, sys, functools
import random
from contextlib import contextmanager

path = 'data_light.json'

with open(path, encoding='utf-8', errors='ignore') as f:
    data = json.load(f)

class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = items
        for k, v in kwargs.items():
            setattr(self, k, v)
        if not hasattr(self, 'ignore_case'):
            self.ignore_case = False

    def __next__(self):
        if self.ignore_case:
            moment_array = [x.lower() for x in self.items]
        else:
            moment_array = self.items
        self.items = []
        for element in moment_array:
            if element not in self.items:
                self.items.append(element)
        return self.items

    def __iter__(self):
        return self

def field(items, *args):
    res = []
    assert len(args) > 0
    for a in range(len(args)):
        for i in range(len(items)):
            try:
                res.append(items[i][args[a]])
            except:
                pass
    return res


def print_result(func):
    @functools.wraps(func)
    def wrapper(*func_args, **func_kwargs):
        print('Результат выполнения функции', func.__name__, ':')
        func_result = func(*func_args, **func_kwargs)
        if isinstance(func_result, int) or isinstance(func_result, str):
            print(func_result)
        elif isinstance(func_result, dict):
            all_keys = list(func_result.keys())
            all_values = list(func_result.values())
            for elem in range(len(all_keys)):
                print(all_keys[elem], '=', all_values[elem])
        elif isinstance(func_result, list):
            for elem in func_result:
                print(elem)
        return func_result

    return wrapper

def filter_func(elem):
    if elem.lower().startswith('программист'):
        return True
    else:
        return False

def add_end_stage(elem):
    elem += ' с опытом Python'
    return elem

@contextmanager
def cm_timer_1():
    start_time = time.time()
    yield 0
    print('===\nВремя выполнения пограммы:', round(time.time() - start_time, 10), 'секунд')

@print_result
def f1(arg):
    return next(Unique(field(arg, "job-name"), ignore_case=True))

@print_result
def f2(arg):
    return list(filter(filter_func, arg))

@print_result
def f3(arg):
    return list(map(add_end_stage, arg))

@print_result
def f4(arg):
    temp = []
    for i in range(len(arg)):
        random_zp = random.randint(100000, 200000)
        temp.append(f', зарплата {random_zp} руб.')
    return list(zip(arg, temp))

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))