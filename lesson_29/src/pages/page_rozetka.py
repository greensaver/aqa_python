from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://rozetka.com.ua/ua/"


class RozetkaPage:
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.driver.implicitly_wait(10)

    def open(self):
        self.driver.get(URL)
        return self

    def find_elements_by_class_name(self, class_name):
        return self.driver.find_elements(By.CLASS_NAME, class_name)

    def find_elements_by_xpass(self, xpath):
        return self.driver.find_elements(By.XPATH, xpath)

    def navigate_to_category(self, category_xpath, expected_url):
        category_link = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, category_xpath))
        )
        category_link.click()

        WebDriverWait(self.driver, 5).until(
            EC.url_to_be(expected_url)
        )

        assert self.driver.current_url == expected_url

        return self

    def parse_product_page(self):
        products = []

        product_elements = self.find_elements_by_class_name('goods-tile__inner')
        for product_element in product_elements:
            title_element = product_element.find_element(By.CLASS_NAME, 'goods-tile__title')
            price_element = product_element.find_element(By.CLASS_NAME, 'goods-tile__price-value')

            title = title_element.text.strip()
            price = price_element.text.strip()

            products.append({'title': title, 'price': price})

        return products

    def parse_and_write_products_to_file(self, filename):
        products = self.parse_product_page()

        with open(filename, 'a', encoding='utf-8') as file:
            for product in products:
                file.write(f"{product['title']}, {product['price']}\n")

        return self
