from operator import itemgetter

class OpSys:
    """Операционная система"""
    def __init__(self, id, fio, size, pc_id):
        self.id = id
        self.fio = fio
        self.size = size
        self.pc_id = pc_id

class Pc:
    """Компьютер"""
    def __init__(self, id, name):
        self.id = id
        self.name = name


class OpSys_s:
    """
    'Операционные системы' для реализации
    связи многие-ко-многим
    """
    def __init__(self,pc_id,os_id):
        self.os_id = os_id
        self.pc_id = pc_id


# Компьютеры
PCs = [
    Pc(1, 'Игровой компьютер'),
    Pc(2, 'Рабочий компьютер'),
    Pc(3, 'Офисный ноутбук'),
]

# Операционные системы
# Номер / название / количество занимаемой памяти (чистый вес ОС в мб) / установлен на ПК
OSs = [
    OpSys(1, 'MacOs-ов', 32000, 1),
    OpSys(2, 'Windows', 24000, 1),
    OpSys(3, 'Harmony-ов', 41000, 2),
    OpSys(4, '(Linux) Raspbian', 12000, 2),
    OpSys(5, '(Linux) Ubuntu', 15000, 3),
    OpSys(6, '(Linux) Kali-ов', 17000, 3),
]


os_pk = [
    OpSys_s(1, 1),
    OpSys_s(2, 1),
    OpSys_s(3, 2),
    OpSys_s(4, 2),
    OpSys_s(5, 3),
    OpSys_s(6, 3),
]


def main():
    """Основная функция"""

    one_to_many = [(e.fio, e.size, d.name) for d in PCs for e in OSs if e.pc_id == d.id]
    many_to_many_temp = [(d.name, ed.pc_id, ed.pc_id) for d in PCs for ed in os_pk if d.id == ed.pc_id]
    many_to_many = [(e.fio, e.size, orc_name) for orc_name, orc_id, mus_id in many_to_many_temp for e in OSs if e.id == mus_id ]

    print('Задание А1')
    for i in range(len(one_to_many)):
        if one_to_many[i][0][-2:]=="ов":
            print(one_to_many[i][0], one_to_many[i][2])

    print('\nЗадание А2')
    arr = arr1 = []
    for x in PCs:
        # Список ОС
        d_muss = list(filter(lambda i: i[2] == x.name, one_to_many))
        if len(d_muss) > 0:
            # занимаемая память
            d_sals = [sal for _, sal, _ in d_muss]
            # Средний объем занимаемой ОС-ми памяти
            d_sals_sum = sum(d_sals)
            arr.append((x.name, d_sals_sum/len(d_muss)))
            arr1=sorted(arr, key=itemgetter(1), reverse=True)

    for i in arr1:
        print(i[0],i[1].__round__())

    print('\nЗадание А3')
    arr2 = []
    for d in PCs:
        if 'И' in d.name:
            arr2.append(d.id)

    for x in range(int(len(arr2))):
        print(many_to_many[x][2])
        for i in OSs:
            if i.pc_id == arr2[x]:
                print(i.fio)


if __name__ == '__main__':
    main()