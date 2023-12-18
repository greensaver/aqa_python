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


class A:
    def __init__(self, text):
        self.text = text

    def __bool__(self):
        if len(self.text) < 20:
            return False
        return True

    def __eq__(self, other):  # ==
        print(abs(len(self.text) - len(other.text)))
        if not isinstance(other, type(self)):
            raise TypeError
        elif abs(len(self.text) - len(other.text)) < 10:
            return True
        else:
            return False


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __ne__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError
        else:
            return self.name != other.name or self.age != other.age

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError
        else:
            return self.name == other.name and self.age == other.age


obj_1 = Person(12, 12)
obj_2 = Person("12", 12)
a = A(12)

print(obj_1 != obj_2)
print(obj_1 == obj_2)
print(obj_1 == a)

obj_2.name = "qweqweqwe"
print(obj_2.name != obj_1.name)
