import pytest
from selenium import webdriver

# C:\Users\Greensaver\PycharmProjects\pythonProject\lesson_17
# /Users/pavlokostyshen/Desktop/hillel/Hillel_october_23/lesson_17/chromedriver

@pytest.fixture
def chrome():
    driver = webdriver.Chrome(executable_path="/Users/Greensaver/PycharmProjects/pythonProject/lesson_17/chromedriver")
    yield driver
    driver.quit()