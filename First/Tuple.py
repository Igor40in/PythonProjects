a = ()  # пустой котреж
a = (43, 56, 45.23, 'd')  # нельзя изменять
b = [43, 56, 45.23, 'd']
b[0] = 340
print(a)
print(b)

print(a.__sizeof__())
print(b.__sizeof__())

a = tuple("Hello Wolrd")
print(a)

a = "Hello Wolrd"
print(a)

a = "Hello Wolrd", "Welcom", 'Hi', 345  # можно заключить в скобки
print(a)

print(a.count(345))

