import random

def field(items, *args):
    assert len(args) > 0
    # Необходимо реализовать генератор
    for item in items:
        r = {}
        for arg in args:
            if arg in item:
                if len(args) == 1 and item[arg] != None:
                    yield item[arg]
                else:
                    if item[arg] is not None:
                        r[arg] = item[arg]
        if len(r) > 0 and len(args) > 1:
            yield r


# Генератор списка случайных чисел
# Пример:
# gen_random(1, 3, 5) должен выдать примерно 2, 2, 3, 2, 1
# Hint: реализация занимает 2 строки
def gen_random(begin, end, num_count):
    for _ in range(num_count):
        yield random.randint(begin, end)
