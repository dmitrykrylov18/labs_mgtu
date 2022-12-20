import time
from contextlib import contextmanager

class cm_timer_1:
    def __init__(self):
        self.start_time = time.time()
        pass

    def __enter__(self):
        return 0

    def __exit__(self, exp_type, exp_value, traceback):
        if exp_type is not None:
            print(exp_type, exp_value, traceback)
        else:
            print(round(time.time() - self.start_time, 1))

@contextmanager
def cm_timer_2():
    start_time = time.time()
    yield 0
    print(round(time.time() - start_time, 1))

with cm_timer_1():
    time.sleep(5.5)

with cm_timer_2():
    time.sleep(5.5)