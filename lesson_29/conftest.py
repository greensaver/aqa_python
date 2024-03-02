import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


@pytest.fixture(scope="class")
def chrome_class(request):
    service = Service(executable_path="/Users/Greensaver/PycharmProjects/pythonProject/lesson_29/chromedriver.exe")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()
