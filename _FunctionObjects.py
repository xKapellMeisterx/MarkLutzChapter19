def echo(message):  # Имени echo присваивается объект функции
    print(message)


echo('Direct call')  # Вызов объекта через первоначальное имя

# Результат вызова функции echo: Direct call

x = echo  # Теперь x тоже ссылается на объект функции
x('Indirect call!')  # Вызов объекта через имя x путем добавления ()


# Результат вызова функции x: Indirect call!

# def indirect(func, arg):
#     func(arg)  # Вызов переданного объекта путем добавления ()


# indirect(echo, 'Argument call!')  # Передача функции другой функции

# Результат вызова функции indirect: Argument call!


# schedule = [(echo, 'Spam!'), (echo, 'Ham!')]
# for (func, arg) in schedule:
#     func(arg)  # Вызов функции, встроенных в контейнер


# Результат вызова функции func(arg) в цикле:
# Spam!
# Ham!


# schedule = [[echo, 'Spam!'], [echo, 'Ham!']]
# for [func, arg] in schedule:
#     func(arg)  # Вызов функции, встроенных в контейнер

# schedule = [{echo: 'Spam!'}, {echo: 'Ham!'}]
# for func in schedule:
#     it = list(func.items())
#     it[0][0](it[0][1])

# def make(label):  # Создание функции без ее вызова
#     def echo(message):
#         print(label + ':' + message)
#
#     return echo


# f = make('Spam!')  # label в объемлющей области видимости предохраняется
# f('Ham!')  # Вызоав функции, возвращенной make
# # Результат вызова функции f: Spam!:Ham!
# f('Eggs!')


# Результат вызова функции f: Spam!:Eggs!


# def func(a):
#     b = 'spam'
#     return b * a
#
#
# print(func.__name__)
# print(dir(func))
# print(func.__code__)
# print(dir(func.__code__))
# print(func.__code__.co_varnames)
# print(func.__code__.co_argcount)
#
# func.count = 0
# print(func.count)


def f():
    new = 1
    pass


f.new = 1
# print(f.__code__.co_varnames)
# print([x for x in dir(f) if not x.startswith('__')])
print(f.new)
print(f.__code__.co_argcount)
print(f.new is f.__code__.co_varnames)
print(f.new == f.__code__.co_varnames)
