import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def chrome():
    service = Service(executable_path="/Users/Greensaver/PycharmProjects/pythonProject/lesson_20/chromedriver.exe")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def firefox(request):
    service = Service(executable_path="/Users/Greensaver/PycharmProjects/pythonProject/lesson_20/geckodriver.exe")
    options = webdriver.ChromeOptions()
    driver = webdriver.Firefox(service=service, options=options)
    request.cls.driver = driver
    driver.implicitly_wait(5)  # імплісіті вейт це вся реалізація
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def chrome_class(request):
    service = Service(executable_path="/Users/Greensaver/PycharmProjects/pythonProject/lesson_20/chromedriver.exe")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()
