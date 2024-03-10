import pytest
from lesson_31.conftest import car_page


@pytest.mark.usefixtures("car_page")
def test_car_brand(car_page):
    brands = car_page.get_car_brands()
    models = car_page.get_car_models()
    years = car_page.get_car_years()

    assert 'Кіберкопійка' in brands
    assert 'ЗАЗ-966' in models
    assert 1964 in years
