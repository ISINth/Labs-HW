# Итератор для удаления дубликатов
class Unique(object):

    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        self.IGNORE_CASE = kwargs.get('ignore_case')
        self.ITEMS = iter(items)
        self.PASSED = set()

    def __next__(self):
        # Нужно реализовать __next__
        while True:
            val = next(self.ITEMS)
            val2 = str(val) if self.IGNORE_CASE else str(val).lower()
            if val2 not in self.PASSED:
                self.PASSED.add(val2)
                return val

    def __iter__(self):
        return self

