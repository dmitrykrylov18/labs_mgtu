def fibonacci(n):
    if n >= 1000000:
        yield "Параметр слишком большой! (> 1000000)"
    else:
        a, b = 0, 1
        for i in range(n):
            yield a
            a, b = b, a + b

if __name__ == '__main__':
    print(*fibonacci(10))