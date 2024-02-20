import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def chrome_class(request):
    service = Service(executable_path="/Users/Greensaver/PycharmProjects/pythonProject/lesson_26/chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")  # запуск від рута, треба при роботі СІСД
    options.add_argument("--disable-gpu")  # не використовує відеокарту
    options.add_argument("--headless")  # без графічної відмальовки браузера.
    driver = webdriver.Chrome(service=service, options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()


