# Итератор для удаления дубликатов
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
        print(self.items)
        return None

    def __iter__(self):
        return self

data = ["a", "A", "b", "B", "a", "A", "b", "B"]
class1 = Unique(data, ignore_case=True)
next(class1)
