import psutil

from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    r = Rectangle("синего", 3, 2)
    c = Circle("зеленого", 5)
    s = Square("красного", 5)
    print(r)
    print(c)
    print(s)

    total, used, free, percent = psutil.disk_usage("/")
    info = f'---MEMORY---\nTotal: {total // (2 ** 30)} GiB\nUsed: {used // (2 ** 30)} GiB\nFree: {free // (2 ** 30)} GiB'
    print(info)

if __name__ == "__main__":
    main()