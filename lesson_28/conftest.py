import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def chrome_class(request):
    service = Service(executable_path="/Users/Greensaver/PycharmProjects/pythonProject/lesson_28/chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    # options.add_argument("--headless")
    driver = webdriver.Chrome(service=service, options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()

