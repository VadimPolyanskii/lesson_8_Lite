# 1. Выполнить задание уровня ultra-light
# 1/1. Написать свой генератор последовательностей, свой тернарный оператор
x = 25

res = [x**2 if x <= 15 else x-3]
print(res)


# 1/2. Написать свой декоратор
def show_prod(f):
    def wrapper(*args, **kwargs):
        print('Ниже произведение чисел!')
        print(f(*args, **kwargs))
        print('Это было произведение чисел!')
    return wrapper


# Функция произведения чисел
@show_prod
def prod(a,b):
    return a*b


prod(5,10)


# 2. Написать декоратор, замеряющий время выполнение декорируемой функции.
import time


def show_time(f):
    def wrapper(*args, **kwargs):
        print('Время обработки функции: ', time.time(), 'сек.')
    return wrapper


@show_time
def computation_time(a,b):
    return a/b


computation_time(10, 5)


# 3. Сравнить время создания генератора и списка с элементами: натуральные числа
# от 1 до 1000000 (создание объектов оформить в виде функций).

# Создадим список
def nat_num_list(*args):
    num_list = []
    for i in range(1, 1000000):
        num_list.append(i)
    return num_list


# Замерим время
start = time.time()
nut_list = nat_num_list()
stop = time.time()
print('Время создания списка: {} секунд'.format(start-stop))


# Создадим генератор
def nat_num_gen(*args):
    for i in range(1, 1000000):
        yield i


# Замерим время
start = time.time()
nut_num_generator = nat_num_gen()
stop = time.time()
print('Время создания генератора: {} секунд'.format(start-stop))

