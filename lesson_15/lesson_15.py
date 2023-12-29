# 1) Напишіть ліст компрехеншин який формує список всіх чисел від 34 до 121 які діляться націло на 3 та на 2

lst = [i for i in range(34, 122, 1) if i % 2 == 0 and i % 3 == 0]
print(lst)


# 2) Напишіть клас калькулятора де будуть 4 арифметичні дії плюс, мінус, додавання, множення - звичайні методи.
# і зробіть статік метод який буде виводити повідомлення, привіт я калькулятор.

class Calculator:

    def plus(self, x, y):
        return x + y

    def multiply(self, x, y):
        return x * y

    def minus(self, x, y):
        return x - y

    def divide(self, x, y):
        return x / y

    @staticmethod
    def hello_calculator():
        print("привіт я калькулятор")
