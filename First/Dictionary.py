# method 1
d = {'test': 1, 'test2': "Test"}
print(d['test2'])

# method 2
d = dict()  # пустой словарь
d = dict(short="dict", loger="dictionary")
d['short'] = '2345'
print(d)

# method 3
d = dict([(23, 34), (56,87)])
print(d)

# method 4
d = dict.fromkeys(['a', 'b'])
print(d)

d = dict.fromkeys(['a', 'b', 'c'], 1)
print(d)

# method 5
a = {a: a**2 for a in range(7)}
print(d)

person = {'name': {'last_name': 'Иванов', 'first_name': 'Иван', 'middle_name': 'Иванович'},
          'address': ['г. Андрюшки', 'ул. Васильковская д. 23б', 'кв.12'],
          'phone': {'home_phone': '34-67-12', 'mobile_phone': '8-564-345-23-65', 'mobile_phone_2': 'Нет'}}
print(person)
print(person['name']['first_name'])
print(person['address'][1])
print(person['phone']['mobile_phone'])
# methods
print(person.values())
print(person.keys())
res = person.popitem()
print(person)
print(res)

person.clear()
print(person)
