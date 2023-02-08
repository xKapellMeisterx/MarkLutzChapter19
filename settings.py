var = ['Hello']
num_settings = 1000


def get_num():
    return num_settings


def get_var():
    return var


def set_num(num: int):
    global num_settings
    num_settings = num

# print(id(var))
# print(id(num_settings))

