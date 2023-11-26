#  2-ий файл з трьома тестами який буде тестити ці три функції. В кожному тесті 1 тест.
#
# В тестових функціях ми ставимо типізацію. В першому файлі в всіх функціях проставляємо що приймає і що повертає.
# Встановіть собі пайтест і прораньте. До домашки отрім кода додайте скріншот прогона тестів.
#
# В понеділок домашки не буде. Але не відкладайте домашку.

from lesson_7_first_file import sort_list_increase, sort_list_decrease, sort_list_words_increase

def test_sort_list_increase():
    assert sort_list_increase([34, 456, 11, 12, -100, 77, 100, 35, 100.0, 100]) == [-100, 11, 12, 34, 35, 77, 100, 100.0, 100, 456]

def test_sort_list_decrease():
    assert sort_list_decrease([34, 456, 11, 12, -100, 77, 100, 35, 100.0, 100]) == [456, 100, 100.0, 100, 77, 35, 34, 12, 11, -100]

def test_sort_list_words_increase():
    assert sort_list_words_increase(['груша', 'грушаa', 'банан', 'яблуко', 'диня', "слива", "апельсин", "фу"]) == ['фу', 'диня', 'груша', 'банан', 'слива', 'грушаa', 'яблуко', 'апельсин']
