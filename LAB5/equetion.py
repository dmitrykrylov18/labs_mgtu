from math import sqrt
import sys

def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
        #coef = float(coef_str)
        coef = coef_str
        not_argv = False
    except:
        # Вводим с клавиатуры
        not_argv = True
        print(prompt)
        pass
    if not_argv:
        flag = True
        while flag:
            try:
                coef = float(input())
                flag = False
            except:
                print('Повторите ввод коэффициента')
                pass
    return coef


def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        list[float]: Список корней
    '''
    if type(a) not in [float]:
        raise TypeError("Коэффициент A должен быть положительным float!")

    if type(b) not in [float]:
        raise TypeError("Коэффициент B должен быть неотрицательным float!")

    if type(c) not in [float]:
        raise TypeError("Коэффициент C должен быть неотрицательным float!")

    if a == 0.0 and b == 0.0:
        raise ValueError("Коэффициент A и B должены быть положительными float!")

    result = []
    under_sqrt_mini = b ** 2 - 4 * a * c
    if under_sqrt_mini >= 0:
        under_sqrt_one = (-b + sqrt(under_sqrt_mini)) / 2 * a
        under_sqrt_two = (-b - sqrt(under_sqrt_mini)) / 2 * a
        if under_sqrt_one >= 0:
            result.append(sqrt(under_sqrt_one))
            result.append(-sqrt(under_sqrt_one))
        if under_sqrt_two >= 0:
            result.append(sqrt(under_sqrt_two))
            result.append(-sqrt(under_sqrt_two))
    return result

def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a, b, c)
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корень: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 4:
        print('Четыре корня: {} и {} и {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))


if __name__ == "__main__":
    main()