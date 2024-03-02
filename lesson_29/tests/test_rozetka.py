import pytest
from lesson_29.src.pages.page_rozetka import RozetkaPage
from lesson_29.conftest import chrome_class


@pytest.mark.usefixtures("chrome_class")
class TestRozetkaPage:
    def setup(self, method):
        self.page = RozetkaPage(self.driver)

    def test_navigation_to_notebooks(self):
        self.page.open()

        products_page_1 = self.page.navigate_to_category("//a[@class='menu-categories__link']", "https://rozetka.com.ua/ua/computers-notebooks/c80253/") \
            .navigate_to_category("(//a[@class='tile-cats__picture ng-star-inserted'])[1]", "https://rozetka.com.ua/ua/notebooks/c80004/") \
            .parse_and_write_products_to_file('rozetka_products.txt') \
            .parse_product_page()

        self.page.open()

        products_page_2 = self.page.navigate_to_category("//a[@class='menu-categories__link']", "https://rozetka.com.ua/ua/computers-notebooks/c80253/") \
            .navigate_to_category("(//a[@class='tile-cats__picture ng-star-inserted'])[2]", "https://hard.rozetka.com.ua/ua/computers/c80095/") \
            .parse_and_write_products_to_file('rozetka_products.txt') \
            .parse_product_page()

        with open('rozetka_products.txt', 'w', encoding='utf-8') as file:
            text = ""
            text += "******** Сторінка 1 - Ноутбуки ********\n"
            for product in products_page_1:
                text += f"{product['title']}, {product['price']}\n"
            text += "\n"

            text += "******** Сторінка 2 - Комп'ютери ********\n"
            for product in products_page_2:
                text += f"{product['title']}, {product['price']}\n"

            file.write(text)
