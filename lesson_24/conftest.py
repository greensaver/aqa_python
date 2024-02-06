import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def chrome():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")  # запуск від рута, треба при роботі СІСД
    options.add_argument("--disable-gpu")  # не використовує відеокарту
    options.add_argument("--headless")  # без графічної відмальовки браузера.
    service = Service(options=options, executable_path="/Users/Greensaver/PycharmProjects/pythonProject/lesson_24/chromedriver.exe")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def firefox(request):
    service = Service(executable_path="/Users/Greensaver/PycharmProjects/pythonProject/lesson_24/geckodriver")
    options = webdriver.ChromeOptions()
    driver = webdriver.Firefox(service=service, options=options)
    request.cls.driver = driver
    driver.implicitly_wait(5)  # імплісіті вейт це вся реалізація
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def chrome_class(request):
    service = Service(executable_path="/Users/Greensaver/PycharmProjects/pythonProject/lesson_24/chromedriver.exe")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()

#фікстура яка приймає декілька параметрів.
@pytest.fixture(scope="class", params=['fashion', 'food', 'history'])
def fixture_chuck_category(request):
    category = request.param
    URL = f"https://api.chucknorris.io/jokes/random?category={category}"
    print(URL)
    response = requests.request(method="GET", url=URL)
    request.cls.response = response
    yield response
