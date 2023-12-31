# Візьміть дві задачі з попередніх уроків,
# декілька стрічок), друга більш складна і перепишіть
# їх на функції. Памятайте про Атамарність та god object. Там де написано що користувач має щось ввести то перероблюємо
# на функція приймає. Подивіться може можна за допомогою функції спростити код. В домашку вставте будь ласка опис задачі
# (далі(один з наступних уроків) буде домашка вашу домашку покрити тестами, але ми трохи поміняємо варіанти).


# LESSON_1 CASE_5 Стрічкова конкатенація + математика:
# Користувач вводить два числа. Програма повинна вивести два прінти: перший — їхню суму,
# другий об'єднати їх. Якщо в нас числа 5 та 4, то результат повинен бути 9 та 54.

number_1 = input("Після введення числа натискаємо Enter \n")
number_2 = input("")

def foo(inp_1: str, inp_2: str):
    result_1 = int(inp_1) + int(inp_2)
    result_2 = inp_1 + inp_2
    return result_1, result_2

print("Сума:", foo(number_1, number_2))

# LESSON_5 CASE_1 Зробіть словник де буде табличка множення додавання ділення і віднімання чисел від 2 до 9(включно).
# (так як робили на уроці). Ці значення запишіть в словник з відповідними ключами "+", "-", "/", "*"
#
# Коли ви підготуєте це, запитайте в користувача яку табличку він хоче
# побачити (додавання, віднімання, множення, ділення). і виведіть йому цю табличку.

nums_for_calc = [2, 3, 4, 5, 6, 7, 8, 9]
dict_calc = {"+": [], "-": [], "/": [], "*": []}

def calc_sum(i : int, j : int):
    return f"{str(i)} + {str(j)} = {str(i + j)}"
def calc_minus(i : int, j : int):
    return f"{str(i)} - {str(j)} = {str(i - j)}"
def calc_multiply(i : int, j : int):
    return f"{str(i)} * {str(j)} = {str(i * j)}"
def calc_divide(i : int, j : int):
    return f"{str(i)} / {str(j)} = {str(i / j)}"

def fill_dict(x: str):
    for i in nums_for_calc:
        for j in nums_for_calc:
            dict_calc["+"].append(calc_sum(i, j))
            dict_calc["-"].append(calc_minus(i, j))
            dict_calc["/"].append(calc_multiply(i, j))
            dict_calc["*"].append(calc_multiply(i, j))

    return dict_calc[x]

print(fill_dict("+"))
print(fill_dict("-"))
print(fill_dict("*"))
print(fill_dict("/"))