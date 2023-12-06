# 1) додайте requirements.txt на ваш гіт
# 2) Виберіть будь-яку помилку яка вам подобається і зробіть функцію яка перевіряє на цю помилку(в функції try except)
# 3) зробіть функцію як ми робили з додаванням тільки замість двох чисел зробіть три числа і протестуйте її всіма
# трьома методами
# 4) перепишіть декоратор який заміряє час з уроку в домашку, можете його поклацати, як він працює

import time
from datetime import datetime

# 2)
def check_zero_division_error(x):
    try:
        print(x / 0)
    except ZeroDivisionError:
        print("на нуль не ділиться в пайтоні")
        exit()

print(check_zero_division_error(1 + 10))

# 3)
def add_three_numbers(number_1: int | float, number_2: int | float, number_3: int | float) -> int | float:
    result = number_1 + number_2 + number_3
    return result

# 4)
def time_wrapper(f):
    def wrapper(*arg, **kwarg):
        start = datetime.now()
        result = f(*arg, **kwarg)
        delta_time = datetime.now() - start
        print("Час виконання функції: ", delta_time, "/n")
        return result
    return wrapper

@time_wrapper
def short_sleep():
    print("short_sleep")
    time.sleep(1)

@time_wrapper
def medium_sleep():
    print("medium_sleep")
    time.sleep(5)

@time_wrapper
def long_sleep():
    print("long_sleep")
    time.sleep(10)

short_sleep()
medium_sleep()
long_sleep()
