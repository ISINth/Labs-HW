#!/usr/bin/env python3
import json
import sys
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gen import field, gen_random
from librip.iterators import Unique as unique

# Здесь необходимо в переменную path получить
# путь до файла, который был передан при запуске

#assert len(sys.argv) > 0
#path = sys.argv[0]
path = "data_light.json"

with open(path, encoding="utf8") as f:
    data = json.load(f)


# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Важно!
# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов

@print_result
def f1(arg):
    return sorted(unique(list(field(arg, "job-name")), ignore_case=True), key = lambda key: str(key).lower())


@print_result
def f2(arg):
    return list(filter(lambda x: "программист" in x.lower(), arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + " с опытом Python", arg))


@print_result
def f4(arg):
    return list(map(lambda x: "{}, зарплата {} руб.".format(x[0], x[1]),
                    zip(arg, gen_random(100000, 200000, len(arg)))))

with timer():
    f4(f3(f2(f1(data))))
