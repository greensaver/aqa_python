import pytest


@pytest.mark.usefixtures("fixture_random")
class TestRandom:

    # перевірити поля "icon_url" чи він не пусти + чи це картинка,  - 2 теста
    def test_check_icon_url_not_empty(self):
        assert str(self.response.json()["icon_url"]) is not None, "'icon_url' is empty"

    def test_check_icon_url_format(self):
        assert str(self.response.json()["icon_url"]).split(".")[-1] == "png", "'.png' format is required"

    # перевірити чи є ключ "value"  і перевірити його значення - 2 теста
    def test_check_key_value(self):
        assert "value" in self.response.json(), "key 'value' is required"

    def test_check_value_not_empty(self):
        assert len(self.response.json()["value"]) > 0, "'value' is empty"

    def test_check_year(self):
        assert int(self.response.json()["created_at"][:4]) > 1990, "All our jokes were created until 1990"

    def test_status_code(self):
        assert self.status_code == 200


# Зробити окремий клас
# пошук жарту по конретному слову  https://api.chucknorris.io/jokes/search?query={query}
# зробити класому фікстуру
# тест на статус код
# тест на кількість жартів
# тест на сам жарт
# + 3 тести

@pytest.mark.usefixtures("fixture_search_bible")
class TestKeyWordJokes:

    def test_status_code(self):
        assert self.status_code == 200

    def test_amount_of_jokes(self):
        assert self.response.json()["total"] == 14

    def test_amount_of_jokes1(self):
        assert str(self.response.json()["result"][0]["value"]) is not None
