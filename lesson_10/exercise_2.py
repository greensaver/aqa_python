# Задача 2
# Візьміть задачу з минулого уроку(
# 3) зробіть функцію як ми робили з додаванням тільки замість двох чисел зробіть три числа і протестуйте її
# всіма трьома методами
# ) модернізуйте її так що кожний раз коли ми її запускаємо те що ми туди передаєм та результат повинно записуватись
# в файл log.txt

# Зверніть увагу на те що в файл повинно дозаписуватись, а не затератись.
# Уявіть що ця функція являється легасі кодом і ви її не можете змінювати,
# тому потрібно використовувати декоратор. Я хотів би бачити таку реалізацію в домашці три функції:
# функція з минулого уроку
# функція що записую текст
# і декоратор


def add_three_numbers(number_1: int | float, number_2: int | float, number_3: int | float) -> int | float:
    result = number_1 + number_2 + number_3
    return result


def log_add_three_numbers(number_1: int | float, number_2: int | float, number_3: int | float, result : int | float):
    with open("log.txt", "a") as file:
        file.write("\n")
        file.write(str(number_1))
        file.write("+")
        file.write(str(number_2))
        file.write("+")
        file.write(str(number_3))
        file.write("=")
        file.write(str(result))
        file.write("\n")


def add_three_numbers_wrapper(func):
    def wrapper(*args):
        original_result = func(*args)
        log_add_three_numbers(*args, original_result)
        return original_result

    return wrapper


@add_three_numbers_wrapper
def add_three_numbers_test(number_1: int | float, number_2: int | float, number_3: int | float):
    result = add_three_numbers(number_1, number_2, number_3)
    return result

