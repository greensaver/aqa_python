# 1) Створіть клас Студент, в ньому обявіть дві змінні імя
# де збережети імя студента, та список його оцінок.
# створіть два метода в цьому класі, перший метод
# який буде вітатись і при вітання використовувати імя студента.
# другий метод буде виводити оцінки. Методи виводять результат через прінти.

# Створіть два екземпляра цього класу, в другому екземплярі
# змніть імя на своє(не міняючи нічого в класі). Вивідіть дві
# функції цих екземплярів, що б кожен студент привітався та сказав свої оцінки.


class StudentClass:
    hello_string: str
    name = ""
    list_grade = []

    def say_hello(self):
        self.hello_string = f"привіт {self.name}, як справи?"
        print(self.hello_string)

    def say_list_grade(self):
        print(f"твої оцінки: {self.list_grade}")


obj_1 = StudentClass()
obj_1.say_hello()
obj_1.say_list_grade()

obj_2 = StudentClass()
obj_2.name = "Sehii"
obj_2.say_hello()
obj_2.list_grade = [2, 3, 1, 5, 4]
obj_2.say_list_grade()
