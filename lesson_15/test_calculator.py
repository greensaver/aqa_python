import pytest
from datetime import datetime
from lesson_15 import Calculator


# 3) Напишіть тестовий клас який буде тестити попередній калькулятор тільки додавання і ділення.
#  до кожної математичної дії зробіть 5 тестів(використовуйте параметрайз, не пишіть руками зайвого).
#  Зробіть класову фікстуру(класметод) для сетапа і тердауна сетпа буде писати повідомлення в файл коли ми запустили
#  тест
#  та текстове повідомлення що ми стартанули. Тердаун буде писати повідомлення що ми закінчили і також час коли
#  закінчили
#  використайте вже відому вам бібліотеку дататайм

class TestCalculator:

    @classmethod
    def setup_class(cls):
        cls.calc = Calculator()
        print("\n-------------------------------START-------------------------------\n")


    @classmethod
    def teardown_class(cls):
        finish_time = datetime.now().strftime("%H:%M:%S")
        with open('finish.txt', 'a') as file:
            file.write(f"Finish Time {finish_time}\n---------------------\n")
        print("\n-------------------------------END-------------------------------\n")

    @pytest.mark.parametrize("numb_1, numb_2, result", [
        pytest.param(3, 3, 6),
        pytest.param(-3, 4, 1),
        pytest.param(0, -0, 0),
        pytest.param(1.1, 2, 3.1),
        pytest.param(-3, -1, -4)])
    def test_plus(self, numb_1, numb_2, result):
        assert self.calc.plus(numb_1, numb_2) == result

    @pytest.mark.parametrize("numb_1, numb_2, result", [
        pytest.param(3, 3, 1),
        pytest.param(-3, 4, -0.75),
        pytest.param(0, 1, 0),
        pytest.param(1.1, 2, 0.55),
        pytest.param(-3, -1, 3.0)])
    def test_divide(self, numb_1, numb_2, result):
        assert self.calc.divide(numb_1, numb_2) == result
