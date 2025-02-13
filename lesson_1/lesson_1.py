# 1 Арифметичні операції:
# Написати програму, яка зчитує два числа та виводить їхню суму, різницю, добуток та частку.
x = int(input("Введіть 2а числа. Після введення числа натискаємо Enter \n"))
y = int(input())
sum = x + y
difference = x - y
product = x * y
quotient = x / y
print(sum, difference, product, quotient)

# 2 Залишок від ділення:
# Користувач вводить два числа. Вивести залишок від ділення першого числа на друге.
remainder = int(input("Введіть 2а числа. Після введення числа натискаємо Enter \n")) % int(input())
print(remainder)

# 3 Цілочисельне ділення:
# Користувач вводить два числа. Вивести, скільки разів перше число ділиться на друге без залишку.
withoutRemainder = int(input("Після введення числа натискаємо Enter \n")) // int(input())
print(withoutRemainder)

# 4 Перетворення стрічки у число:
# Користувач вводить рядок, який складається з цифр. Програма повинна перетворити його на число та вивести.
userString = input("Введіть рядок, який складається з цифр. Після введення числа натискаємо Enter \n")
userString = int (userString)
print(type(userString), userString)

# 5 Стрічкова конкатенація + математика:
# Користувач вводить два числа. Програма повинна вивести два прінти: перший — їхню суму,
# другий об'єднати їх. Якщо в нас числа 5 та 4, то результат повинен бути 9 та 54.
userNum_1 = input("Після введення числа натискаємо Enter \n")
userNum_2 = input("")
print("Сума:", int(userNum_1) + int(userNum_2))
print("Конкатенація:", userNum_1 + userNum_2)

# 6 Вік користувача:
# Запитати у користувача його рік народження, ім'я та який зараз рік (три змінні)
# та вивести на екран два прінти: ім'я та скільки років користувачу.
userYearOfBith = input("Рік народження Пана? \n")
userName = input("Як до Пана можна звертатися? \n")
userActualYear = input("Який зараз рік? \n")
print("Пан", userName, "Вам вже", int(userActualYear) - int(userYearOfBith), "рочків")

# 7 Перевод з цельсія в фаренгейт:
# Напишіть програму, яка запитує в користувача кількість градусів в цельсіях і повертає в фаренгейтах.
celsiusDegrees = float(input("Скільки градусів Цельсія? \n"))
convCelsiusToFarenheit = (celsiusDegrees * 9/5) + 32
print(convCelsiusToFarenheit)

# 8 Перевод з фаренгейта в цельсій:
# Напишіть програму, яка запитує в користувача кількість градусів в фаренгейтах і повертає в цельсіях.
# Вам може здатися, що ця задача така ж, як попередня, але будьте уважні і перевірте результат вручну.
farenheitDegrees = float(input("Скільки градусів Фаренгейту? \n"))
convFarenheitToCelsius = (farenheitDegrees - 32 ) * 5/9
print(convFarenheitToCelsius)

# 9 Теорема Піфагора:
# Запитайте у користувача довжини катетів та виведіть на екран довжину гіпотенузи.
# Трикутник рівнобедрений. Що б взвести в степінь ставимо два рази множення
# два в степені три буде так 2**3, квадратний корінь з двух буде 2**(1/2)
leg_1 = int(input("Трикутник рівнобедрений. Яка довжина катетів? \n"))
leg_2 = int(input())
hypotenuse = (leg_1**2 + leg_2**2)**(1/2)
print(hypotenuse)

# 10 Школярі та яблука
# n школярів ділять k яблук порівну, недільний залишок залишається в кошику.
# Скільки яблук дістанеться кожному школярові та скільки залишиться в кошику?
# Програма отримує на вхід числа n і k - цілі, додатні, не перевищують 10000.
n_schoolchildren = int(input("Введіть числа n (школярі) і k (яблуки) - цілі, додатні, які не перевищують 10000 \n"))
k_apples = int(input())
withoutRemainder = k_apples // n_schoolchildren
remainder = k_apples - (withoutRemainder * n_schoolchildren)
print(withoutRemainder, remainder)

# 11 Магазин канцелярських товарів
# Одного разу, відвідавши магазин канцелярських товарів, Вася купив X олівців, Y ручок та Z фломастерів. Відомо,
# що ціна ручки на 2 гривні більше ціни олівця та на 7 гривень менше ціни фломастера. Також відомо,
# що вартість олівця становить 3 гривні. Потрібно визначити загальну вартість покупки.
# Вхідні дані
# просимо користувача ввести три змінні
# кожне з яких не перевищує 109.
# Вихідні дані
# виведіть одне ціле число – вартість покупки в гривнях.
# приклад для перевірки програми 1
# ввів: 1 1 1
# отримав: 20
x_pencils = int(input("Скільки Вася купив олівців? <= 109 \n"))
pencilPrice = 3
y_pens = int(input("Скільки Вася купив ручок? <= 109 \n"))
penPrice = pencilPrice + 2
z_markers = int(input("Скільки Вася купив фломастерів? <= 109 \n"))
markerPrice = penPrice + 7
print((x_pencils * pencilPrice) + (y_pens * penPrice) + (z_markers * markerPrice), "грн.")

# 12 Циферблад
# Запитайте в користувача скільки хвилин пройшло з початку доби.
# Визначте, скільки годин і хвилин покаже електронний годинник в цей момент і поверніть йому результат (формататування тексту при ввиводі не важливе).
# приклад для перевірки програми 1
# користувач ввів:150
# користувач отримує: 2, 30
# приклад для перевірки програми 2
# користувач ввів:1441
# користувач отримує: 0, 1
userMinutes = int(input("Скільки хвилин пройшло з початку доби? \n"))
convHour = userMinutes // 60 % 24
print(convHour, userMinutes % 60)

# 13 Журавлики
# Петро, Катя та Сергій роблять з паперу журавликів. Разом вони зробили S журавликів.
# Скільки журавликів зробила кожна дитина, якщо відомо, що Петро та Сергій зробили однакову кількість журавликів,
# а Катя зробила в два рази більше журавликів, ніж Петро та Сергій разом.
# Вхідні дані
# Юзер вводить загальну кількість журавликів. Отримує три значення скільки зробив кожен (Петро, Катя та Сергій).
# У єдиному рядку вхідного файлу INPUT.TXT записано одне натуральне число S – загальна кількість зроблених журавликів (S < 106).
userCranes = int(input("Введіть загальну кількість журавликів \n"))
sPetr = userCranes / 6
sSerg = userCranes / 6
sKate = (sPetr + sSerg)  * 2
# sPetr = x, sSerg = x, sKate = 4x
print(sPetr, sSerg, sKate)

# 14 Податки
# Прийшов час податків і вам треба написати програму що б допомогти відділу бугалтерії
# програма приймає від користувача його зарплату за 3 місяці та відсоток який він має сплатити.
# Виведіть на екран скільки треба податків сплатити. Не забудьте ЄСВ(4422)
userSalaryMonth = int(input("Введіть зп за 3и місяці \n"))
userSalaryTax = float(input("Введіть сплачувальний відсоток \n"))
print("Потрібно сплатити:", (userSalaryMonth * (userSalaryTax / 100)) + 1474, "Податків з урахуванням ЄСВ(4422), 1474 грн.")

