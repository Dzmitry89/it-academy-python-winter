# FizzBuzz
"""
FizzBuzz
Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел,
кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz, а вместо чисел
одновременно кратных и 3 и 5 - FizzBuzz
"""

for num in range(1, 101):
    print('Fizz' * (not num % 3) + 'Buzz' * (not num % 5) or num)

# List practice
"""
Используйте генератор списков чтобы получить следующий:
['ab', 'ac', 'ad', 'bb', 'bc', 'bd']
"""

lst1 = [char1 + char2 for char1 in 'ab' for char2 in 'bcd']
print(lst1)

"""
Используйте на предыдущий список slice чтобы получить следующий:
['ab', 'ad', 'bc']
"""

lst2 = lst1[::2]
print(lst2)

"""
Используйте генератор списков чтобы получить следующий
['1a', '2a', '3a', '4a'].
"""

lst3 = [str(index + 1) + 'a' for index in range(4)]
print(lst3)

"""
Одной строкой удалите элемент  '2a' из прошлого списка
и напечатайте его.
"""

print(lst3.pop(1))
print(lst3)

"""
Скопируйте список и добавьте в него элемент '2a' так,
чтобы в исходном списке этого элемента не было.
"""

lst4 = lst3[:]
lst4.insert(1, '2a')
print(lst4)
print(lst3)

# Tuple practice
"""
Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
"""

tuple1 = tuple([char3 for char3 in 'abc'])
print(tuple1)

"""
Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
"""

tuple2 = 'a', 'b', 'c'
lst5 = list(tuple2)
print(lst5)

"""
Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’
"""

a, b, c = 'a', 2, 'python'
print(a, b, c)

"""
Создайте кортеж из одного элемента, чтобы при итерировании по этому элементы
последовательно выводились значения 1, 2, 3. Убедитесь что len() исходного
кортежа возвращает 1.
"""

tuple3 = ([1, 2, 3],)
for el in tuple3[0]:
    print(el)
print(len(tuple3))

"""
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""
# формула для рассчета количества k одинаковых элементов в массиве n
# выглядит: n!/((n-k)!*k!), в нашем условии n!/(n-2)!*2!=(n*(n-1)*(n-2)!)/
# /((n-2)!*2)=n*(n-1)/2
str1 = '1 1 2 2 2 3 3 3 3 3 3 3 3 10 5 2 1 10 8'
# создание словаря: ключ - число, значение - кол-во повторений
dct = {}
for el in list(str1.split()):
    dct[el] = dct.get(el, 0) + 1
print(sum(num * (num - 1) // 2 for num in list(dct.values())))

"""
Дан список. Выведите те его элементы, которые встречаются в списке только один
раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке
"""

lst = [1, 'd', 3, 'c', 4, 'd', 5, 3, 3, 4, 9, 10]
dct = {}
for el in lst:
    dct[el] = dct.get(el, 0) + 1
print([el for el in lst if dct.get(el) == 1])

"""
Дан список целых чисел. Требуется переместить все ненулевые элементы в левую
часть списка, не меняя их порядок, а все нули - в правую часть. Порядок
ненулевых элементов изменять нельзя, дополнительный список использовать
нельзя, задачу нужно выполнить за один проход по списку. Распечатайте
полученный список.
"""

lst6 = [0, 1, 0, 0, 0, 2, 4, 5, 7, 3, 4, 2, 0, 0, 2, 0, 6, 0]
ind1 = 0
while ind1 < len(lst6) - lst6.count(0):
    if lst6[ind1] == 0:
        lst6.insert(len(lst6) - 1, lst6.pop(ind1))
        continue
    else:
        ind1 += 1
print(lst6)
