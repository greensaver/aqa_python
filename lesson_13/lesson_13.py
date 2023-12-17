# Виберіть який з наступних магічних методів і реалізуйте його в простому класі:
#
# __ne__: To check if two objects are not equal.
#
# __lt__: To check if one object is less than another.
#
# __le__: To check if one object is less than or equal to another.
#
# __gt__: To check if one object is greater than another.
#
# __ge__: To check if one object is greater than or equal to another.
#
# Жодного з цих методів ми не розглядали на уроці, але вони працюють ідентично до метода ___eq__
# який ми розглянули на уроці. Тобто вам треба буде змінити всього дві букви.
#
# І написати свою логіку яку ви хочте.
#
# Створіть два обьєта класа в якому ви це реалізували і зробіть перевірку що все працює


class Person:
    def __init__(self, name, age, smile):
        self.name = name
        self.age = age
        self.smile = smile

    def __str__(self):
        return f" Name: {self.name} \n Age: {self.age} \n Face: {self.smile} "

    def __eq__(self, other):
        print(abs(len(self.name) - len(other.name)))
        if not isinstance(other, type(self)):
            raise TypeError
        elif abs(len(self.name) - len(other.name)) < 10:
            return True
        else:
            return False

    def __ne__(self, other):
        return self.name != other.name, self.age != other.age, self.smile != other.smile


obj_1 = Person("Serhii", 18, "😎")
obj_2 = Person("_loGin", 18, "0_o")

print(obj_1)
print(obj_1 != obj_2)
print(obj_2 == obj_1)
