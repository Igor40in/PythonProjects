def func(x):
    def add(a):
        return x + a

    return add
test = func(100)
print(test(200))


def func2():  # функция ничего не возвращает
    pass
print(func2())


def func3(r, w, y = 2):  # аргументы по умолчанию
    res = r + w
    res *=y
    return res

print(func3(2, 4))


def func4(*args):  # ф-ия с произвольным числом параметров
    return args

print(func4('sd', 5, 6))


def func5(**args):  # агументы это кортеж
    return args

print(func5(a=23, b=56, c=90))



