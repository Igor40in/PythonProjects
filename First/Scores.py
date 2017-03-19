# https://itproger.com/course/python/11
a = set()  # пустое множество
# method 1
a = set('hello')
print(a)
print(type(a))

# method 2
a = {i**2 for i in range(10)} # без значений это множество, а не словарь
print(a)
print(type(a))

# method 3
b = frozenset('Qwerty') # неизменяемое множество
print(b)

a = ['r', 's', 'w', 'a', 's', 'w']
print(a)
print(set(a))

a = {32, 45, 43.23, 76}
print(a.__len__())
print(len(a))
x = 43.23
print(x in a)  # Принадлежит или нет число x множесту a
x = {67, 7, 90}
print(a.isdisjoint(x))  # False если все элементы разные в множествах, иначе True
print(a == x)
x = {76, 32,  43.23, 45}
print(a == x)  # True только если полное соответствие по элементам множества, без учета порядка
x = {723, 12, 32, 76}
A = a.copy()
A.update(x)
B = A.copy()
print(A)
B.intersection_update(x)
print(B)
C = A.copy()
C.difference_update(x)  # выводит непересекающиеся элементы множества A
print(C)
D = A.copy()
D.symmetric_difference_update(x)  # выводит те элементы, которые есть в одном множестве, но нет в каждом
print(D)
A.remove(32)
print(A)
A.discard(32)  # тоже что и remove, только если такого элемента нет в множестве, то не выдает ошибку
print(A)
A.pop()
print(A)  # удаляет первый элемент из множества, но так как множество случайно по индексам то удалится один любой
          # элемент множества
A.clear()
print(A)

