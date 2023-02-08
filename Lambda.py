from functools import reduce
from timeit import timeit
from math import factorial

# ------------------------------------------------------
# lambda ФУНКЦИИ.
# ------------------------------------------------------


# # Функция, которая возвращает переданный ей аргумент
# def identify(x):
#     return x
#
#
# print(identify(1))  # Выводит 1
#
# # Аналогичная функция но написанная с использованием lambda
# print((lambda x: x)(1))  # Выводит 1
#
# identify = lambda x: x
# print(identify(1))  # Выводит 1
#
# # Ключевое слово: lambda
# # аргумент lambda функции: x
# # Тело: х

# # (lambda x: x + 1)(2) = lambda 2: 2 + 1
# #                      = 2 + 1
# #                      = 3
#
# amount = lambda x, y: x + y
# print(amount(1, 2))
#
# high_ord_func = lambda x, func: x + func(x)
# print(high_ord_func(2, lambda x: x * x))  # Выводит 6

# ------------------------------------------------------
# lambda НЕ МОЖЕТ СОДЕРЖАТЬ УТВЕРЖДЕНИЯ.
# ------------------------------------------------------

# print((lambda x: assert x == 2)(2))
# print((lambda x: x == 2 return x)(2))
# print((lambda x: pass)(2))
# print((lambda x: x == True if x > 1 else raise Exception('My error!'))(2))

# lambda first: str, last: str: first.title() + " " + last.title()


# ------------------------------------------------------
# lambda И ДЕКОРАТОРЫ.
# ------------------------------------------------------


# def trace(f):
#     def wrap(*args, **kwargs):
#         print(f"[TRACE] func: {f.__name__}, args: {args}, kwargs: {kwargs}")
#         return f(*args, **kwargs)
#
#     return wrap
#
#
# # Применяем декоратор к функции
# @trace
# def add_two(x):
#     return x + 2
#
#
# # Вызов функции
# add_two(3)
#
# # Применение декоратора к lambda функции
# print((trace(lambda x: x ** 2))(3))


# ------------------------------------------------------
# lambda И ЗАМЫКАНИЯ.
# ------------------------------------------------------


# def outer_func(x):
#     y = 4
#
#     def inner_func(z):
#         print(f"x = {x}, y = {y}, z = {z}")
#         return x + y + z
#
#     return inner_func
#
#
# for i in range(3):
#     closure = outer_func(i)
#     print(f"closure({i + 5}) = {closure(i + 5)}")


# Замыкание с использованием lambda функции
# def outer_func(x):
#     y = 4
#     return lambda z: x + y + z
#
#
# for i in range(3):
#     closure = outer_func(i)
#     print(f"closure({i + 5}) = {closure(i + 5)}")


# ------------------------------------------------------
# lambda ИСПОЛЬЗОВАНИЕ В СЦЕНАРИЯХ ВСТРАИВАНИЯ НЕБОЛЬШИХ ПОРЦИЙ КОДА.
# ------------------------------------------------------

# transition_table = [
#     lambda x: x ** 2,  # Внутристрочное определение функции
#     lambda x: x ** 3,
#     lambda x: x ** 4
# ]  # Список из трех вызываемых функций
#
# for f in transition_table:
#     print(f(2))  # Выводит 4, 8, 16
#
# print(transition_table[0](3))  # Выводит 9
#
#
# # Определение именованных функций
# def f1(x):
#     return x ** 2
#
#
# def f2(x):
#     return x ** 3
#
#
# def f3(x):
#     return x ** 4
#
#
# transition_table_for_def = [f1, f2, f3]  # Ссылка по имени
# for f in transition_table_for_def:
#     print(f(2))  # Выводит 4, 8, 16
#
# print(transition_table_for_def[0](3))  # Выводит 9
import sys
from sys import getsizeof

# ------------------------------------------------------
# lambda ПЕРЕКЛЮЧАТЕЛИ ДЛЯ МНОЖЕСТВЕННОГО ВЕТВЛЕНИЯ.
# ------------------------------------------------------

# key = 'got'
# data = {
#     'already': (lambda: 2 + 2),
#     'got': (lambda: 2 * 4),
#     'one': (lambda: 2 ** 6)
# }
#
# print(data[key]())  # Выводит 8
#
#
# # print(getsizeof(data))
#
#
# def f1():
#     return 2 + 2
#
#
# def f2():
#     return 2 * 4
#
#
# def f3():
#     return 2 ** 6
#
#
# key = 'one'
# data = {'already': f1, 'got': f2, 'one': f3}
# print(data[key]())  # Выводит 64
# # print(getsizeof(data))


