import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from lesson_26.src.pages.page_button import PageButton
from lesson_26.conftest import chrome_class


@pytest.mark.usefixtures("chrome_class")
class TestButtons:

    def setup_method(self):
        self.driver: WebDriver = self.driver
        self.page = PageButton(driver=self.driver)

    def test_button_click_example_xpath_1(self):
        self.page.open()
        self.page.button_click_example_xpath_1().click()
        pass

    def test_button_click_example_xpath_2(self):
        self.page.open()
        self.page.button_click_example_xpath_2().click()
        pass

    def test_button_click_example_xpath_3(self):
        self.page.open()
        self.page.button_click_example_xpath_3().click()
        pass

    def test_button_click_example_xpath_4(self):
        self.page.open()
        self.page.button_click_example_xpath_4().click()
        pass

    def test_button_click_example_xpath_5(self):
        self.page.open()
        self.page.button_click_example_xpath_5().click()
        pass

    def test_button_click_example_css_1(self):
        self.page.open()
        self.page.button_click_example_css_1().click()
        pass

    def test_button_click_example_css_2(self):
        self.page.open()
        self.page.button_click_example_css_1().click()
        pass

    def test_button_click_example_css_3(self):
        self.page.open()
        self.page.button_click_example_css_1().click()
        pass

    def test_button_click_example_css_4(self):
        self.page.open()
        self.page.button_click_example_css_1().click()
        pass

    def test_button_click_example_css_5(self):
        self.page.open()
        self.page.button_click_example_css_1().click()
        pass
