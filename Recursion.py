import sys

# data_list1 = [1, 2, 3, 4, 5]


# ------------------------------------------------------
# СУММИРОВАНИЕ С ПОМОЩЬЮ РЕКУРСИИ.
# ------------------------------------------------------

# def mysum(data_list):
#     if not data_list:
#         return 0
#     else:
#         return data_list[0] + mysum(data_list[1:])  # Рекурсивный вызов самой себя


# sys.setrecursionlimit(7)
# sys.setrecursionlimit(22)

# print(mysum([1, 2, 3, 4, 5]))
# print(mysum([1, 2, 3, 4, 5]))

# ------------------------------------------------------
# СУММИРОВАНИЕ С ПОМОЩЬЮ РЕКУРСИИ. АЛЬТЕРНАТИВНЫЕ ВАРИАНТЫ.
# ------------------------------------------------------

# def mysum(data_list):
#     return 0 if not data_list else data_list[0] + mysum(data_list[1:])  # Использование тернарного выражения
#
#
# print(mysum([]))
# print(mysum([1, 2, 3, 4, 5]))

# def mysum(data_list):
#     return data_list[0] if len(data_list) == 1 else data_list[0] + mysum(data_list[1:])  # Любой тип,
#     # предполагая наличие хотя бы одного элемента
#
#
# print(mysum([1, 2, 3, 4, 5]))
# print(mysum(['s', 'p', 'a', 'm']))
# print(mysum(['spam', 'ham', 'eggs']))
# print(mysum([[1, 2], [2, 3]]))

# ------------------------------------------------------
# СУММИРОВАНИЕ С ПОМОЩЬЮ КОСВЕННОЙ РЕКУРСИИ.
# ------------------------------------------------------


# def mysum(data_list):
#     if not data_list:
#         return 0
#     return nonempty(data_list)
#
#
# def nonempty(data_list):
#     return data_list[0] + mysum(data_list[1:])
#
#
# # sys.setrecursionlimit(7)
# # sys.setrecursionlimit(12)
# print(mysum(data_list1))

# ------------------------------------------------------
# ОШИБКА РЕКУРСИИ.
# ------------------------------------------------------


# # RecursionError
# def recursion():
#     return recursion()
#
#
# recursion()

# def recursion(value):
#     print(value)
#     return recursion(value + 1)
#
#
# recursion(1)

# ------------------------------------------------------
# БАЗОВЫЙ СЛУЧАЙ.
# ------------------------------------------------------

# def recursion(value):
#     print(value)
#     if value < 4:  # Базовый случай.
#         recursion(value + 1)  # Рекурсивный вызов самой себя.
#
#
# recursion(1)

# ------------------------------------------------------
# СТЕК ВЫЗОВОВ.
# ------------------------------------------------------

# print(sys.getrecursionlimit())  # Выводит 1000
#
# sys.setrecursionlimit(1500)
#
# print(sys.getrecursionlimit())  # Выводит 1500
#
#
# def recursion(value):
#     while value > 0:
#         print(value)
#         value = value - 1
#         return recursion(value)
#
#
# recursion(1490)

# ------------------------------------------------------
# АЛЬТЕРНАТИВА ФУНКЦИИ SUM С ИСПОЛЬЗОВАНИЕМ РЕКУРСИИ.
# ------------------------------------------------------

# print(sum(data_list1, 100))
#
# # print(sum.__doc__)
#
#
# def mysum(data_list, start):
#     if not data_list:
#         return start
#     else:
#         return data_list[0] + mysum(data_list[1:], start)  # Рекурсивный вызов самой себя
#
#
# print(mysum(data_list1, 100))


# ------------------------------------------------------
# ОПЕРАТОРЫ ЦИКЛА ИЛИ РЕКУРСИЯ.
# ------------------------------------------------------

# data_list = [1, 2, 3, 4, 5]
# sum = 0
#
# while data_list:
#     sum += data_list[0]
#     data_list = data_list[1:]
#
#
# print(sum)


# data_list = [1, 2, 3, 4, 5]
# sum = 0
#
# for x in data_list:
#     sum += x
#
#
# print(sum)

# ------------------------------------------------------
# ОБРАБОТКА ПРОИЗВОЛЬНЫХ СТРУКТУР С ПОМОЩЬЮ РЕКУРСИИ.
# ------------------------------------------------------


# data_list = [1, [2, [3, 4], 5], 6, [7, 8]]
# data_list2 = [1, [2, [3, [4, [5]]]]]
# data_list3 = [[[[[1], 2], 3], 4], 5]
#
#
# def sumtree(data):
#     tot = 0
#     for x in data:
#         if not isinstance(x, list):
#             tot += x
#         else:
#             tot += sumtree(x)
#     return tot
# #
# #
# print(sumtree(data_list))
# print(sumtree(data_list2))
# print(sumtree(data_list3))


# ------------------------------------------------------
# ОБРАБОТКА ПРОИЗВОЛЬНЫХ СТРУКТУР(ОБХОД В ШИРИНУ).
# ------------------------------------------------------

# data_list = [1, [2, [3, 4], 5], 6, [7, 8]]
# data_list2 = [1, [2, [3, [4, [5]]]]]
# data_list3 = [[[[[1], 2], 3], 4], 5]
#
#
# def sumtree(data):
#     tot = 0
#     items = list(data)
#     while items:
#         front = items.pop(0)
#         if not isinstance(front, list):
#             tot += front
#         else:
#             items.extend(front)
#     return tot
#
#
# print(sumtree(data_list))
# print(sumtree(data_list2))
# print(sumtree(data_list3))


# ------------------------------------------------------
# ОБРАБОТКА ПРОИЗВОЛЬНЫХ СТРУКТУР(ОБХОД В ГЛУБИНУ).
# ------------------------------------------------------

# data_list = [1, [2, [3, 4], 5], 6, [7, 8]]
# data_list2 = [1, [2, [3, [4, [5]]]]]
# data_list3 = [[[[[1], 2], 3], 4], 5]
#
#
# def sumtree(data):
#     tot = 0
#     items = list(data)
#     while items:
#         front = items.pop(0)
#         if not isinstance(front, list):
#             tot += front
#         else:
#             items[:0] = front
#     return tot
#
#
# print(sumtree(data_list))
# print(sumtree(data_list2))
# print(sumtree(data_list3))


# ------------------------------------------------------
# ПРИМЕР ИСПОЛЬЗОВАНИЯ РЕКУРСИИ.
# ------------------------------------------------------


# data = {
#     'C:': {
#         'Python39': ['python.exe', 'python.ini'],
#         'Program Files': {
#             'Java': ['README.txt', 'Welcome.html', 'java.exe'],
#             'MATLAB': ['matlab.bat', 'matlab.exe', 'mcc.bat']
#         },
#         'Windows': {
#             'System32': ['acledit.dll', 'aclui.dll', 'zipfldr.dll']
#         }
#     }
# }
#
#
# def get_files(path, depth=0):
#     for f in path:
#         print(' ' * depth, f)
#         if type(path[f]) == dict:
#             get_files(path[f], depth + 1)
#         else:
#             print(" " * (depth + 1), " ".join(path[f]))
#
#
# get_files(data)
