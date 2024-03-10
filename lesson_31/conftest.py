import sqlite3
import pytest
from lesson_31.src.pages.page_car import CarPage


@pytest.fixture(scope="session")
def car_page():
    connection = sqlite3.connect("C:/Users/Greensaver/PycharmProjects/pythonProject/lesson_31/cars.db")
    car_page = CarPage(connection)
    if not car_page.table_exists('cars'):
        car_page.create_car_table()
    yield car_page
    connection.close()