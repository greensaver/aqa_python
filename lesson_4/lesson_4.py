# Задача 1
# Напишіть програму яка запитує в користувача вартість покупок, він їх вводе через пробіл, точна кількість не вказана.
# Вам потрібно до вартості покупок додати 6,5 відсотки податків.
# Потім питаєте чи є в користувача купон на знижку якщо є то питаєте це на суму чи на відсоток і потім віднімаєте суму
# або відсоток відповідно від ціни яку отримали раніше і пишете користувачу кінцеву суму.
#
# завдання з зірочкою не впливає на бал. Округліть суму якщо копійок більше ніж 44 то це буде + 1 гривня, якщо менше.
# то тоді просто відкидаємо копійки від ціни.
# Бажаю вам успіхів в виконанні завдання. Не забутьте скористатись виправленням синтаксису в кінці задачі і перевірити
# чи вона у вас працює.

user_shoping = input("Яка вартість покупок? (вводимо через пробіл) \n").replace(",", ".").split()
user_shoping = [float(i) for i in user_shoping]
user_sum = sum(user_shoping)
print(user_sum)
user_tax = user_sum * (6.5 / 100) + user_sum

user_coupon = input("чи є в користувача купон на знижку? (так/ні) \n").lower()

if user_coupon == "так":
   sum_or_percent = input("це на суму чи на відсоток? (суму/відсоток) \n").lower()
   if sum_or_percent == "суму":
       coupon_sum = float(input("на яку суму? \n"))
       user_tax = user_tax - coupon_sum
       print("До сплати:", round(user_tax, 2))
   elif sum_or_percent == "відсоток":
       coupon_percent = float(input("на який відсоток? \n"))
       user_tax = user_tax - (user_tax * (coupon_percent / 100))
       print("До сплати:", round(user_tax, 2))
   else:
       print("не зрозуміло суму чи відсоток, спробуйте ще раз")

user_tax_rounded = round(user_tax, 0)
user_sum_with_tax = round(user_tax, 2)
rest = user_sum_with_tax - round(user_tax_rounded, 0)

if rest > 0.44:
    user_tax_rounded = user_tax_rounded + 1

print("Тоді до сплати:", user_tax_rounded)

# Задача 2
#
# Переробіть задачу з попереднього уроку враховуючи ваші знання з цього уроку, використайте цикл for in.

# банан, слива кокос, груша пармезан гуталакс

user_str = input("Введіть список продуктів через пробіл (спикок не може бути меньшим 5ти) \n").replace(",", "").title()
prod_list = user_str.split()
# print(type(prod_list))

if len(prod_list) < 5:
    print("ви ввели меньше 5ти продуктів")
    exit()

print("зараз є ось такі продукти в вашому списку:", prod_list)

for i in range(5):
    q = int(input("введіть номер продуктів який купили для того що б видалити \n"))
    if q >= 1 and q <= len(prod_list):
        print("Видаленно:", prod_list.pop(q - 1))
    else:
        print("нема такого, спобуйте ще раз")

    print("зараз є ось такі продукти в вашому списку:", prod_list)

if len(prod_list) == 0:
    print("вже порожньо")
else:
    print("ще є", prod_list)

user_ask = input("Бажаєте додати ще продукти до кошика? (так/ні) \n").title()
if user_ask == "Так":
    user_ask_list = input("Введіть список продуктів через пробіл (спикок не може бути меньшим 5ти) \n").split()
    prod_list.extend(user_ask_list)
    print("Додано ще:", prod_list, "Бувайте")
else:
    print("Бувайте")


# Задача  3
#
# Напишіть програму Банкомат. Втсановіть пін код для користувача(зробимо це константою).
# Запитайте в користувача Пін якщо він введе три рази не вірно то напишіть що карта заблокована.
# Використовуйте цикл while.

password = input("Введіть пароль (у Вас є три спроби) \n")
correct_password = "1"
n = 0

while password != correct_password:
    n += 1
    if n < 3:
        print("Невірний пароль, спробуйте ще раз")
        password = input("Введіть пароль \n")
    else:
        print("Ви вичерпали 3и спроби")
        break
else:
    print("Пароль вірний")

# Задача 4
#
# Напишіть за допомогою f-string та format. Дві стрічки де буде підставлятись імя та вік з зміних
# name = "оЛенА"
# age = 21
# f_string = тут ваш код формата ф-стрінг. | повино вийти -> Я Олена, мені 21 рік
# format_string = тут ваш код формата формат стрінг  | повино вийти -> Я Олена, мені 21 рік
# print(f_string)
# print(format_string)
# Ще по формату https://github.com/Pasha-lt/study/blob/main/format_and_join.py

name = "оЛенА"
age = 21
# знаю, краще зробити для name.title() окрему змінну та можно зробити з циклом)
f_string = f"Я {name.title()}, мені {age} рік"
format_string = """Я {name}, мені {age} рік""".format(name=name.title(), age=age)
print(f_string)
print(format_string)

