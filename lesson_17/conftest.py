import pytest
from selenium import webdriver


@pytest.fixture
def _chrome():
    driver = webdriver.Chrome(executable_path="/Users/Greensaver/PycharmProjects/pythonProject/lesson_17/chromedriver")
    yield driver
    driver.quit()
