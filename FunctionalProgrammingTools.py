from functools import reduce


# ------------------------------------------------------
# map
# ------------------------------------------------------

# counters = [1, 2, 3, 4]
#
# updated = []
# for x in counters:
#     updated.append(x + 10)
#
# print(updated)
#
#
# def inc(x):
#     return x + 10
#
#
# print(list(map(inc, counters)))
# print(map(inc, counters))
#
#
# def inc(x):
#     return x + 10
#
#
# def mymap(func, seq):
#     res = []
#     for x in seq:
#         res.append(func(x))
#     return res


#
#
# print(list(map(inc, [1, 2, 3])))  # Выводит: [11, 12, 13]
# print(mymap(inc, [1, 2, 3]))     # Выводит: [11, 12, 13]

# print(pow(3, 4))  # Выводит: [1, 8, 81]
#
# print(list(map(pow, [1, 2, 3], [2, 3, 4])))  # Выводит: [1, 8, 81]
#
# print(list(map(print, [1, 2, 3], ['1',  ' 2', '-3'])))  # Выводит: [1, 8, 81]

# print(list(map(inc, [1, 2, 3])))  # Выводит: [11, 12, 13]
#
# print([inc(x) for x in [1, 2, 3]])  # Выводит: [11, 12, 13]

# ------------------------------------------------------
# filter
# ------------------------------------------------------

# Вывести числа > 0 из списка [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

# # Используем функцию filter
# print(list(filter((lambda x: x > 0), range(-5, 5))))  # Выводит: [1, 2, 3, 4]

# # Используем синтаксис спискового включения
# print([x for x in range(-5, 5) if x > 0])  # Выводит: [1, 2, 3, 4]

# # Используем цикл for
# res = []
# for x in range(-5, 5):
#     if x > 0:
#         res.append(x)
# print(res)  # Выводит: [1, 2, 3, 4]

# print(reduce((lambda x, y: x + y), [1, 2, 3, 4]))  # Выводит: 10
#
# print(reduce((lambda x, y: x * y), [1, 2, 3, 4]))  # Выводит: 24

# # Пример с использованием цикла for
# nums = [1, 2, 3, 4]
# res = nums[0]
# for x in nums[1:]:
#     res = res + x

# print(res)  # Выводит: 10

# ------------------------------------------------------
# reduce
# ------------------------------------------------------

# def myreduce(function, seqence):
#     tally = seqence[0]
#     for next in seqence[1:]:
#         tally = function(tally, next)
#     return tally


# print(myreduce((lambda x, y: x + y), [1, 2, 3, 4]))  # Выводит: 10
# print(myreduce((lambda x, y: x * y), [1, 2, 3, 4]))  # Выводит: 24


# print(reduce((lambda x, y: x + y), [1, 2, 3, 4], 5))  # Выводит: 15
# print(reduce((lambda x, y: x + y), [], 5))  # Выводит: 5


# import functools
# import operator
#
# print(functools.reduce(operator.add, [2, 4, 6]))
# print(functools.reduce(operator.sub, [2, 4, 6]))
# print(functools.reduce(operator.is_, [2, 2, 2]))
# nums = [2, 2, 6]
# print(nums[0] is nums[1])
