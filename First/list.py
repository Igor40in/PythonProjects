l = []  # пустой список

lis = [1, 56, 'x', 34, 2.34, ['S', 't', 'r', 'o', 'k', 'i']]
print(lis)

c = [a + b for a in 'list' if a != 's' for b in 'soup' if b != 'u']
print (c)

l.append(23)
l.append(34)
b = [24, 67]
l.extend(b)
l.insert(1, 56)
l.append(34)
l.remove(34)  # удаляет только первый 34
l.pop(0)
l.append(56)
print(l)
print(l.index(56))
print(l.count(56))
l.sort()
print(l)
l.reverse()
print(l)
l.clear()
print(l)