# ------------------------------------------------------
# КАК НЕ ЗАПУТАТЬ СВОЙ КОД.
# ------------------------------------------------------


# less1 = (lambda x, y: x if x < y else y)
# less2 = (lambda x, y: x if x < y and x > 5 else y)
# print(less1(4, 20))  # Выводит 4
# print(less2(4, 20))  # Выводит 20

# showall = lambda x: print(*x, sep='', end='')
#
# t = showall(['spam\n', 'toast\n', 'eggs\n'])

# Выводит:
# spam
# toast
# eggs


# showall = lambda x: [print(line, end='') for line in x]
# t = showall(['spam\n', 'toast\n', 'eggs\n'])

# Выводит:
# spam
# toast
# eggs

# showall = lambda x: list(map(sys.stdout.write, x))
#
# t = showall(['spam\n', 'toast\n', 'eggs\n'])
# print(t)
# # Выводит:
# # spam
# # toast
# # eggs
# # [5, 6, 5]
#
# showall = lambda x: [sys.stdout.write(line) for line in x]
#
# t = showall(['spam\n', 'toast\n', 'eggs\n'])
# print(t)
# # Выводит:
# # spam
# # toast
# # eggs
# # [5, 6, 5]
# *Выводить из функции можно через print(X), или sys.stdout.write(str(X) + ‘\n’) чтобы обеспечить переносимость выражения.


# num_in_str = lambda x: list(map(str, x))
#
# t = num_in_str([1, 2, 3])
# print(t)  # Выводит: ['1', '2', '3']
#
# num_in_str = lambda x: [str(num) for num in x]
#
# t = num_in_str([1, 2, 3])
# print(t)  # Выводит: ['1', '2', '3']


# ------------------------------------------------------
# ОБЛАСТИ ВИДИМОСТИ lambda.
# ------------------------------------------------------


# def action(x):
#     return lambda y: x + y
#
#
# act = action(99)
# print(act)  # Выводит: <function action.<locals>.<lambda> at 0x000001DC8953E700>
# print(act(2))  # Выводит: 101
#
# action = (lambda x: (lambda y: x + y))
# act = action(99)
# print(act(3))  # Выводит: 102
# print(((lambda x: (lambda y: x + y))(99))(4))  # Выводит: 103


# ------------------------------------------------------
# lambda ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ.
# ------------------------------------------------------


# print(list(map(lambda x: x.upper(), ['cat', 'dog', 'cow'])))  # Выводит ['CAT', 'DOG', 'COW']
# print(list(filter(lambda x: 'o' in x, ['cat', 'dog', 'cow'])))  # Выводит['dog', 'cow']
# print(reduce(lambda acc, x: f'{acc} | {x}', ['cat', 'dog', 'cow']))  # Выводит cat | dog | cow

# ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
# print(sorted(ids))  # Сортировка по строке
# # Выводит       ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
# sorted_ids = sorted(ids, key=lambda x: int(x[2:]))  # Сортировка по числу
# print(sorted_ids)
# # Выводит       ['id1', 'id2', 'id3', 'id22', 'id30', 'id100']

# Когда инструкция передается в виде строки, timeit() нужен полный контекст.
# В примере ниже это обеспечивается вторым аргументом, который
# устанавливает среду, необходимую основной функции для синхронизации.
# print(timeit("factorial(999)", "from math import factorial", number=10))
# Выводит 0.0003509000000000012

# ИСпользование lambda функции делает решение чище,
# более читабельным и быстрее вводится в интерпретаторе.
# print(timeit(lambda: factorial(999), number=10))
# Выводит 0.00033700000000000396


# ------------------------------------------------------
# ОБРАТНЫЕ ВЫЗОВЫ lambda.
# ------------------------------------------------------

# from tkinter import Button, mainloop
#
#
# x = Button(
#     text='Press me',
#     command=(lambda: sys.stdout.write('Spam\n'))
# )
# x.pack()
# mainloop()

# class MyGui:
#     def makewidgets(self):
#         Button(command=(lambda: self.on_press('spam')))
#
#     def on_press(self, message):
#         """...использование message..."""
#
#     pass


# C = lambda f: (
#     lambda *args: (
#         lambda o: (
#             lambda g: {None} | {
#                 None for _ in iter(lambda:
#                                    (lambda G: (not G) or o.append(G.pop()))
#                                    (list((lambda:
#                                           (yield from (g(*o.pop()) for _ in (None,))))())), None)
#             } and o.pop())(f(lambda *a: o.append(a) or next(iter(())))))([args]))
#
# print(C)
