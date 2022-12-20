def field(items, *args):
    assert len(args) > 0
    for a in range(len(args)):
        for i in range(len(items)):
            try: print(items[i][args[a]])
            except: print()



goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'}
]


field(goods, "title", "price")