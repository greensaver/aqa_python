# Задача 1
# Напишіть программу "Касир в кінотеватрі", яка попросить користувача ввести свій вік (можна використати константу або
# функцію input(), на екран має бути виведено лише одне повідомлення).
# якщо користувачу менше 7 - вивести повідомлення"Де твої батьки?"
# якщо користувачу менше 16 - вивести повідомлення "Це фільм для дорослих!"
# якщо від 16 до 65 то зробіть якесь вітальне повідомлення, на ваш розсуд.якщо користувачу
# більше 65 - вивести повідомлення"Покажіть пенсійне посвідчення!"

age = int(input("Введіть свій вік  \n"))
if age <= 7:
    print("Де твої батьки?")  # виконається коли умова буде Тру.
elif age < 16:
    print("Це фільм для дорослих!")
elif 16 <= age <= 65:
    print("Можна придбати квиток!")
elif age > 65:
    print("Покажіть пенсійне посвідчення!")

# Задача 2
# Текстова в чому різниця між is та ==?

# == це оператор, який перевіряє рівність двуї значень
# is це оператор, який перевіряє ідентичність обьктів по id, (займаному місці в памяті), але потрібно розуміти що для
# оптимізації python кешує маленькі строки та цілі числа в такому випадку id можуть бути однакові, для перевірки
# наглядніше буде використовувати консоль ide.

# Задача 3
# Напишіть програму яка в користувача запитує два числа(можуть бути числа типу інт, а можуть бути в стр).
# Потім запитує це стр чи інт і в залежності від відповіді конкатенує їх або додає і повертає результат
# перемножений на три. якщо після конкатенації отримали 10 то перемноживши на 3 отримаємо 30.

user_num_1 = input("Введіть два числа, спочатку одне і натискаємо Enter, потім друге  \n")
user_num_2 = input()
user_answer = input("це str чи int? \n").lower()

if user_answer == "str":
    res_str = str(user_num_1) + str(user_num_2)
    print(int(res_str) * 3)
elif user_answer == "int":
    res_int = int(user_num_1) + int(user_num_2)
    print(int(res_int) * 3)
else:
    print("Приймається тільки відповідь str або int ")