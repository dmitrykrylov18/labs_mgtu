# Здесь должна быть реализация декоратора
def print_result(func):
    def function():
        print(func.__name__)
        func_result = func()

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

    return function



@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()
