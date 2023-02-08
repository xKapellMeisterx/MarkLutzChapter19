import operator
import pydoc
import inspect
from copy import copy
import time

# ------------------------------------------------------
# СВЯЗАННОСТЬ
# ------------------------------------------------------

# Не правильно.
from functools import wraps
from typing import Callable, Tuple, Any, Union, Literal

from settings import num_settings, var, get_num, get_var, set_num

num = 1

print(var)
print(id(var))


# print(num_settings)
# print(id(num_settings))13


def change_var_or_num():
    var.append('World')
    global num
    num += 1
    global num_settings
    num_settings += 1000


change_var_or_num()
# --------------------
print(var)
print(id(var))
print(get_var())
print(id(get_var()))

# ---------------------
# print(num_settings)
# print(id(num_settings))
# print(get_num())
# print(id(get_num()))


# set_num(2000)
# print(get_num())
# print(id(get_num()))


# Правильно

# var = ['Hello']
#
#
# def change_var(var_to_change):
#     new_var = copy(var_to_change)
#     new_var.append('World')
#     return new_var
#
#
# print(change_var(var))
# print(var)

# ------------------------------------------------------
# СЦЕПЛЕНИЕ
# ------------------------------------------------------

# Не правильно.

# line1 = '1'
# line2 = '2'


# Функция изменяет переменную типа данных str в int И складывает числа.
# def sum_nums(line1: str, line2: str) -> int:
#     num1, num2 = map(int, [line1, line2])
#     return num1 + num2
#
#
# print(sum_nums(line1, line2))

# Правильно.


# def convert_to_int(line_to_convert: str) -> int:
#     num: int = int(line_to_convert)
#     return num
#
#
# def sum_nums(num1: int, num2: int) -> int:
#     return num1 + num2


# print(convert_to_int(line1))
# print(sum_nums(convert_to_int(line1), convert_to_int(line2)))


# ------------------------------------------------------
# РАЗМЕР
# ------------------------------------------------------


# line_1 = '1'
# line_2 = '2'
#
#
# # Не правильно.
#
#
# def sum_nums(line1: str, line2: str) -> int:
#     num_1 = int(line1)
#     num_2 = int(line2)
#
#     def addition(num1: int, num2: int) -> int:
#         res = num1 + num2
#         return res
#
#     result = addition(num_1, num_2)
#     return result
#
#
# print(sum_nums(line_1, line_2))
#
#
# Правильно


# def sum_nums(foo: Callable) -> Callable[[tuple[Any, ...]], int]:
#     @wraps(foo)
#     def wraper(*args) -> int:
#         return sum(foo(*args))
#     return wraper
#
#
# @sum_nums
# def convert_to_int(*args) -> list:
#     return list(map(int, *args))
#
#
# print(convert_to_int(('1', '2')))
# # print(convert_to_int('1', '2'))

# ------------------------------------------------------
# АННОТАЦИЯ
# ------------------------------------------------------

# line1 = '1'
# line2 = '2'
#
#
# def sum_nums(num1: int, num2: int) -> int:
#     """Функция сложения чисел"""
#     ...
#
#     return num1 + num2
#
#
# def sum_string(num1: str, num2: str) -> str:
#     """Функция сложения строк"""
#
#     return num1 + num2
#
#
# print(sum_string(line1, line2))


# ------------------------------------------------------
# ДОСТУП К АННОТАЦИЯМ
# ------------------------------------------------------

# def func(a: 'spam', b: (1, 10), c: float) -> int:
#     return a + b + c
#
#
# print(func.__annotations__)


# Результат вызова print(func.__annotations__):
# {'a': 'spam', 'b': (1, 10), 'c': <class 'float'>, 'return': <class 'int'>}


# def func(a: 'spam' = 4, b: (1, 10) = 5, c: float = 1) -> int:
#     return a + b + c
#
#
# print(func(1, c=3))
# # Результат вызова print(func(1, c=3)):
# # 9


# def func(a: 'spam', b, c: 99):
#     return a + b + c
#
#
# print(func.__annotations__)
# # Результат вызова print(func.__annotations__):
# # {'a': 'spam', 'c': 99}
#
# for arg in func.__annotations__:
#     print(arg, '=>', func.__annotations__[arg])
#
# # Результат вызова print(arg, '=>', func.__annotations__[arg]) в цикле:
# # a => spam
# # c => 99


# ------------------------------------------------------
# АННОТАЦИЯ (python -m pydoc '1)...
# ------------------------------------------------------


# line1 = '1'
# line2 = '2'
#
#
# def sum_nums(num1: int, num2: int) -> int:
#     """Функция сложения чисел"""
#     ...
#
#     return num1 + num2
#
#
# print(inspect.getfullargspec(sum_nums))


# def foo(*args, var: str = 'me', **kwargs):
#     pass
#
#
# fullargs = inspect.getfullargspec(foo)
# print(fullargs)
