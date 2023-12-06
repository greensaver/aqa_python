# Задача 1
# 1) Напишіть 10 тестів(можна що б просто повертали Тру(щоб проходили)) імена тестів повині йти підряд
# test_1, test_2 ... . Повішайти на них три декоратора old, main, new. кожен декоратор повинен бути на 3 функціях
# на одній з функцій повино бути повішано два декоратора old i main.
# додайти їх в python.ini що б були правильні виводи
#
# Зробіть такі прогони
# 1) всі тексти де немає лейби old
# 2) тест де пересікаються old i main.
# 3) тести з маркерами main, new
# З домашкою здайте скріншоти з прогонами, на скріншотах повино бути
# видно який саме тест прогнався(використовуйте прапор verbose).

import pytest


@pytest.mark.old
@pytest.mark.main
@pytest.mark.new
def test_1():
    assert True


@pytest.mark.old
@pytest.mark.main
@pytest.mark.new
def test_2():
    assert True


@pytest.mark.old
@pytest.mark.main
@pytest.mark.new
def test_3():
    assert True


@pytest.mark.old
@pytest.mark.main
def test_4():
    assert True


@pytest.mark.main
def test_5():
    assert True


@pytest.mark.old
def test_6():
    assert True

@pytest.mark.new
def test_7():
    assert True


@pytest.mark.old
def test_8():
    assert True


@pytest.mark.main
def test_9():
    assert True

@pytest.mark.main
def test_10():
    assert True
