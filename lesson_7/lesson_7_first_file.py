# Створіть два файли в 1-му напишіть такі функції:
#
# 1) сортування списка по зростанню числа, від меншого до більшого. Функція приймає список з чисел і повертає
# відсортований список.

def sort_list_increase(x: list[int]) -> list[int]:
    return sorted(x, reverse=False)

# 2) сортування списка на спад, від  більшого до меншого. Функція приймає список з чисел
# і повертає відсортований список.

def sort_list_decrease(x: list[int]) -> list[int]:
    return sorted(x, reverse=True)

# 3) сортування за кількістю букв у слові. Функція приймає список з слів і повертає відсортований список.

def sort_list_words_increase(x: list[str]) -> list[str]:
    return sorted(x, key=len)

