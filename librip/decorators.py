# Здесь необходимо реализовать декоратор, print_result который принимает на вход функцию,
# вызывает её, печатает в консоль имя функции, печатает результат и возвращает значение
# Если функция вернула список (list), то значения должны выводиться в столбик
# Если функция вернула словарь (dict), то ключи и значения должны выводить в столбик через знак равно

def print_result(func):
    def decorated(*args, **kwargs):
        print(func.__name__)

        res = func(*args, **kwargs)

        if type(res) is list:
            print("\n".join(map(str, res)))
        elif type(res) is dict:
            print("\n".join(["{}={}".format(str(x), str(res[x])) for x in res]))
        else:
            print(res)
        return res

    return decorated
